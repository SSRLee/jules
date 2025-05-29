import cv2
import numpy as np
from PIL import Image
import logging

logger = logging.getLogger(__name__)

def find_image_on_screen(template_image_path, main_image_path_or_pil_image, confidence_threshold=0.8):
    """
    Finds a template image within a larger image (screenshot).

    Args:
        template_image_path (str): Path to the template image file.
        main_image_path_or_pil_image (str or PIL.Image.Image): Path to the main image file or a PIL Image object.
        confidence_threshold (float): Minimum confidence score (0.0 to 1.0) to consider a match.

    Returns:
        tuple: (x, y, width, height) of the found template in the main image, or None if not found.
    """
    try:
        template_img = cv2.imread(template_image_path)
        if template_img is None:
            raise FileNotFoundError(f"Template image not found or could not be read: {template_image_path}")
        template_h, template_w = template_img.shape[:2]

        if isinstance(main_image_path_or_pil_image, str):
            main_img = cv2.imread(main_image_path_or_pil_image)
            if main_img is None:
                raise FileNotFoundError(f"Main image not found or could not be read: {main_image_path_or_pil_image}")
        elif isinstance(main_image_path_or_pil_image, Image.Image):
            # Convert PIL Image to OpenCV format
            main_img = np.array(main_image_path_or_pil_image.convert('RGB'))
            main_img = cv2.cvtColor(main_img, cv2.COLOR_RGB2BGR)
        else:
            raise ValueError("main_image_path_or_pil_image must be a file path (str) or a PIL Image object.")

        if main_img.shape[0] < template_h or main_img.shape[1] < template_w:
            logger.debug(f"Main image dimensions ({main_img.shape[1]}w, {main_img.shape[0]}h) are smaller than template dimensions ({template_w}w, {template_h}h). Cannot find match.")
            return None

        # Template matching
        result = cv2.matchTemplate(main_img, template_img, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if max_val >= confidence_threshold:
            # Top-left corner of the matched area
            top_left_x = max_loc[0]
            top_left_y = max_loc[1]
            # Return bounding box: (x, y, width, height)
            logger.debug(f"Template {template_image_path} found with confidence {max_val:.2f} at location {max_loc}. Threshold was {confidence_threshold:.2f}.")
            return (top_left_x, top_left_y, template_w, template_h)
        else:
            logger.debug(f"Template {template_image_path} not found with sufficient confidence. Max confidence: {max_val:.2f}, Threshold: {confidence_threshold:.2f}.")
            return None
    except FileNotFoundError as fnf_error:
        logger.error(f"File not found in find_image_on_screen: {fnf_error}", exc_info=True)
        return None
    except ValueError as val_error:
        logger.error(f"Value error in find_image_on_screen: {val_error}", exc_info=True)
        return None
    except Exception as e:
        logger.error(f"An unexpected error occurred during image recognition for {template_image_path}: {e}", exc_info=True)
        return None

if __name__ == '__main__':
    # This is an example of how to use the function.
    # You'll need to create 'template.png' and 'main_image.png' for this to run.
    
    # Setup basic logging for the example
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger.info("Starting image_recognition.py examples...")

    # Create dummy images for testing if they don't exist.
    try:
        # Attempt to create dummy images for testing if they don't exist
        # This part is for demonstration and might require manual creation of images
        # or using the screen capture module to get actual images.
        
        # Create a dummy main image (e.g., 640x480, black)
        dummy_main_pil = Image.new('RGB', (640, 480), color = 'black')
        dummy_main_pil.save("dummy_main_image.png")
        logger.debug("Created dummy_main_image.png")

        # Create a dummy template image (e.g., 50x50, white)
        dummy_template_pil = Image.new('RGB', (50, 50), color = 'white')
        dummy_template_pil.save("dummy_template.png")
        logger.debug("Created dummy_template.png")
        
        # Example 1: Using image paths (template not in main image yet)
        logger.info("Example 1: Using image paths (template not present initially)")
        location = find_image_on_screen("dummy_template.png", "dummy_main_image.png", 0.7)
        if location:
            logger.info(f"Template found at: x={location[0]}, y={location[1]}, width={location[2]}, height={location[3]}")
        else:
            logger.info("Template not found using image paths (as expected).")

        # To make the template findable, let's draw the template onto the main image
        main_with_template_pil = dummy_main_pil.copy()
        main_with_template_pil.paste(dummy_template_pil, (100, 150)) # Paste at (100, 150)
        main_with_template_pil.save("main_image_with_template.png")
        logger.debug("Created main_image_with_template.png (template pasted at 100,150)")

        logger.info("\nExample 1b: Using image paths (template present)")
        location_present = find_image_on_screen("dummy_template.png", "main_image_with_template.png", 0.7)
        if location_present:
            logger.info(f"Template found at: x={location_present[0]}, y={location_present[1]}, width={location_present[2]}, height={location_present[3]}")
            # Expected: close to (100, 150, 50, 50)
        else:
            logger.warning("Template not found (it should have been!).")


        # Example 2: Using a PIL Image object for the main image
        logger.info("\nExample 2: Using PIL Image for main image (template present)")
        location_pil = find_image_on_screen("dummy_template.png", main_with_template_pil, 0.7)
        if location_pil:
            logger.info(f"Template found using PIL main image at: x={location_pil[0]}, y={location_pil[1]}, width={location_pil[2]}, height={location_pil[3]}")
        else:
            logger.warning("Template not found using PIL main image (it should have been).")

        # Example 3: Template not present (using original dummy_main_image)
        logger.info("\nExample 3: Template not present (high threshold)")
        location_not_present = find_image_on_screen("dummy_template.png", "dummy_main_image.png", 0.95)
        if location_not_present:
            logger.warning(f"Template found at: {location_not_present} (this should not happen if threshold is high or not present)")
        else:
            logger.info("Template not found (as expected with high threshold or if truly not present).")

        # Example 4: File not found
        logger.info("\nExample 4: File not found")
        location_fnf = find_image_on_screen("non_existent_template.png", "dummy_main_image.png")
        if location_fnf:
            logger.warning(f"Template found at: {location_fnf} (should be None due to error)")
        else:
            logger.info("Template not found (due to file not found error, as expected).")

    except ImportError:
        logger.error("Pillow (PIL) is not installed. Please install it to run the __main__ example.")
    except Exception as e:
        logger.error(f"An error occurred in the __main__ example: {e}", exc_info=True)

    # Clean up dummy files (optional - useful for testing)
    import os
    try:
        logger.debug("Cleaning up dummy image files...")
        if os.path.exists("dummy_main_image.png"): os.remove("dummy_main_image.png")
        if os.path.exists("dummy_template.png"): os.remove("dummy_template.png")
        if os.path.exists("main_image_with_template.png"): os.remove("main_image_with_template.png")
        logger.debug("Dummy image files cleaned up.")
    except OSError as e:
        logger.warning(f"Could not remove all dummy files: {e}")
    
    logger.info("image_recognition.py examples finished.")
