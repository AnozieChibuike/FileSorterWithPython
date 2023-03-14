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
  
  Code:<pre><code>for folders in [All the destination folder]:</pre></code>
  Checking if folder exist:<pre><code>if not os.path.exist(folders): # returns true if folder exist</code></pre>
  If folder does not exist: <pre><code>os.mkdir(folders) # creates a new folder with the non-existing folder as the name</code></pre>
- Then, I created a [tuple](https://www.w3schools.com/python/python_tuples.asp) with the tuple items as a string of each of the file extensions so the program can know what files to move
- And then, I created an empty [list](https://www.w3schools.com/python/python_lists.asp) named <code>files</code> which iterated files will be appended to it later.
  I created a [for loop](https://www.w3schools.com/python/python_for_loops.asp) to iterate over files in our download directory.

  Code:<pre><code>for f in os.listdir(download directory): # os.listdir returns a list of files and folders in the parameter given... the parameter must be a directory</code></pre>
  Then I use an [if statement](https://www.w3schools.com/python/python_conditions.asp) to filter out hidden files

  Code:<pre><code>if not f.startswith('.'): # hidden files starts with "." So it is filtered out </code></pre>
  Appending files that passes the if statement to our previous empty list named files
  Code:<pre><code>files.append(f)</code></pre>
