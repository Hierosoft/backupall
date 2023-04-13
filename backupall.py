'''
This script is for Windows 2000 machines such as the
Manncorp Pick & Place.

This script must be tested to work on:
*Python 3.2* to work on win2k
(Python 3.4 failed to install due to a component that could not run).

This script uses dirsync (an improved fork of Python robocopier).
'''

from __future__ import print_function
import sys
import os
from dirsync import sync

if sys.version_info.major < 3:
    input = raw_input

# default_sources = ["C:\\Users\\Jatlivecom\\Downloads\\flashfloppy-3.39\\hex"]
# destinations = ["D:\\"]
# ^ test data
default_sources = ["C:\\", "D:\\"]
destinations = ["E:\\", "F:\\", "G:\\"]


def echo0(*args):
    print(*args, file=sys.stderr)


def backup(sources, destination_root):
    for source in sources:
        if not os.path.isdir(source):
            raise FileNotFoundError(
                'The source "{}" does not exist.'.format(source)
            )
        root = source
        prev_root = root
        while True:
            prev_root = root
            root = os.path.dirname(root)
            if root == prev_root:
                break
        if os.path.sep == "\\":
            if root.endswith("\\"):
                root = root[:-1]
            if root.endswith(":"):
                root = root[:-1]
        destination = os.path.join(destination_root, root)
        # ^ such as E:\c or E:\d
        print("[backup] sync('{}', '{}')".format(source, destination))
        if not os.path.isdir(destination):
            os.mkdir(destination)
            # NOTE: use mkdir to ensure the path is ok
            #   (os.makedirs would create intermediate directories).
        sync(source, destination, 'sync')  # 'sync': one way
    return 0


def main():
    sources = default_sources
    destination = None
    for try_dest in destinations:
        if os.path.isdir(os.path.join(try_dest, "d")):
            destination = try_dest
    if destination is None:
        echo0('Error: There is no configured backup drive (checked {}).'
              ''.format(destinations))
        echo0('- Create the "d" directory to mark a backup drive.')
        return 1
    echo0("[main] * using drive {}".format(destination))
    return backup(sources, destination)


if __name__ == "__main__":
    try:
        code = main()
    except Exception as ex:
        echo0(str(ex))
        code = 1
    if code != 0:
        input("Note the error adove and press return to exit.")
    sys.exit(code)
