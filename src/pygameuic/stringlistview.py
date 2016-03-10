'''
Created on 2016/03/10

@author: hirano
'''
import pygame
import object_rectangle  # @UnresolvedImport
import callback  # @UnresolvedImport
import label
from pygame.rect import Rect

class StringListView(object_rectangle.ObjectRectangle):
    '''
    classdocs
    '''
    def __init__(self, rect, items):
        '''
        Constructor
        '''
        object_rectangle.ObjectRectangle.__init__(self, rect)
        self.items = []
        self.string_items = items
        self.selected_index = None
        self.on_selected = callback.Signal()
        self.items_surface = pygame.Surface((self.rect.w - self.border_widths * 2, self.rect.h- self.border_widths * 2)).convert()
        
    @property
    def string_items(self):
        return self._string_items
    
    @string_items.setter
    def string_items(self, new_items):
        for item in self.items:
            self.rm_item(item)
            
        self._string_items = new_items
        x = 0
        y = 0
        w, h = self.rect.w,  40
        for item in self._string_items:
            string_list_item = StringListItem(Rect(x, y, w,h), item)
            self.add_item(string_list_item)
            y += h
        self.dirty = True
        
    def add_item(self, item):
        assert item is not None
        self.rm_item(item)
        self.items.append(item)
        
    def rm_item(self, child):
        for index, ch in enumerate(self.items):
            if ch == child:
                del self.items[index]
                break;
            
    def all_dirty_item(self):
        for item in self.items:
            item.dirty = True
        
    def deselect(self):
        if self.selected_index is not None:
            self.items[self.selected_index].selected = False
        self.selected_index = None

    def select(self, index):
        self.deselect()
        self.selected_index = index

        if index is not None:
            item = self.items[self.selected_index]
            item.selected = True
            self.on_selected(self, item, index)
            
    def mouse_down(self,  point):
        for index, item in enumerate(self.items):
            item_rect = Rect(self.rect.x, self.rect.y + item.rect.y, item.rect.w, item.rect.h)
            if item_rect.collidepoint(point):
                self.select(index)
                break
            
    def _draw(self, screen):
        if not object_rectangle.ObjectRectangle._draw(self, screen) :
            return False
        
        self.all_dirty_item()
        self.items_surface.fill(self.background_color)
        for item in self.items:
            item.draw_blit(self.items_surface)
            
        self.surface.blit(self.items_surface,(self.border_widths, self.border_widths))
        return True
    
class StringListItem(label.Label):
    
    def __init__(self, rect, text):
        label.Label.__init__(self, rect, text, halign=label.LEFT)