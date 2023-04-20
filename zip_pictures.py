import os
import zipfile
from datetime import datetime

source_folder = 'C:\\Users\\habdulra\\Downloads'

# Step 1: Iterate through images and extract date information
image_files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]
date_dict = {}
valid_extensions = ['.jpg', '.jpeg', '.png']  # Add more valid image file extensions if needed

for image_file in image_files:
    if os.path.splitext(image_file)[1].lower() in valid_extensions:
        image_file_path = os.path.join(source_folder, image_file)
        image_date = datetime.fromtimestamp(os.path.getmtime(image_file_path)).strftime('%Y-%m-%d')  # Extract modification date

        if image_date in date_dict:
            date_dict[image_date].append(image_file_path)
        else:
            date_dict[image_date] = [image_file_path]

# Step 2: Create zip files for each day
for date, image_files in date_dict.items():
    # Create zip file with date as name
    zip_file_name = os.path.join(source_folder, f'{date}.zip')
    with zipfile.ZipFile(zip_file_name, 'w') as zipf:
        for image_file in image_files:
            # Add image file to the zip file
            zipf.write(image_file, os.path.basename(image_file))
            os.remove(image_file)  # Remove image file from root folder after adding it to zip file

# Step 3: Create monthly zip files
for date, _ in date_dict.items():
    year, month, _ = date.split('-')
    monthly_zip_file_name = os.path.join(source_folder, f'{year}-{month}.zip')
    with zipfile.ZipFile(monthly_zip_file_name, 'w') as monthly_zipf:
        for date, _ in date_dict.items():
            if date.startswith(f'{year}-{month}'):
                # Add daily zip files for the corresponding month and year to the monthly zip file
                daily_zip_file_name = os.path.join(source_folder, f'{date}.zip')
                monthly_zipf.write(daily_zip_file_name, os.path.basename(daily_zip_file_name))
                os.remove(daily_zip_file_name)  # Remove daily zip files after adding them to monthly zip file
