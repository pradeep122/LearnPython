# Packages are another way to organize our code.
# A Package is a container for multiple modules
# In file system terms,
# Package is a directory or folder
import sys
sys.path.append('/Users/deepster/Sites/LearnPython/swetha/Tutorial_2')


if __name__ == "__main__":
    from ecommerce.shipping import calc_shipping
    calc_shipping()
