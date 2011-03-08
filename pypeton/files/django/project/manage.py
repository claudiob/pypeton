#!/usr/bin/env python
from django.core.management import execute_manager
import sys, os.path
try:
    import settings # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("%(yellow)sHelp! [%(blue)ssettings.py%(yellow)s] is gone!%(normal)s\\n")
    sys.exit(1)

if __name__ == "__main__":
    execute_manager(settings)
