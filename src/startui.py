'''
Created on 2016/03/03

@author: hirano
'''
import time

import mycolors
import pygameuic  as ui  # @UnresolvedImport
from pygameuic.colors import black_color


class StartScene(ui.Scene):
    def __init__(self):
        ui.Scene.__init__(self)
        self.main_frame = ui.ObjectRectangle(ui.window.rect)#ui.ObjectRectangle(ui.window.rect, mycolors.midnight_blue, None, 10, mycolors.belize_hole)
        self.main_frame.enabled = False
        self.main_frame.border_widths = 10
        self.add_child(self.main_frame)
        
        self.children.append(self.main_frame)
        self.obj_r = ui.ObjectRectangle(ui.Rect(10,10, 100,100))
        self.obj_r.select_background_color = mycolors.peter_river
        self.obj_r.on_mouse_up.connect(self.hoge)
        self.add_child(self.obj_r)

        self.obj_r2 = ui.ObjectRectangle(ui.Rect(130,10, 100,100))
        self.obj_r2.select_background_color = mycolors.peter_river
        self.obj_r2.on_mouse_up.connect(self.hoge2)
        self.add_child(self.obj_r2)
        
        self.obj_r3 = ui.Label(ui.Rect(250, 10, 100, 100), 'test')
        self.obj_r3.select_background_color = mycolors.peter_river
        self.obj_r3.enabled = True
        self.obj_r3.on_mouse_up.connect(self.hoge3)
        self.add_child(self.obj_r3)
        
        self.label1 = ui.Label(ui.Rect(10, 230, 100, 30), 'hoge')
        self.add_child(self.label1)
        
    def run(self):
        ui.Scene.run(self)
        ui.Scene.displayUpdate(self)
        
    def event_mousedown(self, pos):
        ui.Scene.event_mousedown(self, pos)
        
    def event_mouseup(self, pos):
        ui.Scene.event_mouseup(self, pos)
        
    def draw(self):
        ui.Scene.draw(self)
        
    def hoge(self, obj, pos):
        self.show_proccess_spinner(self.search_proccess, 'Scanning for WiFi networks...')
        
    def hoge2(self, obj, pos):
        text = self.show_virtual_keyboard()
        print text
        
    def hoge3(self, obj ,pos):
        self.rm_child(self.obj_r3)
        
    def search_proccess(self):
        print 'hoge'
        time.sleep(3)
        print 'hoge'
        self.add_child(self.obj_r3)