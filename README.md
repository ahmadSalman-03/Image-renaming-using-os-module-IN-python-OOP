This Python script, clutterClear, is designed to manage and organize files by copying and renaming them from one folder to another. The program utilizes the os and shutil libraries to perform file operations, making it useful for decluttering directories or organizing large numbers of files, especially images.

Description of Code Functionality
Imports:

os: Provides functions to interact with the operating system, like listing and renaming files.
shutil: Offers high-level file operations, such as copying files with metadata.
Class clutterClear:

The clutterClear class is initialized with two attributes:
origin: The path of the folder from which files will be copied.
destination: The path of the folder where files will be copied to.
Methods:
copy: Copies files from the origin directory to the destination directory, specifically copying files from index 12 to 50. If there’s a PermissionError, it will be handled and an error message will be printed.
rename: Renames all files in the destination directory sequentially as 0.png, 1.png, 2.png, etc., making it easier to organize or remove duplicate filenames.
Main Program Execution:

The user is prompted to select an option to either copy files, rename files, or quit the program.
Based on the choice:
If the user selects to copy files, they will be prompted to enter the origin and destination paths, and the program will copy files from the specified origin to the destination.
If the user selects to rename files, they will be asked for the destination path, and the program will rename all files in the destination sequentially.
If an invalid option is entered, an error message prompts the user to enter a valid integer.
Usage Example
plaintext
Copy code
Press 1 to copy files.
Press 2 to rename files.
Press 3 to quit!
This interactive interface allows the user to select a file management operation easily.

Example Use Cases
Photo Management: Useful for photographers or anyone handling a large collection of images, enabling them to copy specific files and organize them in a systematic way.
Data Organization: Can help organize files in research, data science, or any field where files need to be moved and renamed frequently.
Notes
Make sure the origin and destination directories exist and contain the necessary permissions for copying and renaming files.
The script currently copies files from indexes 12 to 50 in the origin directory, which can be modified as needed.
This script serves as a basic file management utility, helping to clear clutter by copying and renaming files efficiently.
