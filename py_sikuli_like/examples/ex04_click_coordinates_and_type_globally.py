"""
Example 04: Click Coordinates and Type Globally

This script demonstrates how to use `click` with specific coordinates
and then use `type_text_globally` from the `pysikulix` library.
"""

import logging
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pysikulix import click, type_text_globally, logger as pysikulix_logger

# --- Configuration ---
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
# pysikulix_logger.setLevel(logging.DEBUG) # Uncomment for more detailed library output

# Define arbitrary coordinates to click
# WARNING: These are absolute screen coordinates.
# Clicking here might interact with any window or desktop element at this position.
# Choose coordinates that are safe on your system, e.g., an empty area of your desktop.
CLICK_X, CLICK_Y = 100, 100
TEXT_TO_TYPE = "Global typing test from PySikuliX!"

# --- Main Script ---
def main():
    pysikulix_logger.info("Starting ex04_click_coordinates_and_type_globally.py")

    pysikulix_logger.warning(f"This script will attempt to click at screen coordinates ({CLICK_X}, {CLICK_Y}).")
    pysikulix_logger.warning("Ensure these coordinates are safe and will not cause unintended actions on your system.")
    pysikulix_logger.warning("After clicking, it will type globally, affecting the focused window.")
    pysikulix_logger.info("Pausing for 5 seconds to give you time to prepare or stop the script (Ctrl+C)...")
    try:
        import time
        time.sleep(5)
    except ImportError:
        pysikulix_logger.warning("time module not found, continuing without pause.")

    try:
        # 1. Click at specified coordinates
        pysikulix_logger.info(f"Attempting to click at coordinates: ({CLICK_X}, {CLICK_Y}).")
        click((CLICK_X, CLICK_Y)) # Pass coordinates as a tuple
        pysikulix_logger.info(f"Successfully clicked at ({CLICK_X}, {CLICK_Y}).")
        
        # Give a moment for focus to change if any window was brought forward by the click
        pysikulix_logger.info("Pausing for 1 second before typing...")
        time.sleep(1)


        # 2. Type text globally (to wherever the focus is now)
        pysikulix_logger.info(f"Attempting to type globally: '{TEXT_TO_TYPE}'")
        type_text_globally(TEXT_TO_TYPE, interval=0.05)
        pysikulix_logger.info("Successfully typed text globally.")
        pysikulix_logger.info("Check the window that gained focus after the click, or your active window.")

    except Exception as e:
        pysikulix_logger.error(f"An unexpected error occurred: {e}", exc_info=True)

if __name__ == "__main__":
    main()
    pysikulix_logger.info("ex04_click_coordinates_and_type_globally.py finished.")
    print("\n--- Script ex04_click_coordinates_and_type_globally.py finished ---")
    print("Check the console output above for logs from pysikulix.")
    print(f"Remember the warning about clicking arbitrary coordinates ({CLICK_X},{CLICK_Y}).")
