"""
PySikuliX: A Python library for GUI automation based on SikuliX's concepts.
"""

import logging

# 1. Configure a basic logger for the pysikulix library
logger = logging.getLogger(__name__) # __name__ will be 'pysikulix'

# 2. Set a default logging level (e.g., logging.INFO)
# Users can override this by configuring the 'pysikulix' logger themselves.
logger.setLevel(logging.INFO)

# 3. Add a basic console handler (StreamHandler) with a simple formatter by default
# This ensures users see log messages without needing to configure logging for basic usage.
# Check if handlers are already configured for this logger to avoid duplicate handlers
# if the user/another part of the application configures logging.
if not logger.hasHandlers():
    _handler = logging.StreamHandler()
    _formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    _handler.setFormatter(_formatter)
    logger.addHandler(_handler)
    # Prevent propagation to the root logger if we are adding our own default handler,
    # to avoid duplicate messages if the root logger also has a handler.
    # However, if the user *wants* propagation, they can configure it.
    # For a library, it's often better to let the application control propagation.
    # If we set this to True, messages will only go to this logger's handlers.
    # If False (default), they also go to ancestor handlers (e.g. root).
    # Let's keep it False for now, as it's more standard for libraries to allow propagation.
    # logger.propagate = False 
else:
    # If handlers are already present, we assume the user has configured logging.
    logger.info("Logger 'pysikulix' already has handlers configured.")


from .api import (
    find,
    click,
    double_click,
    right_click,
    type_text_at,
    type_text_globally
)
from .exceptions import ImageNotFoundError, TargetInvalidError

__all__ = [
    'find',
    'click',
    'double_click',
    'right_click',
    'type_text_at',
    'type_text_globally',
    'ImageNotFoundError',
    'TargetInvalidError',
    'logger' # Expose the logger for users if they want to manipulate it directly
]

__version__ = "0.1.1" # Incremented version for logging enhancement
