'''
Created on 2016/03/07

@author: hirano
'''
import pygameuic as ui
import mycolors
class PifiUI(ui.Scene):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        ui.Scene.__init__(self)
        self.main_frame = ui.ObjectRectangle(ui.window.rect)
        self.main_frame.enabled = False
        self.main_frame.border_color = mycolors.belize_hole
        self.main_frame.border_widths = 9
        self.add_child(self.main_frame)
        
        btn = ui.Button(ui.col_rect(9, 7, 2, 1), 'back')
        btn.on_clicked.connect(self.back)
        self.add_child(btn)
        
        scan_btn = ui.Button(ui.col_rect(1, 7, 2, 1), 'scan')
        scan_btn.on_clicked.connect(self.scan)
        self.add_child(scan_btn)
        
        scan_label = ui.Label(ui.col_rect(1,0,10,1), 'Select WiFi network...')
        self.add_child(scan_label)
        
        self.ap_listview = ui.StringListView(ui.col_rect(2, 1, 8, 6), [])
        self.add_child(self.ap_listview)
        
    def back(self, btn):
        ui.use_scene(0)
        
    def scan(self, btn):
        pass
