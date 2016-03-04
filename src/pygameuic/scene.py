import pygame
from pygame.constants import MOUSEBUTTONDOWN, MOUSEBUTTONUP

import window  # @UnresolvedImport
from proccess_spinner import ProccessSpinner  # @UnresolvedImport
from virtualKeyboard import VirtualKeyboard  # @UnresolvedImport


stack = []
current = None


def push(scene):
    global current
    stack.append(scene)
    current = scene


def pop():
    global current

    if len(stack) > 0:
        stack.pop()

    if len(stack) > 0:
        current = stack[-1]

class Scene(object):
    """A view that takes up the entire window content area."""

    def __init__(self):
        self.window_surface = None
        self.surface = pygame.Surface(window.rect.size, pygame.SRCALPHA, 32)
        self.children = []

    def run(self):
#         print 'run()'
        events = pygame.event.get() 
        if events <> None:
            for e in events:
                if e.type == MOUSEBUTTONDOWN:
                    self.unselectall()
                    pos = pygame.mouse.get_pos()
                    self.selectatmouse(pos)
                    hit_object = self.hit_object(pos)
                    if hit_object is not None:
                        hit_object.mouse_down(pos)
                    self.event_mousedown(pos)
                if e.type == MOUSEBUTTONUP:
                    self.unselectall()
                    pos = pygame.mouse.get_pos()
                    hit_object = self.hit_object(pos)
                    if hit_object is not None:
                        hit_object.mouse_up(pos)
                    self.event_mouseup(pos)
                if e.type == pygame.QUIT:
                    pygame.quit()
                    import  sys
                    sys.exit()
        
    def event_mousedown(self, pos):
        pass
    
    def event_mouseup(self, pos):
        pass
    
    def show_proccess_spinner(self, slot, title=''):
        ps = ProccessSpinner(self.window_surface)
        ps.run(slot, title)
        
    def show_virtual_keyboard(self, text=''):
        vk = VirtualKeyboard(self.window_surface)
        return vk.run(text)
        
    def add_child(self, child):
        assert child is not None
        self.rm_child(child)
        self.children.append(child)
        child.dirty = True
        
    def rm_child(self, child):
        for index, ch in enumerate(self.children):
            if ch == child:
#                 ch.orphaned()
                del self.children[index]
                self.all_dirty_child()
                break;
            
    def all_dirty_child(self):
        for child in self.children:
            child.dirty = True
        
    def draw(self):
#         print 'draw'
        for child in self.children:
            child.draw_blit(self.surface)
    
    def displayUpdate(self):
        self.draw()
        self.window_surface.blit(self.surface,(0,0))
        pygame.display.update()
        
    def unselectall(self):
        for child in self.children:
            if child.selected:
                child.selected = False
                child.dirty = True
                
    def selectatmouse(self, pos):
        for child in self.children:
            if child.rect.collidepoint(pos) and child.enabled:
                child.selected = True
                child.dirty = True
                
    def hit_object(self, pos):
        for child in self.children:
            if child.rect.collidepoint(pos) and child.enabled:
                return child
        return None