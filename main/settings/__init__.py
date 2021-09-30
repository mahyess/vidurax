import os
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = int(config("DEBUG", True))
DEBUG = True

if DEBUG:
    pass
    # from .local import *
else:
    from .production import *
