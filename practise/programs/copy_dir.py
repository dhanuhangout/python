"""This module copies a directory to another directory with files."""
#!/usr/bin/python

# import error
import os, sys
import shutil

C_DIR = os.getcwd()
SRC_DIR = '%s/../programs' % C_DIR

sys.path.append(SRC_DIR)

def copy_dir(src, dest):
    """Copies a directory to another directory with files."""
    try:
        shutil.copytree(src, dest)
    except OSError as e:
        # If the error was caused because the source wasn't a directory
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dest)
        else:
            print('Directory not copied. Error: %s' % e)


def main():
    """Start of the program."""
    src = SRC_DIR+'/'+'dir1'
    dest = SRC_DIR+'/'+'dir2'
    copy_dir(src, dest)

if __name__ == '__main__':
    main()

# Ref:
# https://www.pythoncentral.io/how-to-recursively-copy-a-directory-folder-in-python/