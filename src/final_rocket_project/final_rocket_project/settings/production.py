
"""
Production Settings for final_rocket_project
"""

from .base import *

DEBUG = False

# Security settings for production
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Production logging
LOGGING['handlers']['file'] = {
    'level': 'ERROR',
    'class': 'logging.FileHandler',
    'filename': '/var/log/django/error.log',
}
LOGGING['root']['handlers'] = ['file', 'console']
