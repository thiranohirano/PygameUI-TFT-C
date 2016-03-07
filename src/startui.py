'''
Created on 2016/03/03

@author: hirano
'''
import time

import mycolors
import pygameuic  as ui  # @UnresolvedImport

class StartScene(ui.Scene):
    def __init__(self):
        ui.Scene.__init__(self)
        self.main_frame = ui.ObjectRectangle(ui.window.rect)#ui.ObjectRectangle(ui.window.rect, mycolors.midnight_blue, None, 10, mycolors.belize_hole)
        self.main_frame.enabled = False
        self.main_frame.border_color = mycolors.belize_hole
        self.main_frame.border_widths = 10
        self.add_child(self.main_frame)
        
        self.obj_r = ui.Button(ui.Rect(10,10, 100,100), 'Proc')
        self.obj_r.on_clicked.connect(self.hoge)
        self.add_child(self.obj_r)
 
        self.obj_r2 = ui.Button(ui.Rect(130,10, 100,100), 'vkey')
        self.obj_r2.on_clicked.connect(self.hoge2)
        self.add_child(self.obj_r2)
         
        self.obj_r3 = ui.Button(ui.Rect(250, 10, 100, 100), 'test')
        self.obj_r3.on_clicked.connect(self.hoge3)
        self.add_child(self.obj_r3)
        
        self.obj_r4 = ui.Button(ui.Rect(370, 10, 100, 100), 'Button')
        self.obj_r4.on_clicked.connect(self.hoge4)
        self.add_child(self.obj_r4)
         
        self.label1 = ui.Label(ui.Rect(10, 230, 100, 30), 'hoge')
        self.add_child(self.label1)
        
    def hoge(self, obj):
        self.show_proccess_spinner(self.search_proccess, 'Scanning for WiFi networks...')
        
    def hoge2(self, obj):
        text = self.show_virtual_keyboard()
        print text
        
    def hoge3(self, obj):
        self.label1.text = 'hogehoge'
        
    def hoge4(self, obj):
        ui.use_scene(1)
        
    def search_proccess(self):
        print 'hoge'
        time.sleep(3)
        print 'hoge'
        self.add_child(self.obj_r3)