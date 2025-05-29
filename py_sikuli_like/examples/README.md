# PySikuliX Example Scripts

This directory contains example scripts demonstrating how to use the `pysikulix` library for basic GUI automation tasks.

## Prerequisites

1.  **PySikuliX Library**:
    The `pysikulix` library must be installed or accessible in your Python environment.
    If you have cloned the `py_sikuli_like` repository, you can install it in editable mode from the root directory of the project (`py_sikuli_like`):
    ```bash
    pip install -e .
    ```
    This command installs the library and its dependencies listed in the main `requirements.txt`.

2.  **Python Environment**:
    Ensure you have Python installed. These scripts are generally compatible with Python 3.x.
    The necessary dependencies for `pysikulix` (like Pillow, mss, opencv-python, PyAutoGUI) will be installed by the command above.

3.  **Display Server**:
    `pysikulix` interacts with the screen, so it requires a running display server (e.g., X11 on Linux, or the standard GUI environments on Windows/macOS). It typically won't work in headless environments without virtual display software (e.g., Xvfb).

## Example Images

The example scripts use placeholder images located in the `examples/images/` subdirectory:
*   `red_square.png`
*   `blue_circle.png`
*   `green_triangle.png`

**IMPORTANT FOR IMAGE-BASED EXAMPLES (`ex01`, `ex02`, `ex03`):**
For these scripts to successfully find the specified images (`red_square.png`, `blue_circle.png`, `green_triangle.png`), the target image **MUST BE VISIBLE ON YOUR SCREEN** when the script is running.

*   **How to make images visible**: Before running an image-based example, open the corresponding PNG file (e.g., `examples/images/red_square.png`) using your system's default image viewer.
*   **No obstructions**: Ensure the image is not significantly obstructed by other windows.
*   **Original size and appearance**: The scripts expect the images to appear as they are in the files (no scaling, rotation, or significant color changes).

## Running the Examples

Navigate to the `py_sikuli_like/examples` directory in your terminal. You can then run each script using Python:

```bash
python ex01_find_image.py
```

```bash
python ex02_click_image.py
```

```bash
python ex03_type_at_image.py
```

```bash
python ex04_click_coordinates_and_type_globally.py
```

**Script Descriptions:**

*   **`ex01_find_image.py`**:
    *   Demonstrates using `pysikulix.find()` to locate `images/red_square.png` on the screen.
    *   It will print the coordinates if the image is found.
    *   **Remember to open `images/red_square.png` to make it visible before running.**

*   **`ex02_click_image.py`**:
    *   Demonstrates using `pysikulix.click()` to find and click `images/blue_circle.png`.
    *   **Remember to open `images/blue_circle.png` to make it visible before running.**

*   **`ex03_type_at_image.py`**:
    *   Demonstrates using `pysikulix.type_text_at()` to find `images/green_triangle.png`, click its center, and then type "Hello from PySikuliX!".
    *   **Remember to open `images/green_triangle.png` to make it visible.**
    *   Note: The text will be typed into whichever window becomes active after the click. For a simple image viewer, this might not be a text input field.

*   **`ex04_click_coordinates_and_type_globally.py`**:
    *   Demonstrates using `pysikulix.click()` with absolute screen coordinates (e.g., 100,100) and then `pysikulix.type_text_globally()` to type into the currently focused window.
    *   **WARNING**: Clicking arbitrary screen coordinates can interact with any application or desktop element at that location. Be cautious and ensure the chosen coordinates are safe on your system.

## Logging

The scripts and the `pysikulix` library use Python's `logging` module. By default, you will see INFO level messages in the console, which provide a good overview of the operations. For more detailed output from the `pysikulix` library itself (e.g., for debugging), you can often uncomment a line in the example scripts like:
`# pysikulix_logger.setLevel(logging.DEBUG)`

If you encounter issues, the log messages can provide valuable clues.

Happy automating!
