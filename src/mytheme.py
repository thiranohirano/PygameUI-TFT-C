from pygameuic import *  # @UnusedWildImport
from pygameuic.theme import *  # @UnusedWildImport
import mycolors
from pygameuic.colors import *  # @UnusedWildImport

def set_theme():
    myfontsize = int((window.rect.w / 12 + 0.5 - 2) / 2)
    myfont = pygame.font.Font(resource.get_font_path("VL-PGothic-Regular"), myfontsize)#pygame.font.SysFont('Courier New', myfontsize)
    myfont_bold = pygame.font.Font(resource.get_font_path("VL-PGothic-Regular"), myfontsize, bold=True)#pygame.font.SysFont('Courier New', myfontsize, bold=True)
    fsize = int(window.rect.height / 12 + 0.5)
    mytxtfont = pygame.font.Font(resource.get_font_path("VL-PGothic-Regular"), fsize)
    theme.current.set(class_name=LABEL_CLASS,
                      key=FONT_KEY,
                      value=myfont)

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
    theme.current.set(class_name=BUTTON_CLASS,
                      key=FONT_KEY,
                      value=myfont_bold)

    theme.current.set(class_name=STRING_LIST_VIEW_CLASS,
                      key=BORDER_COLOR_KEY,
                      value=mycolors.belize_hole)
    theme.current.set(class_name=STRING_LIST_VIEW_CLASS,
                      key=BORDER_WIDTHS_KEY,
                      value=3)
    theme.current.set(class_name=STRING_LIST_ITEM_CLASS,
                      key=SELECT_BACKGROUND_COLOR_KEY,
                      value=mycolors.peter_river)
    theme.current.set(class_name=STRING_LIST_ITEM_CLASS,
                      key=FONT_KEY,
                      value=myfont_bold)
    theme.current.set(class_name=PROCESS_SPINNER_CLASS,
                      key=FONT_KEY,
                      value=myfont_bold)
    theme.current.set(class_name=VIRTUAL_KEYBOARD_CLASS,
                      key=FONT_KEY,
                      value=myfont_bold)
    # theme.current.set(class_name=VIRTUAL_KEYBOARD_CLASS,
    #                   key=TEXT_FONT_KEY,
    #                   value=mytxtfont)
