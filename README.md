# OVERVIEW

This Program makes it **easier** for **users** to **sort** or **arrange** files stored in the user's _system download_ directory by _automating_ the process of moving files like; Videos,Photos,Documents ...e.t.c to their respective folders, moving _all_ files at _once_.
If a destination folder does **NOT** exist,A _new_ one is automatically created by the program as the name of the missing folder for the type of file supposed to be stored in it.

# ADDED FEATURES

The Program counts the number of files moved, specify the type moved and the amount

# STRUCTURE

- Firstly, I imported the required ***modules*** for the program

   > os module 

   >move method from shutil module

   >Path method from pathlib module

    Since they are ***built-in*** python libraries, you do not need to worry about any installation of module.
- Secondly, I set the download directory/folder using:<pre><code>str"Path.home()" + "\Downloads"</code></pre> <code>Path.home()</code> returns the a value of the home directory, see: [PathLib Example](https://www.tutorialspoint.com/How-to-find-the-real-user-home-directory-using-Python) to learn more.
  I did the same for all the destination folders replacing<code>"\Downloads"</code> with <code>"\\{Name of destination folder}"</code>
- Thirdly, I iterated through the destination folders and if they do not exist a new one is created.
  code:<pre><code>for folders in [All the destination folder]:
          if not os.path.exist(folders): # returns true if folder exist
       </code></pre>
