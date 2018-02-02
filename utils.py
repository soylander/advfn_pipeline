import os
import errno
from settings import DATA_PATH

def make_directory(full_path):
    if not os.path.exists(os.path.dirname(full_path)):
        try:
            os.makedirs(os.path.dirname(full_path))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise