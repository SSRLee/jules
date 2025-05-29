"""
Core API for PySikuliX, providing a simplified interface to screen interaction.
"""
from . import logger # Import the configured logger

from .screen_capture import capture_screen
from .image_recognition import find_image_on_screen
from .mouse_control import click as mc_click, double_click as mc_double_click, right_click as mc_right_click
from .keyboard_control import type_text as kc_type_text, hotkey as kc_hotkey, press_key as kc_press_key
from .exceptions import ImageNotFoundError, TargetInvalidError

def _get_center(bbox):
    """
    Calculates the center of a bounding box.

    Args:
        bbox (tuple): (x, y, width, height).

    Returns:
        tuple: (center_x, center_y).
    """
    if not bbox or len(bbox) != 4:
        return None # Should not happen if bbox is validated before calling
    return bbox[0] + bbox[2] // 2, bbox[1] + bbox[3] // 2

def find(template_image_path, confidence_threshold=0.8):
    """
    Finds a template image on the current screen.

    Args:
        template_image_path (str): Path to the template image file.
        confidence_threshold (float): Minimum confidence score (0.0 to 1.0)
                                      to consider a match. Defaults to 0.8.

    Returns:
        tuple: (x, y, width, height) of the found template, or None if not found.
    """
    screen_image = capture_screen()
    logger.info(f"Attempting to find image: {template_image_path} with confidence {confidence_threshold}")
    screen_image = capture_screen()
    if not screen_image:
        logger.error("Screen capture failed, cannot proceed with find.")
        return None
    
    bbox = find_image_on_screen(template_image_path, screen_image, confidence_threshold)
    if bbox:
        logger.info(f"Image found: {template_image_path} at {bbox}")
    else:
        logger.warning(f"Image not found: {template_image_path}")
    return bbox

def click(target, button='left', duration=0.25):
    """
    Clicks on a target, which can be an image path or coordinates.

    Args:
        target (str or tuple): Path to an image file or (x, y) coordinates.
        button (str): Mouse button ('left', 'middle', 'right'). Defaults to 'left'.
        duration (float): Time in seconds for mouse movement. Defaults to 0.25.

    Raises:
        ImageNotFoundError: If the target is an image path and the image is not found.
        TargetInvalidError: If the target type is not supported.
    """
    target_info = f"image '{target}'" if isinstance(target, str) else f"coordinates {target}"
    logger.info(f"Attempting to {button}-click on {target_info} with duration {duration}s.")

    if isinstance(target, str):  # Image path
        bbox = find(target) # find() already logs its attempt and result
        if bbox:
            center_x, center_y = _get_center(bbox)
            logger.info(f"Performing {button}-click on found image '{target}' at center ({center_x}, {center_y}).")
            mc_click(center_x, center_y, button=button, duration=duration)
        else:
            logger.error(f"Image target not found for click: {target}")
            raise ImageNotFoundError(f"Image target not found: {target}")
    elif isinstance(target, (tuple, list)) and len(target) == 2:  # Coordinates
        logger.info(f"Performing {button}-click on coordinates ({target[0]}, {target[1]}).")
        mc_click(target[0], target[1], button=button, duration=duration)
    else:
        logger.error(f"Invalid target type for click: {target}. Type: {type(target)}")
        raise TargetInvalidError("Click target must be an image path (str) or (x,y) coordinates.")

def double_click(target, button='left', duration=0.25):
    """
    Double-clicks on a target, which can be an image path or coordinates.

    Args:
        target (str or tuple): Path to an image file or (x, y) coordinates.
        button (str): Mouse button ('left', 'middle', 'right'). Defaults to 'left'.
        duration (float): Time in seconds for mouse movement. Defaults to 0.25.

    Raises:
        ImageNotFoundError: If the target is an image path and the image is not found.
        TargetInvalidError: If the target type is not supported.
    """
    target_info = f"image '{target}'" if isinstance(target, str) else f"coordinates {target}"
    logger.info(f"Attempting to double-{button}-click on {target_info} with duration {duration}s.")

    if isinstance(target, str):  # Image path
        bbox = find(target) # find() already logs its attempt and result
        if bbox:
            center_x, center_y = _get_center(bbox)
            logger.info(f"Performing double-{button}-click on found image '{target}' at center ({center_x}, {center_y}).")
            mc_double_click(center_x, center_y, button=button, duration=duration)
        else:
            logger.error(f"Image target not found for double_click: {target}")
            raise ImageNotFoundError(f"Image target not found for double_click: {target}")
    elif isinstance(target, (tuple, list)) and len(target) == 2:  # Coordinates
        logger.info(f"Performing double-{button}-click on coordinates ({target[0]}, {target[1]}).")
        mc_double_click(target[0], target[1], button=button, duration=duration)
    else:
        logger.error(f"Invalid target type for double_click: {target}. Type: {type(target)}")
        raise TargetInvalidError("Double_click target must be an image path (str) or (x,y) coordinates.")

