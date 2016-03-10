import pygame
from pygame.constants import MOUSEBUTTONDOWN, MOUSEBUTTONUP

import window  # @UnresolvedImport
from proccess_spinner import ProccessSpinner  # @UnresolvedImport
from virtualKeyboard import VirtualKeyboard  # @UnresolvedImport
from pygameuic.colors import black_color


stack = []
current = None


def push(scene):
    global current
    stack.append(scene)
    current = scene
    current.all_dirty_item()

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
        self.items = []

    def run(self):
        events = pygame.event.get() 
        if events <> None:
            for e in events:
                if e.type == MOUSEBUTTONDOWN:
                    self._unselectall()
                    pos = pygame.mouse.get_pos()
                    self._selectatmouse(pos)
                    hit_object = self._hit_object(pos)
                    if hit_object is not None:
                        hit_object.mouse_down(pos)
                    self.event_mousedown(pos)
                if e.type == MOUSEBUTTONUP:
                    self._unselectall()
                    pos = pygame.mouse.get_pos()
                    hit_object = self._hit_object(pos)
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
        
    def add_item(self, item):
        assert item is not None
        self.rm_item(item)
        self.items.append(item)
        item.dirty = True
        
    def rm_item(self, child):
        for index, ch in enumerate(self.items):
            if ch == child:
#                 ch.orphaned()
                del self.items[index]
                self.all_dirty_item()
                break;
            
    def all_dirty_item(self):
        self.window_surface.fill(black_color)
        for child in self.items:
            child.dirty = True
        
    def _draw(self):
#         print 'draw'
        draw_flag = False
        for child in self.items:
            if child.draw_blit(self.surface):
                draw_flag = True
                
        return draw_flag
    
    def displayUpdate(self):
        flag = self._draw()
        if flag == True:
            self.window_surface.blit(self.surface,(0,0))
            pygame.display.update()
            print 'update'
        
    def _unselectall(self):
        for child in self.items:
            if child.selected:
                child.selected = False
                child.dirty = True
                
    def _selectatmouse(self, pos):
        for child in self.items:
            if child.rect.collidepoint(pos) and child.enabled:
                child.selected = True
                child.dirty = True
                
    def _hit_object(self, pos):
        for child in self.items:
            if child.rect.collidepoint(pos) and child.enabled:
                return child
        return None