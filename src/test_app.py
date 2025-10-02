#!/usr/bin/env python3
"""
Test runner for direct execution without pip installation
"""

import sys
import os

# Add the src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Now import and run the CLI
from dj_boilerplate_generator.cli import main

if __name__ == "__main__":
    main()