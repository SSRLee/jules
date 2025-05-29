"""
Example 01: Find an Image on Screen

This script demonstrates how to use the `find` function from the `pysikulix`
library to locate a specific image on the screen.
"""

import logging
import os
# Assuming pysikulix is installed or available in the Python path.
# If running from the py_sikuli_like/examples directory, and pysikulix is in the parent:
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pysikulix import find, logger as pysikulix_logger

# --- Configuration ---
# 1. Configure basic logging to see output from this script and pysikulix
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
# You can set the pysikulix logger level specifically if needed
# pysikulix_logger.setLevel(logging.DEBUG) # For more detailed output from the library

# 2. Define the path to the image to be found
# This assumes the script is run from the 'examples' directory.
IMAGE_TO_FIND = "images/red_square.png"

# --- Main Script ---
def main():
    pysikulix_logger.info("Starting ex01_find_image.py: Attempting to find an image.")

    # Important Note for Users:
    # For this script to successfully find the image, 'red_square.png'
    # (or whatever image you are searching for) MUST be visible on your screen.
    # Open 'examples/images/red_square.png' in an image viewer before running,
    # or ensure it's otherwise displayed.
    pysikulix_logger.info(f"Please ensure the image '{IMAGE_TO_FIND}' is visible on your screen.")
    pysikulix_logger.info("Pausing for 5 seconds to give you time to display the image...")
    try:
        # In a real scenario, you might use PyAutoGUI's sleep, but time.sleep is fine here.
        import time
        time.sleep(5)
    except ImportError:
        pysikulix_logger.warning("time module not found, continuing without pause.")


    pysikulix_logger.info(f"Attempting to find '{IMAGE_TO_FIND}' on the screen...")
    
    try:
        location = find(IMAGE_TO_FIND, confidence_threshold=0.7) # Adjust confidence as needed

        if location:
            pysikulix_logger.info(f"Image '{IMAGE_TO_FIND}' FOUND at coordinates: {location}")
            pysikulix_logger.info(f"(x={location[0]}, y={location[1]}, width={location[2]}, height={location[3]})")
        else:
            pysikulix_logger.warning(f"Image '{IMAGE_TO_FIND}' NOT FOUND on the screen.")
            pysikulix_logger.warning("Troubleshooting tips:")
            pysikulix_logger.warning("1. Is the image fully visible and unobstructed on your screen?")
            pysikulix_logger.warning("2. Is the image identical to the file (no scaling, rotation, color changes)?")
            pysikulix_logger.warning("3. Try adjusting the `confidence_threshold` (lower might find more, but less accurately).")
            pysikulix_logger.warning("4. Check screen resolution and DPI scaling settings if issues persist.")

    except Exception as e:
        pysikulix_logger.error(f"An unexpected error occurred: {e}", exc_info=True)

if __name__ == "__main__":
    # Ensure the image path is correct if running from a different directory
    # This example assumes it's run from `py_sikuli_like/examples`
    if not os.path.exists(IMAGE_TO_FIND):
        pysikulix_logger.error(f"Error: Image file not found at '{os.path.abspath(IMAGE_TO_FIND)}'.")
        pysikulix_logger.error("Please ensure the path is correct and the 'images' directory is accessible.")
        pysikulix_logger.error(f"Current working directory: {os.getcwd()}")
    else:
        main()

    pysikulix_logger.info("ex01_find_image.py finished.")
    print("\n--- Script ex01_find_image.py finished ---")
    print("Check the console output above for logs from pysikulix.")
    print(f"Remember to have '{IMAGE_TO_FIND}' visible on screen when running.")
