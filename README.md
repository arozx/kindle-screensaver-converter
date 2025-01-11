# Kindle Screensaver Converter

This Python script converts images into screensavers compatible with Kindle devices (in order to replace the default ones if you know how or use them as screensavers in KOReader). It allows you to set dimensions, resolution, and bit depth while applying smart cropping and grayscale adjustments to highlight the most prominent parts of the image.

> There is a new version with GUI [here](https://github.com/neura-neura/kindle-screensaver-converter-gui)

## Features

- **Dimension Control:** Specify the target height and width in pixels.
- **Resolution Adjustment:** Define horizontal and vertical resolution (DPI).
- **Bit Depth Configuration:** Customize the bit depth of the output.
- **Smart Cropping:** Automatically detects and retains the most visually prominent area of the image.
- **Scaling Before Cropping:** Ensures the maximum part of the image is preserved by scaling before cropping.
- **Grayscale with Contrast Enhancement:** Applies grayscale with enhanced contrast for better visual impact.
- **Output Format:** Saves images in PNG format.
- **Custom Folder Handling:** Processes images from a folder named `PUT YOUR IMAGES HERE` and saves results in a `converted_screensavers` folder in the root directory.

## Requirements

- Python 3.x
- [Pillow](https://pypi.org/project/pillow/) (Python Imaging Library fork)

## Installation

1. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   ```

2. **Activate the Virtual Environment:**
   - On **Windows (CMD):**
     ```bash
     venv\Scripts\activate
     ```
   - On **Windows (PowerShell):**
     ```bash
     .\venv\Scripts\Activate.ps1
     ```
   - On **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Place your images in a folder named `PUT YOUR IMAGES HERE`.

2. Run the script:
   ```bash
   python kindle_screensaver_converter.py
   ```

3. Provide the required details when prompted:
   - Target dimensions (height and width in pixels).
   - Horizontal and vertical resolution (DPI).
   - Bit depth.

4. The script will process the images and save the converted versions in a folder named `converted_screensavers`.

## Example

Suppose you have a folder `PUT YOUR IMAGES HERE` containing images you want to convert. Run the script and enter the following when prompted:

- Target Height: 800 pixels
- Target Width: 600 pixels
- Horizontal Resolution: 96 DPI
- Vertical Resolution: 96 DPI
- Bit Depth: 8

The converted images will appear in a folder named `converted_screensavers` in the script's root directory.

## Troubleshooting

- Ensure that the `PUT YOUR IMAGES HERE` folder exists and contains valid image files.
- Verify Python and Pillow installation.
- Ensure you have read/write permissions in the directory.
> Note that the PNG format always saves grayscale images with 8 bits per pixel, regardless of the simulated bit depth applied during processing. While the visual effect of reducing the grayscale levels (e.g., to 1, 2, or 4 bits) is evident in the resulting images, the file properties will consistently indicate an 8-bit depth. This is because PNG does not natively support lower bit depths for grayscale images; the quantization we apply is effectively a simulation. For example, specifying 1 bit results in only 2 grayscale levels (black and white), but the image is still stored as 8 bits per pixel. Similarly, 2-bit quantization produces 4 grayscale levels, and 4-bit quantization yields 16 levels, yet both are saved in an 8-bit format.



## License

This project is open-source and available under the MIT License.
