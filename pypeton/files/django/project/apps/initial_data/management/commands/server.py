# Run python manage.py server to run the server in a given environment

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
import logging
from os import system        

class Command(BaseCommand):
    help = "Call runserver with a given environment."

    def handle(self, *args, **options):
        """
        Call runserver with a given environment.
        """
        # TODO: Raise an error if an argument is not passed
        environment = " --settings=settings.%%s" %% args[0]
        system('python manage.py runserver 0.0.0.0:8000 %%s' %% environment)
        logging.info("Require success")
