"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import os
import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
cmdLineArg = sys.argv
print("Command Line Argument(s):")
for i in cmdLineArg:
    print(i)

# Print out the OS platform you're using:
# YOUR CODE HERE
print("Operating System Platform", sys.platform)

# Print out the version of Python you're using:
# YOUR CODE HERE
print("Python version: ", sys.version_info.major, ".", sys.version_info.minor,
      ".", sys.version_info.micro, " - ", sys.version_info.releaselevel, sep='')

# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print("Current Process Id:", os.getpid())

# Print the current working directory (cwd):
# YOUR CODE HERE
print("Current Working Directory:", os.getcwd())

# Print out your machine's login name
# YOUR CODE HERE
print("Login Name:", os.getlogin())
