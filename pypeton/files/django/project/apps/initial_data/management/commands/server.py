# Run python manage.py server to run the server in a given environment

from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
import logging

class Command(BaseCommand):
    help = "Call runserver with a given environment."

    def handle(self, *args, **options):
        """
        Call runserver with a given environment.
        """
        call_command('runserver', '0.0.0.0:8000')
        logging.info("Require success")
