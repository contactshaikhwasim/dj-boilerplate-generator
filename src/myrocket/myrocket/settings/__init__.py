
"""
Enterprise Django Settings - Auto-configured based on environment
"""

import os
from .base import *

# Environment detection
DJANGO_ENV = os.environ.get('DJANGO_ENV', 'development')

if DJANGO_ENV == 'production':
    from .production import *
elif DJANGO_ENV == 'testing':
    from .testing import *
else:
    from .development import *


# Import original settings to maintain compatibility
try:
    from .original_settings import *
except ImportError:
    pass
