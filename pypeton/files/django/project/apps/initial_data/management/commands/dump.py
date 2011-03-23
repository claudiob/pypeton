# Run python manage.py dump to dump a model's data into a fixture

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
import logging
from os import system        

class Command(BaseCommand):
    help = "Dump a model's data into a fixture."

    def handle(self, *args, **options):
        """
        Dump a model's data into a fixture.
        Example: python manage.py pictures development
        """
        # TODO: Raise an error if an argument is not passed
        model = args[0]
        indent = " --indent=4"
        environment = " --settings=settings.%%s" %% args[1]
        output = "apps/%%s/fixtures/%%s.json" %% (args[0], args[1])
        system('python manage.py dumpdata %%s %%s %%s > %%s' %% 
            (model, indent, environment, output))
        logging.info("Dump success")
