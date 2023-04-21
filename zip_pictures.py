import os
import shutil
import zipfile
from datetime import datetime

# Set the root folder path
root_folder = "C:\\Users\\habdulra\\Downloads"

# Iterate through all the files in the root folder
for file_name in os.listdir(root_folder):
    file_path = os.path.join(root_folder, file_name)
    # Check if the file is an image (you can customize the file extension as needed)
    if file_name.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
        # Get the modified date of the image file
        modified_date = datetime.fromtimestamp(os.path.getmtime(file_path))
        # Create a zip file name with the format: yyyy_mm_dd.zip
        zip_file_name = f"{modified_date.year}_{modified_date.month:02d}_{modified_date.day:02d}.zip"
        # Create a folder name with the format: yyyy_mm
        folder_name = f"{modified_date.year}_{modified_date.month:02d}"

        # Check if the folder already exists
        if not os.path.exists(os.path.join(root_folder, folder_name)):
            # If not, create the folder
            os.mkdir(os.path.join(root_folder, folder_name))

        # Check if the zip file already exists
        if os.path.exists(os.path.join(root_folder, folder_name, zip_file_name)):
            # If it does, append the image to the existing zip file
            with zipfile.ZipFile(os.path.join(root_folder, folder_name, zip_file_name), "a") as zipf:
                zipf.write(file_path, file_name)
        else:
            # If it doesn't, create a new zip file with the image
            with zipfile.ZipFile(os.path.join(root_folder, folder_name, zip_file_name), "w") as zipf:
                zipf.write(file_path, file_name)

        # Remove the original image file
        os.remove(file_path)

