import os
import shutil
import zipfile
from datetime import datetime

# Set the root folder path
root_folder = "C:\\camera_FTP"

# Recursive function to process subdirectories
def process_subdirectories(folder_path):
    for folder_name, subfolders, file_names in os.walk(folder_path):
        for file_name in file_names:
            file_path = os.path.join(folder_name, file_name)
            # Check if the file is an image (you can customize the file extension as needed)
            if file_name.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
                # Get the modified date of the image file
                modified_date = datetime.fromtimestamp(os.path.getmtime(file_path))
                # Create a zip file name with the format: yyyy_mm_dd.zip
                zip_file_name = f"{modified_date.year}_{modified_date.month:02d}_{modified_date.day:02d}.zip"
                # Create a folder name with the format: yyyy_mm
                folder_name = f"{modified_date.year}_{modified_date.month:02d}"

                # Get the relative path of the current folder within the root folder
                relative_folder_path = os.path.relpath(folder_name, root_folder)
                # Create the corresponding folder structure in the root folder
                zip_folder_path = os.path.join(root_folder, relative_folder_path, folder_name)
                os.makedirs(zip_folder_path, exist_ok=True)

                # Check if the zip file already exists
                if os.path.exists(os.path.join(zip_folder_path, zip_file_name)):
                    # If it does, append the image to the existing zip file
                    with zipfile.ZipFile(os.path.join(zip_folder_path, zip_file_name), "a") as zipf:
                        zipf.write(file_path, file_name)
                else:
                    # If it doesn't, create a new zip file with the image
                    with zipfile.ZipFile(os.path.join(zip_folder_path, zip_file_name), "w") as zipf:
                        zipf.write(file_path, file_name)

                # Remove the original image file
                os.remove(file_path)

        for subfolder in subfolders:
            subfolder_path = os.path.join(folder_name, subfolder)
            process_subdirectories(subfolder_path)

# Start processing from the root folder
process_subdirectories(root_folder)
