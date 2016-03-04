'''
Created on 2016/03/04

@author: hirano
'''
from pygameuic.colors import black_color, white_color, dark_gray_color,\
    gray_color
from itertools import chain
import pygame

BACKGROUND_COLOR_KEY = 'background_color'
SELECT_BACKGROUND_COLOR_KEY = 'select_background_color'
BORDER_WIDTHS_KEY = 'border_widths'
BORDER_COLOR_KEY = 'border_color'
TEXT_COLOR_KEY = 'text_color'
SELECT_TEXT_COLOR_KEY = 'select_text_color'
PADDING_KEY = 'padding'
FONT_KEY = 'font'

class Theme(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.styles = {}
        
    def set(self, class_name, key, value):
        self.styles.setdefault(class_name, {})
        self.styles[class_name][key] = value
        
    def get_dict(self, obj, base_name='ObjectRectangle'):
        classes  = []
        klass = obj.__class__
        while True:
            classes.append(klass)
            if klass.__name__ == base_name:
                break
            klass = klass.__bases__[0]
        re_style = {}
        for klass in classes:
            class_name = klass.__name__
            try:
                style = self.styles[class_name]
            except KeyError:
                style = {}
                
            re_style = dict(chain(style.iteritems(), style.iteritems()))
            
        return re_style
        
default_theme = Theme()
current = None

def init_default_theme():
    default_theme.set(class_name='ObjectRectangle',
                      key=BACKGROUND_COLOR_KEY,
                      value=black_color)
    default_theme.set(class_name='ObjectRectangle',
                      key=SELECT_BACKGROUND_COLOR_KEY,
                      value=gray_color)
    default_theme.set(class_name='ObjectRectangle',
                      key=BORDER_WIDTHS_KEY,
                      value=1)
    default_theme.set(class_name='ObjectRectangle',
                      key=BORDER_COLOR_KEY,
                      value=None)
    default_theme.set(class_name='Label',
                    key=TEXT_COLOR_KEY,
                    value=white_color)
    default_theme.set(class_name='Label',
                    key=SELECT_TEXT_COLOR_KEY,
                    value=dark_gray_color)
    default_theme.set(class_name='Label',
                    key=PADDING_KEY,
                    value=(6, 6))
    default_theme.set(class_name='Label',
                    key=BORDER_WIDTHS_KEY,
                    value=None)
    default_theme.set(class_name='Label',
                    key=FONT_KEY,
                    value=pygame.font.SysFont('Courier New', 24))

def use_theme(theme):
    """Make the given theme current.
    There are two included themes: light_theme, dark_theme.
    """
    global current
    current = theme
#     import scene
#     if scene.current is not None:
#         scene.current.stylize()
        
def init():
    init_default_theme()
    use_theme(default_theme)
        