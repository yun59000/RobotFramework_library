#!/usr/bin/env python

from os.path import join, dirname
from setuptools import setup
# from CSVLibrary.version import VERSION
VERSION = '0.0.3'

filename = join(dirname(__file__), 'CSVLibrary', 'version.py')

# execfile(join(dirname(__file__), 'CSVLibrary', 'version.py'))

exec(compile(open(filename, "rb").read(), filename, 'exec'), {})



DESCRIPTION = """
CSV file support for Robot Framework.
"""[1:-1]

setup(name         = 'robotframework-csvlibrary',
      version      = VERSION,
      description  = 'CSV library for Robot Framework',
      long_description = DESCRIPTION,
      author       = 'Marcin Mierzejewski',
      author_email = '<mmierz@gmail.com>',
      url          = 'https://github.com/s4int/robotframework-CSVLibrary',
      license      = 'Apache License 2.0',
      keywords     = 'robotframework testing csv',
      platforms    = 'any',
      classifiers  = [
          "Development Status :: 4 - Beta",
          "License :: OSI Approved :: Apache Software License",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Software Development :: Testing"
      ],
      install_requires = [
          'robotframework >= 2.6.0',
      ],
      packages    = ['CSVLibrary'],
      )
