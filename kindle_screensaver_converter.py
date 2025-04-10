import os
from PIL import Image, ImageEnhance
import numpy as np

# ASCII Art Title
def print_title():
    print("""
        
╦╔═┬┌┐┌┌┬┐┬  ┌─┐  ╔═╗┌─┐┬─┐┌─┐┌─┐┌┐┌┌─┐┌─┐┬  ┬┌─┐┬─┐  ╔═╗┌─┐┌┐┌┬  ┬┌─┐┬─┐┌┬┐┌─┐┬─┐
╠╩╗││││ │││  ├┤   ╚═╗│  ├┬┘├┤ ├┤ │││└─┐├─┤└┐┌┘├┤ ├┬┘  ║  │ ││││└┐┌┘├┤ ├┬┘ │ ├┤ ├┬┘
╩ ╩┴┘└┘─┴┘┴─┘└─┘  ╚═╝└─┘┴└─└─┘└─┘┘└┘└─┘┴ ┴ └┘ └─┘┴└─  ╚═╝└─┘┘└┘ └┘ └─┘┴└─ ┴ └─┘┴└─
made by neura - https://github.com/neura-neura/kindle-screensaver-converter
    """)

def enhance_contrast_grayscale(image):
    image = image.convert("L")  # Convert to grayscale
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(2.0)  # Enhance contrast

def adjust_bit_depth(image, bit_depth):
    if bit_depth == 8:
        return image  # 8-bit is the default value for grayscale images
    
    # Calculate number of gray levels based on bit depth
    levels = 2 ** bit_depth - 1
    
    # Convert to array for pixel manipulation
    img_array = np.array(image)
    
    # Normalize and adjust to the new bit range
    normalized = img_array / 255.0  # Normalize to range 0-1
    adjusted = np.round(normalized * levels) * (255 / levels)  # Adjust to new range and scale back to 8 bits
    
    # Adjust to new range and scale back to 8 bits
    return Image.fromarray(adjusted.astype(np.uint8))

def get_most_prominent_frame(image):
    # Detect the most "prominent" region to keep based on brightness
    grayscale_image = image.convert("L")
    histogram = grayscale_image.histogram()
    brightness = sum(i * histogram[i] for i in range(256)) / sum(histogram)

    # Placeholder logic for determining a "prominent" frame, can be improved
    # For now, we return the center cropped frame as fallback
    return grayscale_image.crop((
        (grayscale_image.width - 100) // 2,
        (grayscale_image.height - 100) // 2,
        (grayscale_image.width + 100) // 2,
        (grayscale_image.height + 100) // 2,
    ))

def process_images(height, width, dpi_x, dpi_y, bit_depth):
    input_folder = "input_images"
    output_folder = "converted_screensavers"
    os.makedirs(output_folder, exist_ok=True)

    images = [f for f in os.listdir(input_folder) if f.lower().endswith((".jpg", ".jpeg", ".png"))]

    for idx, image_name in enumerate(images):
        image_path = os.path.join(input_folder, image_name)
        with Image.open(image_path) as img:
            # Resize and crop intelligently
            img = img.convert("RGB")
            scale_factor = max(width / img.width, height / img.height)
            new_width = int(img.width * scale_factor)
            new_height = int(img.height * scale_factor)
            img = img.resize((new_width, new_height), Image.LANCZOS)

            # Get prominent frame
            left = (img.width - width) // 2
            top = (img.height - height) // 2
            right = left + width
            bottom = top + height
            img = img.crop((left, top, right, bottom))

            # Apply enhanced grayscale and adjust bit depth
            img = enhance_contrast_grayscale(img)
            img = adjust_bit_depth(img, bit_depth)

            # Save converted image
            output_name = f"bg_ss{str(idx + 1).zfill(2)}_{image_name}.png"
            output_path = os.path.join(output_folder, output_name)
            img.save(output_path, "PNG", dpi=(dpi_x, dpi_y))

        print(f"Processed image {idx + 1}/{len(images)}: {image_name}")

    print(f"\nConversion complete! Converted images are in: {output_folder}")

if __name__ == "__main__":
    print_title()
    print("Processing images from 'PUT YOUR IMAGES HERE' folder...")

    kindle_height = int(input("Enter target height (pixels): "))
    kindle_width = int(input("Enter target width (pixels): "))
    kindle_dpi_x = int(input("Enter horizontal resolution (DPI): "))
    kindle_dpi_y = int(input("Enter vertical resolution (DPI): "))
    kindle_bit_depth = int(input("Enter bit depth: "))

    process_images(kindle_height, kindle_width, kindle_dpi_x, kindle_dpi_y, kindle_bit_depth)
