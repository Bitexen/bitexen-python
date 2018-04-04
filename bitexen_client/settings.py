from __future__ import absolute_import

import importlib
import os
import sys

from bitexen_client.utils.dotdict import dotdict

def import_path(fullpath):
    """
    Import a file with full path specification. Allows one to
    import from anywhere, something __import__ does not do.
    """
    path, filename = os.path.split(fullpath)
    filename, ext = os.path.splitext(filename)
    sys.path.insert(0, path)
    module = importlib.import_module(filename, path)
    importlib.reload(module)  # Might be out of date
    del sys.path[0]
    return module

settings = {}
try:
    userSettings = import_path(os.path.join('.', 'bitexen_client_settings'))
    settings.update(vars(userSettings))
except ImportError:
    #ToDo: add loggings
    pass

settings = dotdict(settings)