def right_click(target, duration=0.25):
    """
    Right-clicks on a target, which can be an image path or coordinates.

    Args:
        target (str or tuple): Path to an image file or (x, y) coordinates.
        duration (float): Time in seconds for mouse movement. Defaults to 0.25.

    Raises:
        ImageNotFoundError: If the target is an image path and the image is not found.
        TargetInvalidError: If the target type is not supported.
    """
    target_info = f"image '{target}'" if isinstance(target, str) else f"coordinates {target}"
    logger.info(f"Attempting to right-click on {target_info} with duration {duration}s.")

    if isinstance(target, str):  # Image path
        bbox = find(target) # find() already logs its attempt and result
        if bbox:
            center_x, center_y = _get_center(bbox)
            logger.info(f"Performing right-click on found image '{target}' at center ({center_x}, {center_y}).")
            mc_right_click(center_x, center_y, duration=duration)
        else:
            logger.error(f"Image target not found for right_click: {target}")
            raise ImageNotFoundError(f"Image target not found for right_click: {target}")
    elif isinstance(target, (tuple, list)) and len(target) == 2:  # Coordinates
        logger.info(f"Performing right-click on coordinates ({target[0]}, {target[1]}).")
        mc_right_click(target[0], target[1], duration=duration)
    else:
        logger.error(f"Invalid target type for right_click: {target}. Type: {type(target)}")
        raise TargetInvalidError("Right_click target must be an image path (str) or (x,y) coordinates.")

def type_text_at(target, text_to_type, interval=0.0, clear_first=False):
    """
    Clicks on a target and then types text.

    Args:
        target (str or tuple): Path to an image file or (x, y) coordinates to click.
        text_to_type (str): The string to type.
        interval (float): Interval between key presses. Defaults to 0.0.
        clear_first (bool): If True, attempts to select all (Ctrl+A) and delete
                            existing text before typing. Defaults to False.

    Raises:
        ImageNotFoundError: If the target is an image path and the image is not found.
        TargetInvalidError: If the target type is not supported.
    """
    target_info = f"image '{target}'" if isinstance(target, str) else f"coordinates {target}"
    logger.info(f"Attempting to type text at {target_info}. Clear first: {clear_first}.")
    # click() call below will log its own details, including image search if target is image path.
    
    # Click on the target first
    try:
        click(target, button='left', duration=0.1) # Use a shorter duration for quicker action
    except (ImageNotFoundError, TargetInvalidError) as e:
        logger.error(f"Failed to click target before typing: {e}") # Log and re-raise
        raise

    if clear_first:
        logger.info("Clearing field: pressing Ctrl+A, then Delete.")
        kc_hotkey('ctrl', 'a') 
        kc_press_key('delete') # or 'backspace'
        # Consider a small sleep if issues arise, e.g., pyautogui.sleep(0.05)

    logger.debug(f"Typing text (first 20 chars): '{text_to_type[:20]}...' with interval {interval}s.")
    kc_type_text(text_to_type, interval=interval)

def type_text_globally(text_to_type, interval=0.0):
    """
    Types text at the current cursor focus without clicking a target.

    Args:
        text_to_type (str): The string to type.
        interval (float): Interval between key presses. Defaults to 0.0.
    """
    logger.info("Attempting to type text globally (at current cursor focus).")
    logger.debug(f"Typing text (first 20 chars): '{text_to_type[:20]}...' with interval {interval}s.")
    kc_type_text(text_to_type, interval=interval)

