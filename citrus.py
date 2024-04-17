import os
from PIL import Image
import pillow_heif

def convert_heic_to_png(heic_file, output_png):
    print("Starting Conversion...please wait for final message")
    """Converts an HEIC image to PNG format.

    Args:
        heic_file (str): Path to the input HEIC image file.
        output_png (str): Path to the output PNG image file.
    """

    try:
        heif_image = pillow_heif.read_heif(heic_file)
        pil_image = Image.frombytes(heif_image.mode, heif_image.size, heif_image.data, "raw")
        pil_image.save(output_png, format="PNG")
        print(f"HEIC image converted to PNG: {output_png}")
    except Exception as e:
        print(f"Error converting HEIC image: {e}")

def convert_all_heic(heic_folder, output_folder=None):
    """Converts all HEIC images in a folder to PNG format, with a flag file check.

    Args:
        heic_folder (str): Path to the folder containing HEIC images.
        output_folder (str, optional): Path to the output folder for PNG images.
            Defaults to the same folder as HEIC images.
    """

    flag_file = os.path.join(heic_folder, "converted.flag")  # Create flag file path

    if not os.path.exists(flag_file):  # Check if flag file exists
        if not output_folder:
            output_folder = heic_folder

        for filename in os.listdir(heic_folder):
            if filename.endswith((".heic", ".HEIC")):  # Check for both extensions
                heic_filepath = os.path.join(heic_folder, filename)
                png_filename = os.path.splitext(filename)[0] + ".png"
                output_filepath = os.path.join(output_folder, png_filename)
                convert_heic_to_png(heic_filepath, output_filepath)

        # Create the flag file after conversion
        with open(flag_file, "w") as f:
            f.write("Conversion completed")
            print("Final Message: All HEIC images converted successfully.")
    else:
        print("HEIC images already converted (flag file found).")

if __name__ == "__main__":
    heic_folder = "./convert"
    convert_all_heic(heic_folder)