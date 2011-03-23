# Run python manage.py upload to synchronize assets between servers

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
import logging
from os import system        

class Command(BaseCommand):
    help = "Synchronize assets between servers."

    def handle(self, *args, **options):
        """
        Synchronize assets between servers.
        """
        # TODO: Raise an error if an argument is not passed
        environment = " --settings=settings.%%s" %% args[0]
        system('python manage.py syncstatic %%s' %% environment)
        logging.info("Upload success")
