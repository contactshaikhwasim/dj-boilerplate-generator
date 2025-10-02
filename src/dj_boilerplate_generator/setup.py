# setup.py
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dj-boilerplate-generator",
    version="1.0.0",
    author="Enterprise Django Team",
    author_email="dev@enterprise-django.com",
    description="Ultimate Django Boilerplate Generator - Enterprise Edition",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/enterprise-django/boilerplate-generator",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.10",
    install_requires=[
        "click>=8.0.0",
        "questionary>=1.10.0",
        "rich>=13.0.0",
        "jinja2>=3.0.0",
        "python-decouple>=3.8",
        "dj-database-url>=1.0.0",
    ],
    entry_points={
        "console_scripts": [
            "django-enterprise=dj_boilerplate_generator.cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "dj_boilerplate_generator": ["templates/phase1/**/*"],
    },
)