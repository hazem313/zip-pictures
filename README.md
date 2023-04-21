# Image Organizer

This Python script helps organize image files (with extensions .png, .jpg, .jpeg, .gif) in a given root folder by creating folders based on the modified date of the image files and zipping them for easy storage and sharing. It uses the `os`, `shutil`, and `zipfile` modules for file and folder manipulation.

## How to Use

1. Make sure you have Python installed on your system.
2. Clone or download the script to your local machine.
3. Open the script in a Python IDE or text editor.
4. Set the `root_folder` variable to the path of the folder where your image files are located.
5. Customize the image file extensions in the `if` statement as needed.
6. Run the script.

The script will iterate through all the files in the `root_folder`, check if they are image files based on the extensions, create folders based on the modified date of the image files, and zip them into files named in the format `yyyy_mm_dd.zip`. If a folder or zip file already exists with the same name, the script will append the image to the existing zip file. Finally, the original image files will be removed.

Please note that this script will modify your file system by creating folders, zipping files, and deleting original image files. Use it with caution and make sure to backup your files before running the script.

## License

This script is released under the [MIT License](LICENSE) which allows for personal and commercial use with attribution.
