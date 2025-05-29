import mss
from PIL import Image
import logging

logger = logging.getLogger(__name__)

def capture_screen(output_path=None):
    """
    Captures the entire screen.

    Args:
        output_path (str, optional): File path to save the capture. Defaults to None.

    Returns:
        PIL.Image: Image object of the captured screen.
    """
    try:
        with mss.mss() as sct:
            monitor = sct.monitors[1]  # Capture the primary monitor
            sct_img = sct.grab(monitor)
            img = Image.frombytes("RGB", (sct_img.width, sct_img.height), sct_img.rgb, "raw", "RGB")
            if output_path:
                img.save(output_path)
                logger.info(f"Screen captured and saved to {output_path}")
            else:
                logger.info("Screen captured to PIL Image object.")
            return img
    except Exception as e:
        logger.error(f"Error capturing screen: {e}", exc_info=True)
        return None

def capture_region(bbox, output_path=None):
    """
    Captures a specific region of the screen.

    Args:
        bbox (tuple): (x, y, width, height) defining the region to capture.
        output_path (str, optional): File path to save the capture. Defaults to None.

    Returns:
        PIL.Image: Image object of the captured region.
    """
    try:
        with mss.mss() as sct:
            monitor = {"top": bbox[1], "left": bbox[0], "width": bbox[2], "height": bbox[3]}
            sct_img = sct.grab(monitor)
            img = Image.frombytes("RGB", (sct_img.width, sct_img.height), sct_img.rgb, "raw", "RGB")
            if output_path:
                img.save(output_path)
                logger.info(f"Region {bbox} captured and saved to {output_path}")
            else:
                logger.info(f"Region {bbox} captured to PIL Image object.")
            return img
    except Exception as e:
        logger.error(f"Error capturing region {bbox}: {e}", exc_info=True)
        return None

if __name__ == '__main__':
    # Example usage (optional, for testing)
    # Setup basic logging for the example
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    logger.info("Starting screen_capture.py examples...")

    # Capture entire screen and save
    screen_image = capture_screen("fullscreen_capture.png")
    if screen_image:
        logger.info("Fullscreen capture example successful (image saved or returned).")
    else:
        logger.error("Fullscreen capture example failed.")

    # Capture a specific region and save
    # Replace x, y, width, height with desired values
    region_bbox = (100, 100, 300, 200) 
    region_image = capture_region(region_bbox, "region_capture.png")
    if region_image:
        logger.info(f"Region capture example successful for {region_bbox} (image saved or returned).")
    else:
        logger.error(f"Region capture example failed for {region_bbox}.")

    # Capture screen to Image object without saving
    # screen_image_obj = capture_screen()
    # if screen_image_obj:
    #     screen_image_obj.show() # Display the image (optional)
    #     logger.info("Screen captured to object and shown.")

    # Capture region to Image object without saving
    # region_image_obj = capture_region(region_bbox)
    # if region_image_obj:
    #     region_image_obj.show() # Display the image (optional)
    #     logger.info(f"Region {region_bbox} captured to object and shown.")
    logger.info("screen_capture.py examples finished.")
