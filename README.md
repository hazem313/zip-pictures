# zip-pictures
zip pictures by date 


## Image Zipper

This Python script is designed to organize and compress image files in a specified folder by creating zip files for each day's images and monthly zip files for images in the same month and year. The script utilizes the `os` and `zipfile` modules from Python's standard library, as well as the `datetime` module for date manipulation.

```bash
pip install os
pip install zipfile


```python
val = test


### Usage

1. Update the `source_folder` variable to specify the folder path where your image files are located.
2. Optionally, update the `valid_extensions` variable to specify the file extensions of the image files you want to include. By default, `.jpg`, `.jpeg`, and `.png` extensions are included.
3. Run the script in a Python environment.

The script performs the following steps:

1. Iterates through the image files in the source folder and extracts the modification date information.
2. Organizes the image files into a dictionary (`date_dict`) with keys as the modification dates in the format of `YYYY-MM-DD` and values as the corresponding image file paths.
3. Creates zip files for each day's images, with the date as the zip file name, and adds the image files to the respective zip files.
4. Removes the original image files from the root folder after adding them to the zip files.
5. Creates monthly zip files for images in the same month and year, with the format of `YYYY-MM.zip`, and adds the daily zip files for the corresponding month and year to the monthly zip files.
6. Removes the daily zip files after adding them to the monthly zip files.

Note: The script assumes that the images are organized based on the modification date of the files. If you want to use the creation date instead, you can update the `datetime.fromtimestamp(os.path.getmtime(image_file_path))` to `datetime.fromtimestamp(os.path.getctime(image_file_path))` in the script.

Please make sure to backup your image files before running the script, as it removes the original image files from the root folder after zipping them.

### Requirements

The script requires Python 3.x and the following standard Python modules:

- os
- zipfile
- datetime

### Disclaimer

This script is provided as-is without any warranty. Please use it at your own risk. Always make sure to backup your files before running any script that modifies or deletes files.
