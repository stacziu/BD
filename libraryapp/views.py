from django.http import HttpResponse

from .forms import UserRegistrationForm, LoginForm, ContactForm, FAQForm
from .models import Users, Books, PhysicalBooks, Booksauthors, Booksgenres, Authors, Genres, Holds, Loans, Contact, FAQ, Fines
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.core.files.storage import FileSystemStorage
from django.shortcuts import get_object_or_404
from django.contrib import messages
import datetime

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user to the MySQL database
            return redirect('login')  # Redirect to login page
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    error_message = None
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
                user = Users.objects.get(username=username)
                if check_password(password, user.password_hash):
                    # Create a session
                    request.session['user_id'] = user.user_id
                    request.session['username'] = user.username
                    return redirect('home')  # Redirect to home page
                else:
                    error_message = "Invalid password!"
            except Users.DoesNotExist:
                error_message = "User does not exist!"

    return render(request, 'login.html', {'form': form, 'error_message': error_message})

def logout_view(request):
    # Clear the session data
    request.session.flush()
    return redirect('home')

def add_book(request):
    if request.method == 'POST':
        # Create the book
        title = request.POST['title']
        publisher = request.POST['publisher']
        published_year = request.POST['published_year']
        number_of_copies = int(request.POST['number_of_copies'])

        # Handle the image
        image = request.FILES.get('image')
        if image:
            fs = FileSystemStorage()
            image_path = fs.save(image.name, image)
        else:
            image_path = None

        # Create the book object with the image path
        book = Books.objects.create(
            title=title,
            publisher=publisher,
            published_year=published_year,
            image=image_path
        )

        # Handle authors
        author_names = request.POST['authors'].split(',')
        for name in author_names:
            author, created = Authors.objects.get_or_create(author_name=name.strip())
            Booksauthors.objects.create(book=book, author=author)

        # Handle genres
        genre_names = request.POST['genres'].split(',')
        for name in genre_names:
            genre, created = Genres.objects.get_or_create(genre_name=name.strip())
            Booksgenres.objects.create(book=book, genre=genre)

        # Create physical copies
        for i in range(number_of_copies):
            PhysicalBooks.objects.create(book=book, state=1)

        return redirect('home')

    return render(request, 'add_book.html')

def index(request):
    # Fetch all books
    books = Books.objects.all()

    # Apply search and category filters
    query_genres = request.GET.get('q')
    query_authors = request.GET.get('a')
    category_id = request.GET.get('genre')
    print("Selected category ID:", category_id)

    if query_genres:
        books = books.filter(title__icontains=query_genres)

    if category_id:
        books = books.filter(booksgenres__genre_id=category_id)

    if query_authors:
        books = books.filter(booksauthors__author__author_name__icontains=query_authors)

    # Prepare books with genres
    books_with_genres = []
    for book in books:
        genres = Booksgenres.objects.filter(book=book).select_related('genre')
        authors = Booksauthors.objects.filter(book=book).select_related('author')
        genre_names = ", ".join([g.genre.genre_name for g in genres])
        books_with_genres.append({
            'id': book.book_id,
            'title': book.title,
            'published_year': book.published_year,
            'genre_names': genre_names,
            'image': book.image.url if book.image else None,
            'authors': authors
        })

    # Fetch all genres for the dropdown
    genres = Genres.objects.all()

    return render(request, 'index.html', {
        'books': books_with_genres,
        'genres': genres
    })

def book_detail(request, book_id):
    try:
        # Get the book and its related details
        book = Books.objects.get(pk=book_id)
        genres = Booksgenres.objects.filter(book=book).select_related('genre')
        genre_names = ", ".join([g.genre.genre_name for g in genres])
        authors = Booksauthors.objects.filter(book=book).select_related('author')
        author_names = ", ".join([a.author.author_name for a in authors])
        copies = PhysicalBooks.objects.filter(book_id=book_id, state=1).count()
        # Pass the book's details to the template
        context = {
            'book_id': book.book_id,
            'book': book,
            'genre_names': genre_names,
            'author_names': author_names,
            'image': book.image.url if book.image else None,
            'copies': copies,

        }
        return render(request, 'book_detail.html', context)
    except Books.DoesNotExist:
        return HttpResponse("Book not found.", status=404)

