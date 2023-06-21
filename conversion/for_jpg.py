import os
import shutil
from PIL import Image

folder_path = "dragons"
output_folder_png = os.path.join(folder_path, "completed_colour")
output_folder_jpg = os.path.join(folder_path, "completed_jpg")
file_list = []

start_time = "0000"  # Specify the start time here (e.g., "0000", "1237")

# Create the output folders if they don't exist
if not os.path.exists(output_folder_png):
    os.makedirs(output_folder_png)

if not os.path.exists(output_folder_jpg):
    os.makedirs(output_folder_jpg)

# Iterate over the files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".png"):
        file_list.append(filename)

# Sort the file list based on the number before the hyphen
file_list.sort(key=lambda x: int(x.split("-")[0]))

# Convert the start time to minutes
start_hour = int(start_time[:2])
start_minute = int(start_time[2:])
start_minutes = start_hour * 60 + start_minute

# Copy the files to the output folder with incrementing hour-minute filenames (PNG)
for i, filename in enumerate(file_list):
    minutes = start_minutes + i  # Calculate the current minutes based on the start time and index
    hour = str(minutes // 60).zfill(2)  # Calculate the hour value
    minute = str(minutes % 60).zfill(2)  # Calculate the minute value
    output_filename = f"{hour}{minute}.png"
    output_path = os.path.join(output_folder_png, output_filename)
    shutil.copy2(os.path.join(folder_path, filename), output_path)
    print(f"Copied {filename} to {output_path}")

    # Convert and save the PNG files to JPEG format (JPG)
    output_filename_jpg = f"{hour}{minute}.jpg"
    output_path_jpg = os.path.join(output_folder_jpg, output_filename_jpg)

    # Open the PNG file
    png_path = os.path.join(output_folder_png, output_filename)
    with Image.open(png_path) as img:
        # Convert and save as JPEG
        img = img.convert("RGB")
        img.save(output_path_jpg, "JPEG")
        print(f"Converted {filename} to {output_path_jpg}")
