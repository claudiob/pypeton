# Run python manage.py require to reload the python requirements

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
import logging
from os import system        

class Command(BaseCommand):
    help = "Install the python requirements for the project."

    def handle(self, *args, **options):
        """
        Install the python requirements.
        """
        system('pip install -r ../deploy/requirements.txt')
        logging.info("Require success")
