# Absolute Path - starts from the root of the hard disk
# Relative Path - path starting from current directory

from pathlib import Path

path = Path("ecommerce")
print(path.exists())

#path = Path("emails")
# print(path.mkdir())
# print(path.rmdir())

path = Path()
print(path.glob('*.py'))
for file in path.glob('*.py'):
    print(file)
# with glob() we can search directories and files in the current path.
# * - all files and directories
# *.* - we will get all files with all extentions
