
from api.config import PACKAGE_ROOT
import os


with open(os.path.join(PACKAGE_ROOT, 'VERSION'), 'rb') as _version_file:
    __version__ =_version_file.read().strip()
    