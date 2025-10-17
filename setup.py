#!/usr/bin/env python
from os.path import dirname, join

import setuptools

here = dirname(__file__)


def get_version():
    version_file = join(here, "bitexen_client", "version.py")
    version_dict = {}
    with open(version_file) as f:
        exec(f.read(), version_dict)
    return version_dict["__version__"], version_dict["__url__"]


version, url = get_version()

setuptools.setup(
    name="bitexen_client",
    version=version,
    description="Python Client for Bitexen API",
    url=url,
    long_description=open(join(here, "README.md")).read(),
    long_description_content_type="text/markdown",
    author="Bitexen Development Team",
    author_email="development@bitexen.com",
    install_requires=["requests"],
    packages=["bitexen_client", "bitexen_client.utils"],
    python_requires=">=3.7",
)
