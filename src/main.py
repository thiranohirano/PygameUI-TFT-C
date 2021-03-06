"""
Created on 2016/03/03

@author: hirano
"""
import os
import pygame
import pygameuic as ui  # @UnresolvedImport
import startui
import pifiui
import controllerui
import mytheme

# os.putenv('SDL_FBDEV', '/dev/fb1')
# os.putenv('SDL_MOUSEDRV', 'TSLIB')
# os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

if __name__ == '__main__':
    ui.init('pygameui ', (480, 320))
#     pygame.mouse.set_visible(False)
    mytheme.set_theme()
    ui.append_scene(startui.StartScene())
    ui.append_scene(pifiui.PifiUI())
    ui.append_scene(controllerui.ControllerUI())
    ui.use_scene(0)
    ui.run()