#!/usr/bin/env python
from setuptools import setup
from os.path import dirname, join

import bitexen_client

here = dirname(__file__)

setup(name='bitexen_client',
      version=bitexen_client.version.__version__,
      description='Python Client for Bitexen API',
      url=bitexen_client.version.__url__,
      long_description=open(join(here, 'README.md')).read(),
      author='Bitexen Development Team',
      author_email='development@bitexen.com',
      install_requires=[
          'requests',
          'websocket-client'
      ],
      packages=['bitexen_client', 'bitexen_client.utils'],
      )