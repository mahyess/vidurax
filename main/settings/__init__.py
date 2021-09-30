from . import base

DEBUG = True

if not DEBUG:
    from . import production
