"""
Custom exceptions for PySikuliX.
"""

class ImageNotFoundError(Exception):
    """Custom exception raised when an image cannot be found on screen."""
    def __init__(self, message="Image not found on screen."):
        self.message = message
        super().__init__(self.message)

class TargetInvalidError(Exception):
    """Custom exception raised when a target for an action is invalid."""
    def __init__(self, message="Target for action is invalid. Must be image path or coordinates."):
        self.message = message
        super().__init__(self.message)
