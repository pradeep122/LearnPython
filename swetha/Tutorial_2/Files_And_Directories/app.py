# Absolute Path - It starts from the root of the hard disk
# eg:/usr/local/bin
# Relative Path - We start from current directory and go somewhere else

from pathlib import Path
path = Path("ecommerce")
print(path.exists())

# path = Path("emails")

# To make directory
# print(path.mkdir())

# To remove directory
# print(path.rmdir())

# glob() is used to search the files with a pattern
# To get all the files and directories from the current directory
# path = Path()
# print(path.glob('*'))

# To get all the files but not the directories from the current directory
# path = Path()
# print(path.glob('*.*'))

# To get all the .py files but not the directories from the current directory
path = Path()
for file in path.glob('*.py'):
    print(file)
