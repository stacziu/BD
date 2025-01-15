# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class Authors(models.Model):
    author_id = models.AutoField(primary_key=True)
    author_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'authors'


class Books(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    publisher = models.CharField(max_length=45)
    published_year = models.CharField(max_length=4)
    image = models.ImageField(upload_to='book_images/', blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'books'


class Booksauthors(models.Model):
    book = models.OneToOneField(Books, models.DO_NOTHING, primary_key=True)
    author = models.ForeignKey(Authors, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'booksauthors'


class Booksgenres(models.Model):
    book = models.OneToOneField(Books, models.DO_NOTHING, primary_key=True)  # The composite primary key (book_id, genre_id) found, that is not supported. The first column is selected.
    genre = models.ForeignKey('Genres', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'booksgenres'
        unique_together = (('book', 'genre'),)


class Fines(models.Model):
    fine_id = models.AutoField(primary_key=True)  # The composite primary key (fine_id, user_id, loans_loan_id) found, that is not supported. The first column is selected.
    user = models.ForeignKey('Users', models.DO_NOTHING)
    amount = models.DecimalField(max_digits=4, decimal_places=2)
    issued_date = models.DateField()
    status = models.IntegerField()
    loans_loan = models.ForeignKey('Loans', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'fines'
        unique_together = (('fine_id', 'user', 'loans_loan'),)


class Genres(models.Model):
    genre_id = models.AutoField(primary_key=True)
    genre_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'genres'


class Holds(models.Model):
    hold_id = models.AutoField(primary_key=True)  # The composite primary key (hold_id, user_id, physical_book_id) found, that is not supported. The first column is selected.
    user = models.ForeignKey('Users', models.DO_NOTHING)
    physical_book = models.ForeignKey('PhysicalBooks', models.DO_NOTHING)
    hold_date = models.DateField()
    release_date = models.DateField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'holds'
        unique_together = (('hold_id', 'user', 'physical_book'),)


class Loans(models.Model):
    loan_id = models.AutoField(primary_key=True)  # The composite primary key (loan_id, user_id, physical_book_id) found, that is not supported. The first column is selected.
    user = models.ForeignKey('Users', models.DO_NOTHING)
    physical_book = models.ForeignKey('PhysicalBooks', models.DO_NOTHING)
    loan_date = models.DateField()
    return_date = models.DateField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'loans'
        unique_together = (('loan_id', 'user', 'physical_book'),)


class Notifictions(models.Model):
    notification_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    message = models.CharField(max_length=255)
    sent_date = models.DateField()
    notification_read = models.IntegerField()
    loan = models.ForeignKey(Loans, models.DO_NOTHING, blank=True, null=True)
    fines = models.ForeignKey(Fines, models.DO_NOTHING, blank=True, null=True)
    hold = models.ForeignKey(Holds, models.DO_NOTHING, blank=True, null=True)
    notifiction_type = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'notifictions'


class PhysicalBooks(models.Model):
    physical_book_id = models.AutoField(primary_key=True)  # The composite primary key (physical_book_id, book_id) found, that is not supported. The first column is selected.
    state = models.IntegerField()
    book = models.ForeignKey(Books, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'physical_books'
        unique_together = (('physical_book_id', 'book'),)


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    role = models.CharField(max_length=5)
    password_hash = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Contact(models.Model):
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    working_hours = models.CharField(max_length=100)

    def __str__(self):
        return "Contact Information"


class FAQ(models.Model):
    question = models.CharField(max_length=255)  # Pytanie
    answer = models.TextField()  # Odpowiedź

    def __str__(self):
        return self.question
