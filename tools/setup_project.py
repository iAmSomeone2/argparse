#!/usr/bin/env python3
"""

"""

from enum import Enum

_VERSION_FILE = "VERSION.txt"
"""
Name of file to read version info from
...
This is the file name only. It is not a full path.
"""

class _ConfigSys(Enum):
    """
    Enumeration of supported configuration systems
    """
    CMAKE
    MESON

def _set_up_meson():
    """
    Set up the project using the Meson configuration system.
    """

if __name__ == "__main__":
    print("hello")