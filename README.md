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
  I did the same for all the destination folders replacing<code>"\Downloads"</code> with <code>"\\{Name of destination folder}"</code>NOTE : I used <code>Path.home()</code> so the program can be cross platform
- Thirdly, I iterated through the destination folders and if they do not exist a new one is created.
  
  Code:<pre><code>for folders in [All the destination folder]:</pre></code>
  Checking if folder exist:<pre><code>if not os.path.exist(folders): # returns true if folder exist</code></pre>
  If folder does not exist: <pre><code>os.mkdir(folders) # creates a new folder with the non-existing folder as the name</code></pre>
- Then, I created a [tuple](https://www.w3schools.com/python/python_tuples.asp) with the tuple items as a string of each of the file extensions so the program can know what files to move
- And then, I created an empty [list](https://www.w3schools.com/python/python_lists.asp) named <code>files</code> which iterated files will be appended to it later.
  I created a [for loop](https://www.w3schools.com/python/python_for_loops.asp) to iterate over files in our download directory.

  Code:<pre><code>for f in os.listdir(download directory): # os.listdir returns a list of files and folders in the parameter given... the parameter must be a directory</code></pre>
  Then I use an [if statement](https://www.w3schools.com/python/python_conditions.asp) to filter out hidden files.

  Code:<pre><code>if not f.startswith('.'): # hidden files starts with "." So it is filtered out </code></pre>
  Appending files that passes the if statement to our previous empty list named files.

  Code:<pre><code>files.append(f)</code></pre>
- Lastly I iterated through the new list of files named files.

  Code:<pre><code>for file in files:</pre></code>
  Creating an if statement to know the type of file to move, 
  
  Here is an example for video files:<pre><code>if file.endswith(previously created tuple for video file extension): # returns true or false for each iteration</code></pre>
  Moving the files that pass the if statement with the method from shutil called move:<pre><code>move(downloadDirectory + r"\" + file , Video destination Folder) # Here the move method takes 2 parameters : Folder we are moving file out from and Destination folder</code><pre>
  I do this process for each file extension ; photos,documents,compressed files...e.t.c

# INSTALLATION/RUNNING/REQUIREMENT 
- git , Go to [Git downloads](https://git-scm.com/downloads) to check installation for your Operating System
- Python 3.x + , Go to [Python website](https://www.python.org/downloads/) and download the latest python version
- Command Line for windows or Terminal for Linux users

***

Running program for window Users
- Open Command Line
- run:<pre><code>git clone https://github.com/AnozieChibuike/FileSorterWithPython</code></pre>A new folder named ***FileSorterWithPython*** will be created
- Tell the command line to go to the ***FileSorterWithPython*** folder<pre><code>cd FileSorterWithPython</code></pre>
- Run program:<pre><code>py fileMod.py</code></pre>

***

Running program for Linux Users
- Open Terminal
- run:<pre><code>git clone https://github.com/AnozieChibuike/FileSorterWithPython</code></pre>A new folder named ***FileSorterWithPython*** will be created
- Tell the Terminal to go to the ***FileSorterWithPython*** folder<pre><code>cd FileSorterWithPython</code></pre>
- <code>ls</code> to see the files in the ***FileSorterWithPython*** folder
- Run program:<pre><code>python3 fileMod.py</code></pre>
