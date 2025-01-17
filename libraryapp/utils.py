from django.utils.timezone import now
from decimal import Decimal  # Import Decimal
from libraryapp.models import Loans, Fines

def check_overdue_loans():
    overdue_loans = Loans.objects.filter(status=1, return_date__lt=now().date())
    for loan in overdue_loans:
        fine, created = Fines.objects.get_or_create(
            user=loan.user,
            loans_loan=loan,
            defaults={'amount': Decimal('0.00'), 'issued_date': now().date(), 'status': 1}
        )
        if not created:
            days_overdue = (now().date() - loan.return_date).days
            fine.amount = Decimal(days_overdue) * Decimal('0.20')  # Convert to Decimal
            fine.save()
