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
        host = "0.0.0.0:8000"
        environment = "--settings=settings.%%s" %% args[0]
        adminmedia = "--adminmedia=static/admin"
        system('python manage.py runserver %%s %%s %%s' %% 
            (host, environment, adminmedia))
        logging.info("Require success")
