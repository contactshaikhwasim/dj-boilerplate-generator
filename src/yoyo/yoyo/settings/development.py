
"""
Development Settings for yoyo
"""

from .base import *

DEBUG = True

# Development-specific apps
DEV_APPS = [
    'debug_toolbar',
]

INSTALLED_APPS += DEV_APPS

# Debug Toolbar middleware
MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')

# Debug Toolbar configuration
INTERNAL_IPS = [
    '127.0.0.1',
]

# Email configuration for development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Allow all hosts for development
ALLOWED_HOSTS = ['*']
