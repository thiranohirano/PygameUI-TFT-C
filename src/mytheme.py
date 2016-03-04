from pygameuic import *  # @UnusedWildImport
from pygameuic.theme import BORDER_WIDTHS_KEY, BORDER_COLOR_KEY
import mycolors

def set_theme():
    theme.current.set(class_name='ObjectRectangle',
                      key=BORDER_WIDTHS_KEY,
                      value=5)
    theme.current.set(class_name='ObjectRectangle',
                      key= BORDER_COLOR_KEY,
                      value=mycolors.belize_hole)
