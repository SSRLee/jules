"""
Example 03: Type Text at an Image Location

This script demonstrates how to use the `type_text_at` function from 
the `pysikulix` library to find an image, click its center, and then 
type text.
"""

import logging
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pysikulix import type_text_at, ImageNotFoundError, logger as pysikulix_logger

# --- Configuration ---
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
# pysikulix_logger.setLevel(logging.DEBUG) # Uncomment for more detailed library output

IMAGE_TO_TYPE_AT = "images/green_triangle.png"
TEXT_TO_TYPE = "Hello from PySikuliX!"

# --- Main Script ---
def main():
    pysikulix_logger.info("Starting ex03_type_at_image.py: Attempting to find, click, and type at an image.")

    # Important Note for Users:
    # 1. Image Visibility: 'green_triangle.png' MUST be visible on your screen.
    #    Open 'examples/images/green_triangle.png' in an image viewer.
    # 2. Active Window: The script will click the center of the image. Typing will
    #    go to the window that becomes active after the click. For a simple image
    #    opened in a viewer, this might just be the viewer itself, not a text field.
    #    To test typing into a field, you would need an image of an actual text input box.
    pysikulix_logger.info(f"Please ensure the image '{IMAGE_TO_TYPE_AT}' is visible on your screen.")
    pysikulix_logger.info("The script will click it and then type. Ensure the active window after click is safe for typing.")
    pysikulix_logger.info("Pausing for 7 seconds to give you time to prepare...")
    try:
        import time
        time.sleep(7)
    except ImportError:
        pysikulix_logger.warning("time module not found, continuing without pause.")

    pysikulix_logger.info(f"Attempting to find '{IMAGE_TO_TYPE_AT}', click it, and type '{TEXT_TO_TYPE}'...")
    
    try:
        # type_text_at will:
        # 1. Find the image (IMAGE_TO_TYPE_AT).
        # 2. Click its center.
        # 3. Type the text (TEXT_TO_TYPE).
        type_text_at(IMAGE_TO_TYPE_AT, TEXT_TO_TYPE, interval=0.05)
        
        pysikulix_logger.info(f"Successfully found '{IMAGE_TO_TYPE_AT}', clicked it, and typed the text.")
        pysikulix_logger.info("Check the window that was active after the click for the typed text.")

    except ImageNotFoundError:
        pysikulix_logger.warning(f"Image '{IMAGE_TO_TYPE_AT}' NOT FOUND on the screen. Action aborted.")
        pysikulix_logger.warning("Troubleshooting tips (see ex01_find_image.py for more).")
    except Exception as e:
        pysikulix_logger.error(f"An unexpected error occurred: {e}", exc_info=True)

if __name__ == "__main__":
    if not os.path.exists(IMAGE_TO_TYPE_AT):
        pysikulix_logger.error(f"Error: Image file not found at '{os.path.abspath(IMAGE_TO_TYPE_AT)}'.")
        pysikulix_logger.error("Please ensure the path is correct and the 'images' directory is accessible.")
        pysikulix_logger.error(f"Current working directory: {os.getcwd()}")
    else:
        main()

    pysikulix_logger.info("ex03_type_at_image.py finished.")
    print("\n--- Script ex03_type_at_image.py finished ---")
    print("Check the console output above for logs from pysikulix.")
    print(f"Remember to have '{IMAGE_TO_TYPE_AT}' visible and consider where the text will be typed.")
