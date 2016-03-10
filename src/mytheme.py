from pygameuic import *  # @UnusedWildImport
from pygameuic.theme import *  # @UnusedWildImport
import mycolors
from pygameuic.colors import *  # @UnusedWildImport

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
                      key=BORDER_COLOR_KEY,
                      value=mycolors.belize_hole)
    
    theme.current.set(class_name=STRING_LIST_VIEW_CLASS,
                      key=BORDER_COLOR_KEY,
                      value=mycolors.belize_hole)
    theme.current.set(class_name=STRING_LIST_VIEW_CLASS,
                      key=BORDER_WIDTHS_KEY,
                      value=3)
    theme.current.set(class_name=STRING_LIST_ITEM_CLASS,
                      key=SELECT_BACKGROUND_COLOR_KEY,
                      value=mycolors.peter_river)
