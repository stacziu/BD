from django.core.management.base import BaseCommand
from libraryapp.utils import check_overdue_loans

class Command(BaseCommand):
    help = 'Check overdue loans and apply fines'

    def handle(self, *args, **kwargs):
        check_overdue_loans()
        self.stdout.write(self.style.SUCCESS('Overdue loans processed successfully'))
