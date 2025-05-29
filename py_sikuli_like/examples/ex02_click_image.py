"""
Example 02: Click an Image on Screen

This script demonstrates how to use the `click` function from the `pysikulix`
library to find and then click on a specific image on the screen.
"""

import logging
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pysikulix import click, ImageNotFoundError, logger as pysikulix_logger

# --- Configuration ---
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
# pysikulix_logger.setLevel(logging.DEBUG) # Uncomment for more detailed library output

IMAGE_TO_CLICK = "images/blue_circle.png"

# --- Main Script ---
def main():
    pysikulix_logger.info("Starting ex02_click_image.py: Attempting to find and click an image.")

    # Important Note for Users:
    # For this script to successfully find and click the image, 'blue_circle.png'
    # MUST be visible on your screen.
    # Open 'examples/images/blue_circle.png' in an image viewer before running.
    pysikulix_logger.info(f"Please ensure the image '{IMAGE_TO_CLICK}' is visible on your screen.")
    pysikulix_logger.info("Pausing for 5 seconds to give you time to display the image...")
    try:
        import time
        time.sleep(5)
    except ImportError:
        pysikulix_logger.warning("time module not found, continuing without pause.")

    pysikulix_logger.info(f"Attempting to find and click '{IMAGE_TO_CLICK}' on the screen...")
    
    try:
        # The click function will internally try to find the image first.
        # It uses a default confidence, but you might need to adjust it in a real scenario
        # by using find() explicitly first if click() doesn't expose confidence.
        # For now, click() uses the default confidence of find().
        click(IMAGE_TO_CLICK)
        pysikulix_logger.info(f"Successfully found and clicked on '{IMAGE_TO_CLICK}'.")
        pysikulix_logger.info("Check if your mouse cursor moved to the image and performed a click.")

    except ImageNotFoundError:
        pysikulix_logger.warning(f"Image '{IMAGE_TO_CLICK}' NOT FOUND on the screen. Click action aborted.")
        pysikulix_logger.warning("Troubleshooting tips:")
        pysikulix_logger.warning("1. Is the image fully visible and unobstructed on your screen?")
        pysikulix_logger.warning("2. Is the image identical to the file (no scaling, rotation, color changes)?")
        pysikulix_logger.warning("3. Check screen resolution and DPI scaling settings if issues persist.")
    except Exception as e:
        pysikulix_logger.error(f"An unexpected error occurred: {e}", exc_info=True)

if __name__ == "__main__":
    if not os.path.exists(IMAGE_TO_CLICK):
        pysikulix_logger.error(f"Error: Image file not found at '{os.path.abspath(IMAGE_TO_CLICK)}'.")
        pysikulix_logger.error("Please ensure the path is correct and the 'images' directory is accessible.")
        pysikulix_logger.error(f"Current working directory: {os.getcwd()}")
    else:
        main()

    pysikulix_logger.info("ex02_click_image.py finished.")
    print("\n--- Script ex02_click_image.py finished ---")
    print("Check the console output above for logs from pysikulix.")
    print(f"Remember to have '{IMAGE_TO_CLICK}' visible on screen when running.")
