Task1.Part1

1) Log in to the system as root. Use the passwd command to change the password.

 ![screenshots](screenshots/1.png)

2) Examine the basic parameters of the command. What system file does it change *?

That file contains info about users, which can deal with different directories (following dirs) and files.
 ![screenshots](screenshots/2.png)

3) Determine the users registered in the system, as well as what commands they execute. What additional information can be gleaned from the command execution?

 ![screenshots](screenshots/3.png)

 ![screenshots](screenshots/4.png)

4) Change personal information about yourself.

 ![screenshots](screenshots/5.png)

5) Become familiar with the Linux help system and the man and info commands. 
Get help on the previously discussed commands, define and describe any two keys for these commands. Give examples.

 ![screenshots](screenshots/6.png)

 ![screenshots](screenshots/6.1.png)

 ![screenshots](screenshots/7.png)

 ![screenshots](screenshots/7.1.png)

6) Explore the more and less commands using the help system. View the contents of files .bash* using commands.

more .bash_history
 ![screenshots](screenshots/8.png)

less .bash_history
 ![screenshots](screenshots/9.png)

7) * Describe in plans that you are working on laboratory work 1. Tip: You should read the documentation for the finger command.

 ![screenshots](screenshots/10.png)

8) * List the contents of the home directory using the ls command, define its files and directories. Hint: Use the help system to familiarize yourself with the ls command.

 ![screenshots](screenshots/11.png)

Task1.Part2

1) Examine the tree command. Master the technique of applying a template, for example, display all files that contain a character c, or files that contain a specific sequence of characters. 
List subdirectories of the root directory up to and including the second nesting level.

 ![screenshots](screenshots/12.png)

 ![screenshots](screenshots/13.png)

2) What command can be used to determine the type of file (for example, text or binary)? Give an example.

 ![screenshots](screenshots/14.png)

3) Master the skills of navigating the file system using relative and absolute paths. How can you go back to your home directory from anywhere in the filesystem?

 ![screenshots](screenshots/15.png)

4) Become familiar with the various options for the ls command. Give examples of listing directories using different keys. 
Explain the information displayed on the terminal using the -l and -a switches.

 ![screenshots](screenshots/16.png)

5) Perform the following sequence of operations:
- create a subdirectory in the home directory;
- in this subdirectory create a file containing information about directories located in the root directory (using I/O redirection operations);
- view the created file;
- copy the created file to your home directory using relative and absolute addressing.
- delete the previously created subdirectory with the file requesting removal;
- delete the file copied to the home directory.

 ![screenshots](screenshots/17.png)

 ![screenshots](screenshots/18.png)

6) Perform the following sequence of operations:
- create a subdirectory test in the home directory;
- copy the .bash_history file to this directory while changing its name to labwork2;
- create a hard and soft link to the labwork2 file in the test subdirectory;
- how to define soft and hard link, what do these concepts;
- change the data by opening a symbolic link. What changes will happen and why (If we open and operate with symbolic link, nothing happens, because symbol link is just link to file name, but in Linux file registration is operating by inode.)
- rename the hard link file to hard_lnk_labwork2;
- rename the soft link file to symb_lnk_labwork2 file;
- then delete the labwork2. What changes have occurred and why? (After that we can operate with file using another hard link and another file name. But soft link is already unuseful, because file name it referred is already deleted.)

 ![screenshots](screenshots/19.png)
 
7) Using the locate utility, find all files that contain the squid and traceroute sequence.

 ![screenshots](screenshots/20.png)

8) Determine which partitions are mounted in the system, as well as the types of these partitions.

 ![screenshots](screenshots/21.png)

 ![screenshots](screenshots/22.png)

9) Count the number of lines containing a given sequence of characters in a given file.

 ![screenshots](screenshots/23.png)

10) Using the find command, find all files in the /etc directory containing the 
host character sequence.

 ![screenshots](screenshots/24.png)

11) List all objects in /etc that contain the ss character sequence. How can I 
duplicate a similar command using a bunch of grep?

 ![screenshots](screenshots/25.png)

12) Organize a screen-by-screen print of the contents of the /etc directory. Hint: 
You must use stream redirection operations.

 ![screenshots](screenshots/26.png)

13) What are the types of devices and how to determine the type of device? Give 
examples.

 ![screenshots](screenshots/27.png)

14) How to determine the type of file in the system, what types of files are there?
lsscsi - shows hard disc and optical disc drives
lsusb - shows USB devices in system. Lspci shows controller of USB.

 ![screenshots](screenshots/28.png)

15) * List the first 5 directory files that were recently accessed in the /etc directory

 ![screenshots](screenshots/29.png)