def edit_book(request, book_id):

    # Retrieve the book to edit
    book = get_object_or_404(Books, pk=book_id)
    physical_books = PhysicalBooks.objects.filter(book=book)

    if request.method == 'POST':
        # Update book details
        book.title = request.POST['title']
        book.publisher = request.POST['publisher']
        book.published_year = request.POST['published_year']

        # Handle image upload
        image = request.FILES.get('image')
        if image:
            fs = FileSystemStorage()
            image_path = fs.save(image.name, image)
            book.image = image_path

        book.save()

        # Update authors
        Booksauthors.objects.filter(book=book).delete()
        author_names = request.POST['authors'].split(',')
        for name in author_names:
            author, created = Authors.objects.get_or_create(author_name=name.strip())
            Booksauthors.objects.create(book=book, author=author)

        # Update genres
        Booksgenres.objects.filter(book=book).delete()
        genre_names = request.POST['genres'].split(',')
        for name in genre_names:
            genre, created = Genres.objects.get_or_create(genre_name=name.strip())
            Booksgenres.objects.create(book=book, genre=genre)


        return redirect('book_detail', book_id=book.book_id)

    # Pass existing book data to the form
    authors = ", ".join(
        [author.author_name for author in Authors.objects.filter(booksauthors__book=book)]
    )
    genres = ", ".join(
        [genre.genre_name for genre in Genres.objects.filter(booksgenres__book=book)]
    )


    return render(request, 'edit_book.html', {
        'book': book,
        'authors': authors,
        'genres': genres,
        'physical_books': physical_books,
    })

def delete_physical_book(request, book_id):
    if request.method == 'POST':
        physical_book = get_object_or_404(PhysicalBooks, pk=book_id)
        associated_book = physical_book.book
        physical_book.delete()
        return redirect('edit_book', book_id=associated_book.book_id)

def add_physical_book(request, book_id):
    if request.method == "POST":
        # Get the book object
        book = get_object_or_404(Books, book_id=book_id)
        # Create a new physical book (default state = 1, "available")
        PhysicalBooks.objects.create(book=book, state=1)
        # Redirect back to the edit page
        return redirect('edit_book', book_id=book.book_id)

def place_hold(request, book_id):
    # Retrieve the custom user from your session
    custom_user = request.session.get('user_id')

    # Ensure the user is logged in
    if not custom_user:
        messages.error(request, "You need to be logged in to place a hold.")
        return redirect('login')  # Redirect to your login page

    # Retrieve the Users instance from your custom model
    try:

        user = get_object_or_404(Users, user_id=custom_user)
        # Get the book and ensure it's available
        physical_book = PhysicalBooks.objects.filter(book_id=book_id, state=1).first()
        if physical_book.state == 1:  # Assuming 1 means 'available'
            # Create a hold entry
            hold = Holds.objects.create(
                user=user,
                physical_book=physical_book,
                hold_date=datetime.date.today(),
                release_date=datetime.date.today() + datetime.timedelta(days=3),
                status=1  # Status 1 means "active hold"
            )
            physical_book.state = 0
            physical_book.save()
            messages.success(request, "Hold placed successfully!")
            return redirect(f'/book/{book_id}/')  # Redirect to book details
        else:
            messages.error(request, "This book is not available.")
            return redirect(f'/book/{book_id}/')
    except Books.DoesNotExist:
        return HttpResponse("Book not existing.", status=404)

def approve_loan(request, hold_id):
    if request.method == "POST":
        hold = get_object_or_404(Holds, hold_id=hold_id)
        Loans.objects.create(
            user=hold.user,
            physical_book=hold.physical_book,
            loan_date=datetime.date.today(),
            return_date=datetime.date.today() + datetime.timedelta(days=14),
            status=1
        )
        # Delete the hold entry
        hold.delete()
        return redirect('active_holds')

def cancel_hold(request, hold_id):
    if request.method == "POST":
        hold = get_object_or_404(Holds, hold_id=hold_id)
        # Mark the physical book as available
        hold.physical_book.state = 1
        hold.physical_book.save()
        # Delete the hold entry
        hold.delete()
        return redirect('active_holds')

def mark_returned(request, loan_id):
    if request.method == "POST":
        loan = get_object_or_404(Loans, loan_id=loan_id)

        unpaid_fine = Fines.objects.filter(loans_loan=loan, status=1).exists()
        if unpaid_fine:
            # Notify the user that the loan cannot be marked as returned due to unpaid fines
            messages.error(request, "This loan has unpaid fines. Please clear the fines before marking it as returned.")
            return redirect('active_loans')

            # If no unpaid fines, proceed to mark the loan as returned
        loan.status = 0  # Assuming 0 means 'returned'
        loan.save()

        # Mark the physical book as available
        loan.physical_book.state = 1  # Assuming 1 means 'available'
        loan.physical_book.save()

        # Provide success feedback to the user
        messages.success(request, "The loan has been successfully marked as returned.")
        return redirect('active_loans')

def active_holds(request):
    holds = Holds.objects.filter(status=1)  # Fetch active holds
    return render(request, 'holds.html', {'holds': holds})

