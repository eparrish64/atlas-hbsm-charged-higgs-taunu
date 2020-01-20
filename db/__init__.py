import logging
import os

from .decorators import cached_property

log = logging.getLogger('db')
if not os.environ.get("DEBUG", False):
    log.setLevel(logging.INFO)

if hasattr(logging, 'captureWarnings'):
    logging.captureWarnings(True)
