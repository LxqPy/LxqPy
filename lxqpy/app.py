#!/bin/python3

'''

    This is the starting point of LxqPy. So LxqPy
    is supposed to be a window manager for X Window
    System, and a Wayland Compositor for Wayland. Pretty
    much a clone of LxqPy.

    This software needs Python-Xlib and PyWayland. I don't
    like XCFFIB because it is not well documented.

    So far this version supports Python 3.9.6, but yeah
    that's all I can say :) . NOTE : NO SUPPORT FOR PYPY,
    ............ yet .

'''

# Import stuff , you know.

# Atleast the contributor knows who are we ....

__name__    = "LxqPy"
__version__ = "0.1.0 Pre-Alpha 1"
__author__  = "LxqPy Team"

# Start of the scripts.

from libs.display.display_init import test

test()

