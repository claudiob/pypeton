# Run python manage.py require to load the requirements in a given environment

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
import logging
from os import system        

class Command(BaseCommand):
    help = "Install the python requirements for a given environment."
    can_import_settings = False
    requires_model_validation = False

    def handle(self, *args, **options):
        """
        Install the python requirements for a given environment.
        """
        # TODO: Raise an error if an argument is not passed
        system('pip install -r ../deploy/requirements.txt')
        system('pip install -r ../deploy/requirements/%%s.txt' %% args[0])
        logging.info("Require success")
