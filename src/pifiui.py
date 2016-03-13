'''
Created on 2016/03/07

@author: hirano
'''
import pygame
import pygameuic as ui
import mycolors
import pifi

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
        
        btn = ui.Button(ui.col_rect(9, 7, 2, 1), 'Back')
        btn.on_clicked.connect(self.back)
        self.add_child(btn)
        
        scan_btn = ui.Button(ui.col_rect(1, 7, 2, 1), 'Scan')
        scan_btn.on_clicked.connect(self.scan)
        self.add_child(scan_btn)
        
        scan_label = ui.Label(ui.col_rect(1,0,10,1), 'Select WiFi network...')
        self.add_child(scan_label)
        
        self.ap_listview = ui.StringListView(ui.col_rect(1, 1, 10, 6), [])
        self.ap_listview.items_font = pygame.font.SysFont('Courier New', 20, bold=True)
        self.ap_listview.on_selected.connect(self.ap_selected)
        self.add_child(self.ap_listview)
        
        self.pifi = pifi.PiFi()
        
    def back(self, btn):
        ui.use_scene(0)
        
    def scan(self, btn):
        self.show_proccess_spinner(self.scan_proccess, "Scanning for WiFi networks...")
        
    def scan_proccess(self):
        self.pifi.getWifiAPs()
        aps_list = []
        for ap in self.pifi.aps:
            strength = "H"
            if ap.signal < -80:
                strength = "L"
            elif ap.signal < -60:
                strength = "M"
            aps_list.append(strength+" SSID:" + ap.ssid)
        self.ap_listview.string_items = aps_list
        
    def ap_selected(self, slv, item, index):
        print str(index)
