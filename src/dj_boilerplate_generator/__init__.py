# dj_boilerplate_generator/__init__.py
"""
Ultimate Django Boilerplate Generator - Enterprise Edition
Phase 1: Foundation & Core Architecture
"""

__version__ = "1.0.0"
__author__ = "Enterprise Django Team"
__email__ = "dev@enterprise-django.com"

from .cli import main
from  dj_boilerplate_generator.generators.base_generator import BaseGenerator

__all__ = ['main', 'BaseGenerator']