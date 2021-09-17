"""
~~~~~~~~~~~
Dictalchemy
~~~~~~~~~~~

Contains asdict() and fromdict() methods that will work on SQLAlchemy
declarative models.

Read more in the source or on github
<https://github.com/danielholmstrom/dictalchemy>.
"""

import os

from setuptools import find_packages
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, "README.rst")).read()

# Requirements for the package
install_requires = [
    "SQLAlchemy>=0.9.4",
]

# Requirement for running tests
test_requires = install_requires

setup(
    name="dictalchemy3",
    version="1.0.0",
    description="Contains asdict and fromdict methods for SQL-Alchemy declarative models",
    long_description=README,
    url="http://github.com/disko/dictalchemy3/",
    license="MIT",
    author="Daniel Holmstrom",
    author_email="holmstrom.daniel@gmail.com",
    platforms="any",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: " "Libraries :: Python Modules",
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    tests_require=test_requires,
    test_suite="dictalchemy",
)