def loans_view(request):
    search_query = request.GET.get('search')
    sort_option = request.GET.get('sort')
    loans = Loans.objects.select_related('user', 'physical_book__book')


    # Filter by search query (username)
    if search_query:
        loans = loans.filter(user__username__icontains=search_query)

    # Sorting logic
    if sort_option == 'loan_date_asc':
        loans = loans.order_by('loan_date')
    elif sort_option == 'loan_date_desc':
        loans = loans.order_by('-loan_date')

    today = datetime.date.today()


    active_loans = loans.filter(status=1, return_date__gte=today)
    overdue_loans = loans.filter(status=1, return_date__lt=today)

    return render(request, 'loans.html', {
        'active_loans': active_loans,
        'overdue_loans': overdue_loans,
    })

def mark_paid(request, fine_id):
    if request.method == "POST":
        fine = get_object_or_404(Fines, fine_id=fine_id)

        fine.status = 0
        fine.save()

        return redirect('fines')

def active_fines(request):
    search_query = request.GET.get('search')
    sort_option = request.GET.get('sort')
    fines = Fines.objects.select_related('user')

    # Filter by search query (username)
    if search_query:
        fines = fines.filter(user__username__icontains=search_query)

    # Sorting logic
    if sort_option == 'fine_date_asc':
        fines = fines.order_by('issued_date')
    elif sort_option == 'fine_date_desc':
        fines = fines.order_by('-issued_date')


    unpaid_fines = fines.filter(status=1)


    return render(request, 'active_fines.html', {
        'unpaid_fines': unpaid_fines,
    })

def contact(request):
    contact_info, created = Contact.objects.get_or_create(pk=1, defaults={
        'phone': '+48 123-456-789',  # Wartości domyślne
        'email': 'contact@example.com',
        'address': '123 Main Street',
        'working_hours': '9 AM - 5 PM',
    })

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact_info)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm(instance=contact_info)

    return render(request, 'contact.html', {'form': form, 'contact_info': contact_info})

def faq(request):
    faqs = FAQ.objects.all()  # Pobranie wszystkich pytań i odpowiedzi
    return render(request, 'faq.html', {'faqs': faqs})

def users(request):
    if request.method == "POST":
        # Pobierz słownik ról z formularza
        roles = request.POST  # Now this will be a dictionary of "roles[user_id] = role"

        for user_id, role in roles.items():
            if user_id.startswith('roles[') and user_id.endswith(']'):
                # Extract the user_id from the key format "roles[user_id]"
                user_id = user_id[6:-1]  # "roles[1]" becomes "1"
                try:
                    user = Users.objects.get(user_id=user_id)
                    user.role = role
                    user.save()
                except Users.DoesNotExist:
                    continue

        return redirect("users")  # Redirect to the same page after updating the roles

    # For GET requests, retrieve the list of users
    users_list = Users.objects.all()

    # Get the currently logged-in user from the session
    custom_user = None
    user_id = request.session.get('user_id')
    if user_id:
        try:
            custom_user = Users.objects.get(user_id=user_id)
        except Users.DoesNotExist:
            pass  # If the user doesn't exist, `custom_user` remains None

    return render(request, "users.html", {"users": users_list, "custom_user": custom_user})

def update_profile(request):
    if request.method == 'POST':
        user_id = request.session.get('user_id')
        if not user_id:
            return HttpResponse("You are not logged in.", status=401)

        try:
            user = Users.objects.get(pk=user_id)
            user.first_name = request.POST.get("first_name", user.first_name)
            user.last_name = request.POST.get("last_name", user.last_name)
            user.email = request.POST.get("email", user.email)
            user.phone_number = request.POST.get("phone_number", user.phone_number)
            user.role = request.POST.get("role", user.role)
            user.save()
            return redirect('/profile/')
        except Users.DoesNotExist:
            return HttpResponse("User not found.", status=404)
    else:
        user_id = request.session.get('user_id')
        if not user_id:
            return redirect('/login')


        # Fetch loans for the user and calculate derived fields
        loans = Loans.objects.filter(user_id=user_id, status = 1).select_related('physical_book')
        fines = Fines.objects.filter(user_id=user_id).select_related('loans_loan')


        loan_details = []
        for loan in loans:
            # Find the fine associated with this loan
            fine = fines.filter(loans_loan=loan).first()
            fine_amount = fine.amount if fine else 0.00
            fine_status = 'Paid' if fine and fine.status == 0 else 'Unpaid'
            issued_date = fine.issued_date if fine else None

            loan_details.append({
                'book_title': loan.physical_book.book.title,  # Assuming PhysicalBooks has a 'title' field
                'loan_date': loan.loan_date,
                'return_date': loan.return_date,
                'days_remaining': (loan.return_date - datetime.date.today()).days if loan.status == 1 else "N/A",
                'fine_amount': f"${fine_amount:.2f}",
                'fine_status': fine_status,
                'issued_date': issued_date,
                'status': 'Active' if loan.status == 1 else 'Returned',
            })

        user = Users.objects.get(pk=user_id)
        return render(request, 'profile.html', {'user': user, 'loans': loan_details})

