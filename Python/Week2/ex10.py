import sys, glob, os
import getpass

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')

# TODO: Use the glob.glob() function to obtain the list of filenames

file_names = glob.glob(pattern)

print(file_names)

# TODO: use os.path.getsize to find each file's size
#For Loop
for files in file_names:
    size = os.path.getsize(files)
 #   print(size)

# TODO: Add a test to only display files that are not zero length
'''''''''''
for files in file_names:
    size = os.path.getsize(files)
    new_list = []
    if size != 0:
        new_list.append(size)

        file_names = new_list
        print(file_names)
'''''''''
'''''''''''
for files in file_names:
    size = os.path.getsize(files)
    if size == 0:
        file_names.remove(files)
    else:
        new_name = os.path.basename(files)
        print(new_name, size)
''''''''

# TODO: Remove the leading directory name(s) from each filename before you print it - 
# using os.path.basename()
''''''''''''''
for files in file_names:
    new_name = os.path.basename(files)
    print(new_name)
'''''''''''''''

''''''''''''