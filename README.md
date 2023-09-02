# File Sorting Program Documentation

This is a Python program that organizes files in a user's Downloads folder into different folders based on their file type.


# Dependencies
-Great Mindset
-Python 3.6 or higher
-os module
-shutil module
-pathlib module

# Usage

Clone or download the repository to your local machine.
Navigate to the directory where the program is saved.
Open a terminal or command prompt window in the directory.

### Windows
Run the program using the command <pre><code>python main.py</code></pre> or running the file<pre><code>run.bat</code></pre>

### Linux
Run the program using the command <pre><code>python3 main.py</code></pre> or running <pre><code>./run.sh</code></pre>


# How it works

The program specifies the user's Downloads directory as the <code>root_dir</code>.
It creates new folders to organize the files based on their file type: <code>video_dir, pic_dir, doc_dir, app_dir, other_dir, sub_dir, music_dir, and zip_dir</code>.
The program then looks for all files in the <code>root_dir</code> that are not hidden or the script file itself, and adds them to a [list](https://www.w3schools.com/python/python_lists.asp) called <code>files</code>.
The program then iterates through each file in files and checks the file extension to determine its file type.
If the file is a video file, it is moved to the video_dir. If it is a picture, it is moved to the pic_dir, and so on.
If the file does not match any of the specified file types, it is moved to the <code>other_dir</code>.
The program keeps track of the number of files moved to each folder and prints a success message for each folder with moved files.
Finally, the program prints the total number of files moved.

### Supported file types

***Video***: .mp4, .mkv, .mov, .webm, .MP4

***Picture***: .jpg, .jpeg, .png, .svg, .gif, .tif, .tiff

***Document***: .docx, .doc, .txt, .pdf, .xls, .ppt, .xlsx, .pptx, .html

***Application***: .exe, .dmg, .pkg

***Subtitle***: .srt

***Audio***: .mp3, .aud, .wav, .wax, .m4a, .aac

***Compressed files***: .zip, .7z, .zipx, .rar, .tar

***Other***: any file that does not match the above file types.

Example output:
<pre><code>
video_dir does not exist, creating folder...
pic_dir does not exist, creating folder...
doc_dir does not exist, creating folder...
app_dir does not exist, creating folder...
other_dir does not exist, creating folder...
sub_dir does not exist, creating folder...
music_dir does not exist, creating folder...
zip_dir does not exist, creating folder...
Successfully moved 5 video(s)!
Successfully moved 2 photo(s)!
Successfully moved 3 document(s)!
Successfully moved 1 executable(s)!
Successfully moved 1 subtitle(s)!
Successfully moved 2 music file(s)!
Successfully moved 1 compressed file(s)!
Successfully moved 1 other file(s)!

Moved total of 16 files
</pre></code>
# Limitations

This script only organizes files in the user's Downloads folder. If the user has files in other directories that they would like to organize, they will need to modify the script accordingly.

Also, this script only organizes files based on their file extensions. It does not use any advanced techniques to determine file types based on their contents. As a result, there may be some files that are not moved into the correct subfolder.

