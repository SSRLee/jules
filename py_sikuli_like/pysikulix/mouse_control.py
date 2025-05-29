import pyautogui
import logging

logger = logging.getLogger(__name__)

# Note: PyAutoGUI's coordinate system starts from the top-left corner of the primary screen (0,0).

def move_to(x, y, duration=0.25):
    """
    Moves the mouse cursor to the specified x, y coordinates.

    Args:
        x (int): The x-coordinate on the screen.
        y (int): The y-coordinate on the screen.
        duration (float): Time in seconds to spend moving the mouse.
    """
    logger.debug(f"Moving mouse to ({x}, {y}) over {duration}s.")
    try:
        pyautogui.moveTo(x, y, duration=duration)
    except Exception as e:
        logger.error(f"Error moving mouse to ({x}, {y}): {e}", exc_info=True)
        # Depending on desired strictness, could re-raise or raise a custom exception.

def click(x=None, y=None, button='left', duration=0.25):
    """
    Performs a mouse click.

    If x and y are provided, moves to that position first.
    Otherwise, clicks at the current mouse position.

    Args:
        x (int, optional): The x-coordinate to move to before clicking.
        y (int, optional): The y-coordinate to move to before clicking.
        button (str): Mouse button to click ('left', 'middle', 'right'). Defaults to 'left'.
        duration (float): Time in seconds to spend moving the mouse, if x and y are specified.
    """
    action_log = f"{button}-click"
    target_log = f"at ({x}, {y})" if x is not None and y is not None else "at current position"
    logger.debug(f"Performing {action_log} {target_log} with move duration {duration if x is not None else 'N/A'}s.")

    try:
        if x is not None and y is not None:
            pyautogui.click(x, y, button=button, duration=duration)
        else:
            pyautogui.click(button=button)
    except Exception as e:
        logger.error(f"Error performing {action_log} {target_log}: {e}", exc_info=True)

def double_click(x=None, y=None, button='left', duration=0.25):
    """
    Performs a double click.

    If x and y are provided, moves to that position first.
    Otherwise, double clicks at the current mouse position.

    Args:
        x (int, optional): The x-coordinate to move to before double clicking.
        y (int, optional): The y-coordinate to move to before double clicking.
        button (str): Mouse button to double click ('left', 'middle', 'right'). Defaults to 'left'.
        duration (float): Time in seconds to spend moving the mouse, if x and y are specified.
    """
    action_log = f"double-{button}-click"
    target_log = f"at ({x}, {y})" if x is not None and y is not None else "at current position"
    logger.debug(f"Performing {action_log} {target_log} with move duration {duration if x is not None else 'N/A'}s.")

    try:
        if x is not None and y is not None:
            # PyAutoGUI's doubleClick function doesn't take duration for move, so move first.
            # Consider logging this move_to call if it's separate and significant.
            pyautogui.moveTo(x, y, duration=duration) 
            pyautogui.doubleClick(button=button)
        else:
            pyautogui.doubleClick(button=button)
    except Exception as e:
        logger.error(f"Error performing {action_log} {target_log}: {e}", exc_info=True)

def right_click(x=None, y=None, duration=0.25):
    """
    Performs a right mouse click.

    If x and y are provided, moves to that position first.
    Otherwise, right clicks at the current mouse position.

    Args:
        x (int, optional): The x-coordinate to move to before clicking.
        y (int, optional): The y-coordinate to move to before clicking.
        duration (float): Time in seconds to spend moving the mouse, if x and y are specified.
    """
    # This function essentially calls `click` with button='right'.
    # The `click` function already has logging.
    # We can add a specific log here for the intent of right_click if desired,
    # or rely on the logging within the called `click` function.
    logger.debug(f"Attempting right-click (delegating to click function). Target: {('('+str(x)+','+str(y)+')') if x is not None else 'current pos'}, duration: {duration}s")
    try:
        click(x, y, button='right', duration=duration)
    except Exception as e:
        # This is defensive; click() should handle its own errors.
        # If click() re-raises, this would catch it.
        logger.error(f"Error during right_click (after delegation to click): {e}", exc_info=True)


if __name__ == '__main__':
    # Example Usage (Use with caution, as this will move your mouse)
    # Setup basic logging for the example
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger.info("Starting mouse_control.py examples in 3 seconds...")
    pyautogui.sleep(3)

    # Get current screen size
    screen_width, screen_height = pyautogui.size()
    logger.info(f"Screen size: {screen_width}x{screen_height}")

    # Example 1: Move mouse to center of the screen
    center_x, center_y = screen_width // 2, screen_height // 2
    logger.info(f"Moving mouse to center: ({center_x}, {center_y})")
    move_to(center_x, center_y, duration=1)
    pyautogui.sleep(1)

    # Example 2: Perform a left click at (100, 100)
    logger.info("Left clicking at (100, 100)")
    click(100, 100, button='left', duration=0.5)
    pyautogui.sleep(1)

    # Example 3: Perform a right click at current position
    # First, move somewhere else to see the right click happen there
    logger.info(f"Moving mouse to ({center_x + 100}, {center_y}) before right click example.")
    move_to(center_x + 100, center_y, duration=0.5)
    current_pos = pyautogui.position()
    logger.info(f"Right clicking at current position: {current_pos}")
    right_click() # No x, y means current position
    pyautogui.sleep(1)

    # Example 4: Perform a double click at (200, 200)
    logger.info("Double clicking at (200, 200)")
    double_click(200, 200, button='left', duration=0.5)
    pyautogui.sleep(1)
    
    # Example 5: Move mouse back to a corner (e.g., top-left)
    logger.info("Moving mouse to (10, 10)")
    move_to(10, 10, duration=1)

    logger.info("Mouse control examples finished.")
    logger.info("NOTE: If your mouse is now in an unexpected location, that's due to the script execution.")
    logger.info("PyAutoGUI has a failsafe: quickly move your mouse to any corner of the screen to raise pyautogui.FailSafeException and stop the script.")
