from pygameuic import *  # @UnusedWildImport
from pygameuic.theme import BORDER_WIDTHS_KEY, BORDER_COLOR_KEY, BUTTON_CLASS, BACKGROUND_COLOR_KEY, SELECT_BACKGROUND_COLOR_KEY 
import mycolors
from pygameuic.colors import black_color

def set_theme():
    theme.current.set(class_name=BUTTON_CLASS,
                      key=BACKGROUND_COLOR_KEY,
                      value=black_color)
    theme.current.set(class_name=BUTTON_CLASS,
                      key=SELECT_BACKGROUND_COLOR_KEY,
                      value=mycolors.peter_river)
    theme.current.set(class_name=BUTTON_CLASS,
                      key=BORDER_WIDTHS_KEY,
                      value=5)
    theme.current.set(class_name=BUTTON_CLASS,
                      key= BORDER_COLOR_KEY,
                      value=mycolors.belize_hole)
