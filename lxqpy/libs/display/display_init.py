'''

    This is used for initializing display.

'''

# Import shit.

from Xlib.display import Display

def test():

    display = Display()

    name = display.get_display_name()

    print(name)