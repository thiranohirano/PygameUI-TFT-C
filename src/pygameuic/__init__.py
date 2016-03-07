import pygame

from object_rectangle import *
from label import *
from button import *
from callback import *
from virtualKeyboard import *
from proccess_spinner import *
from scene import Scene  # @UnresolvedImport
import scene  # @UnresolvedImport
import window  # @UnresolvedImport
import theme  # @Reimport @UnresolvedImport

Rect = pygame.Rect
window_surface = None

class SceneManager(object):
    def __init__(self):
        self.scenes = []

    def append_scene(self, scene):
        scene.window_surface = window_surface
        self.scenes.append(scene)
        
    def use_scene(self, index):
        scene.pop()
        scene.push(self.scenes[index])
        scene.current.__class__.__class__.__name__
        
scene_manager = SceneManager()

def init(name=' ', window_size=(480, 320)):
    pygame.init()
    global window_surface
    window_surface = pygame.display.set_mode(window_size)
    pygame.display.set_caption(name)
    window.rect = pygame.Rect((0, 0), window_size)
    theme.init()

def append_scene(_scene):
    global scene_manager
    scene_manager.append_scene(_scene)
    
def use_scene(_index):
    global scene_manager
    scene_manager.use_scene(_index)
    
def run():
    assert len(scene.stack) > 0
    clock = pygame.time.Clock()
    
    while True:
        clock.tick(20)
        scene.current.run()
        scene.current.displayUpdate()
                        