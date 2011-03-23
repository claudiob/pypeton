# Run python manage.py sync to swipe, synchronize and pre-fill the database

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
import logging
from os import system        

class Command(BaseCommand):
    help = "Swipes, syncs and loads the database with fixtures."

    def handle(self, *args, **options):
        """
        Swipes, syncs and loads the database with fixtures.
        """
        # TODO: Raise an error if an argument is not passed
        environment = " --settings=settings.%%s" %% args[0]
        system('python manage.py reset_db %%s' %% environment)
        system('python manage.py syncdb %%s' %% environment)
        system('python manage.py loaddata %%s %%s' %% (args[0], environment))
        logging.info("Sync success")
