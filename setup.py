#!/usr/bin/env python
from os.path import dirname, join
from setuptools import setup

import bitexen_client

here = dirname(__file__)

setup(
    name='bitexen_client',
    version=bitexen_client.version.__version__,
    description='Python Client for Bitexen API',
    url=bitexen_client.version.__url__,
    long_description=open(join(here, 'README.md')).read(),
    author='Bitexen Development Team',
    author_email='development@bitexen.com',
    install_requires=['requests'],
    packages=['bitexen_client', 'bitexen_client.utils'],
)