if __name__ == '__main__':
    # This __main__ block is for basic conceptual testing.
    # Actual execution requires:
    #   1. A display server (e.g., X11 on Linux) for screen capture and GUI interactions.
    #   2. Dummy image files ('./dummy_template.png') for image-based functions.
    #   3. Careful execution, as it will interact with your screen and keyboard.
    
    print("PySikuliX API Module - Conceptual Tests")
    print("-----------------------------------------")
    print("Ensure you have a display server and understand these tests will interact with your GUI.")
    print("Create a 'dummy_template.png' for image tests to run without ImageNotFoundError.")
    print("Sleeping for 3 seconds before starting...")
    # import time
    # time.sleep(3)

    # --- Test `find` ---
    # To test find, you'd need 'dummy_template.png' to be visible on screen.
    print("\nTesting find()... (requires 'dummy_template.png' to be on screen)")
    # try:
    #     # Create a dummy template for testing locally if not present
    #     from PIL import Image
    #     try:
    #         img = Image.open("dummy_template.png")
    #     except FileNotFoundError:
    #         print("Creating dummy_template.png for testing find().")
    #         dummy_img = Image.new('RGB', (60, 30), color = 'red')
    #         dummy_img_text = Image.new('RGB', (50,20), color='blue')
    #         dummy_img.paste(dummy_img_text, (5,5))
    #         dummy_img.save("dummy_template.png")
    #         print("Please make 'dummy_template.png' visible on your screen now for the test.")
    #         time.sleep(5) # Give time to position it

    #     bbox = find("dummy_template.png", confidence_threshold=0.7)
    #     if bbox:
    #         print(f"find(): Found 'dummy_template.png' at {bbox}")
    #         center = _get_center(bbox)
    #         print(f"find(): Center of 'dummy_template.png' is {center}")
    #     else:
    #         print("find(): 'dummy_template.png' not found on screen.")
    # except Exception as e:
    #     print(f"Error during find() test: {e}")


    # --- Test `click` (coordinates) ---
    # print("\nTesting click() with coordinates (e.g., 10, 10)...")
    # print("CAUTION: This will click at (10,10). Ensure no critical window is there.")
    # time.sleep(2)
    # try:
    #     click((10, 10))
    #     print("click((10,10)): Executed. Check if mouse moved and clicked near top-left.")
    # except Exception as e:
    #     print(f"Error during click((10,10)) test: {e}")
    # time.sleep(1)

    # --- Test `click` (image) ---
    # print("\nTesting click() with an image... (requires 'dummy_template.png' on screen)")
    # print("CAUTION: This will click the center of 'dummy_template.png' if found.")
    # time.sleep(2)
    # try:
    #     click("dummy_template.png") # Assumes dummy_template.png is findable
    #     print("click('dummy_template.png'): Executed if image was found.")
    # except ImageNotFoundError:
    #     print("click('dummy_template.png'): ImageNotFoundError as expected if not visible.")
    # except Exception as e:
    #     print(f"Error during click('dummy_template.png') test: {e}")
    # time.sleep(1)

    # --- Test `type_text_globally` ---
    # print("\nTesting type_text_globally()...")
    # print("CAUTION: This will type where your cursor is focused in 2s. Focus a text editor!")
    # time.sleep(2)
    # try:
    #     type_text_globally("Hello from PySikuliX! ", interval=0.05)
    #     print("type_text_globally(): Executed. Check your active text input.")
    # except Exception as e:
    #     print(f"Error during type_text_globally() test: {e}")
    # time.sleep(1)

    # --- Test `type_text_at` (coordinates) ---
    # print("\nTesting type_text_at() with coordinates (e.g., 100, 100)...")
    # print("CAUTION: This will click at (100,100) and type. Focus a text editor AT (100,100) or ensure it's safe.")
    # time.sleep(3)
    # try:
    #     # You might need to open a text editor and position its window
    #     # such that (100,100) is a clickable input area.
    #     type_text_at((100, 100), "Typed at (100,100).", clear_first=True)
    #     print("type_text_at((100,100), ...): Executed.")
    # except Exception as e:
    #     print(f"Error during type_text_at((100,100)) test: {e}")

    # --- Test `type_text_at` (image) ---
    # print("\nTesting type_text_at() with an image... (requires 'dummy_template.png' on screen)")
    # print("CAUTION: This will click the image and type. Ensure it's an input field or safe.")
    # time.sleep(3)
    # try:
    #     # For this to be meaningful, dummy_template.png should be an image of a text input field.
    #     type_text_at("dummy_template.png", " Typed into image target.", clear_first=True)
    #     print("type_text_at('dummy_template.png', ...): Executed if image found.")
    # except ImageNotFoundError:
    #     print("type_text_at('dummy_template.png', ...): ImageNotFoundError as expected if not visible.")
    # except Exception as e:
    #     print(f"Error during type_text_at('dummy_template.png') test: {e}")

    print("\nConceptual tests finished. Uncomment sections in api.py's __main__ to run them.")
    print("Remember to manage dummy images and potential GUI interactions carefully.")
