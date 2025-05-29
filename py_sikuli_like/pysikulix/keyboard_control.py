import pyautogui
import logging

logger = logging.getLogger(__name__)

# PyAutoGUI's functions for keyboard control are used here.
# Reminder: PyAutoGUI has a failsafe mechanism. If you lose control,
# quickly move your mouse to any corner of the screen to raise
# pyautogui.FailSafeException and stop the script.

def type_text(text, interval=0.0):
    """
    Types the given text string.

    Args:
        text (str): The string to type.
        interval (float): The time in seconds to wait between each key press.
                          Defaults to 0.0 (fast typing).
    """
    # For security, avoid logging the actual 'text' content at INFO level.
    # Log at DEBUG if absolutely necessary, or log a masked version.
    logger.debug(f"Typing text (length: {len(text)}) with interval {interval}s.")
    try:
        pyautogui.typewrite(text, interval=interval)
    except Exception as e:
        logger.error(f"Error typing text: {e}", exc_info=True)

def press_key(key_name):
    """
    Presses a single key.

    Args:
        key_name (str): The name of the key to press (e.g., 'enter', 'ctrl', 'f1', 'a').
                        Refer to PyAutoGUI documentation for all valid key names.
    """
    logger.debug(f"Pressing key: '{key_name}'.")
    try:
        pyautogui.press(key_name)
    except Exception as e:
        logger.error(f"Error pressing key '{key_name}': {e}", exc_info=True)

def hotkey(*args):
    """
    Presses a combination of keys simultaneously (e.g., for shortcuts like Ctrl+C).

    Args:
        *args: A sequence of key names to press down together (e.g., 'ctrl', 'shift', 'esc').
               The keys are pressed in the given order and released in reverse order.
    """
    keys_str = ", ".join(args)
    logger.debug(f"Pressing hotkey combination: '{keys_str}'.")
    try:
        if not args:
            logger.warning("hotkey() called with no keys.")
            return
        pyautogui.hotkey(*args)
    except Exception as e:
        logger.error(f"Error pressing hotkey '{keys_str}': {e}", exc_info=True)

if __name__ == '__main__':
    # Example Usage (Use with caution, as this will interact with your active window)
    # Setup basic logging for the example
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger.info("Starting keyboard_control.py examples in 3 seconds...")
    logger.info("Please focus a text editor or a safe input field to see the typing.")
    pyautogui.sleep(3)

    # Example 1: Type some text
    logger.info("Typing: 'Hello, PySikuliX!'")
    type_text("Hello, PySikuliX!", interval=0.05)
    pyautogui.sleep(1)

    # Example 2: Press the 'enter' key
    logger.info("Pressing 'enter' key.")
    press_key('enter')
    pyautogui.sleep(1)

    # Example 3: Type more text
    logger.info("Typing: 'This is a new line.'")
    type_text("This is a new line.", interval=0.05)
    pyautogui.sleep(1)

    # Example 4: Demonstrate a hotkey (e.g., Ctrl+A to select all)
    logger.info("Attempting hotkey: 'ctrl' + 'a' (select all). Ensure a text editor is active.")
    # type_text("Some text to select. ") # Type something to be selected
    # press_key('enter')
    hotkey('ctrl', 'a')
    pyautogui.sleep(1)

    # Example 5: Demonstrate another hotkey (e.g., Ctrl+C to copy)
    logger.info("Attempting hotkey: 'ctrl' + 'c' (copy). Assumes text was selected.")
    # hotkey('ctrl', 'c')
    # pyautogui.sleep(1)
    # logger.info("If text was selected, it should now be in your clipboard.")
    # press_key('pagedown') # Move away, so we don't overwrite

    # Example 6: Press a function key (e.g., 'f1' - often opens help)
    # logger.info("Pressing 'f1' key (might open a help window).")
    # press_key('f1')
    # pyautogui.sleep(2) # Give time for potential help window

    logger.info("Keyboard control examples finished.")
    logger.info("NOTE: If your keyboard is typing unexpectedly or focus is lost, that's due to script execution.")
    logger.info("Remember PyAutoGUI's failsafe: quickly move your mouse to any screen corner.")
