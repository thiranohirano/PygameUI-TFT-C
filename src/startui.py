'''
Created on 2016/03/03

@author: hirano
'''
import time
import pygame
import mycolors
import pygameuic  as ui  # @UnresolvedImport
import socket
from subprocess import PIPE, Popen
import threading

class StartScene(ui.Scene):

    def __init__(self):
        ui.Scene.__init__(self)
        self.main_frame = ui.ObjectRectangle(ui.window.rect)  # ui.ObjectRectangle(ui.window.rect, mycolors.midnight_blue, None, 10, mycolors.belize_hole)
        self.main_frame.enabled = False
        self.main_frame.border_color = mycolors.belize_hole
        self.main_frame.border_widths = 9
        self.add_child(self.main_frame)
        
        self.ip_label = ui.Label(ui.col_rect(0,0,12,1), self.get_ip())
        self.add_child(self.ip_label)
        
        self.obj_r = ui.Button(ui.col_rect(0, 1, 3, 2), 'Proc')
        self.obj_r.on_clicked.connect(self.hoge)
        self.add_child(self.obj_r)
 
        self.obj_r2 = ui.Button(ui.col_rect(3, 1, 3, 2), 'vkey')
        self.obj_r2.on_clicked.connect(self.hoge2)
        self.add_child(self.obj_r2)
         
        self.obj_r3 = ui.Button(ui.col_rect(6, 1, 3, 2), 'test')
        self.obj_r3.on_clicked.connect(self.hoge3)
        self.add_child(self.obj_r3)
        
        self.obj_r4 = ui.Button(ui.col_rect(9, 1, 3, 2), 'Button')
        self.obj_r4.on_clicked.connect(self.hoge4)
        self.add_child(self.obj_r4)
         
        self.label1 = ui.Label(ui.Rect(10, 230, 100, 30), 'hoge')
#         self.add_child(self.label1

#         self.listview1 = ui.StringListView(ui.col_rect(0, 5, 3,3),["hoge", "hoge2", "hoge3"])
# #         self.listview1.items_font = pygame.font.SysFont('Courier New', 12, bold=True)
#         self.add_child(self.listview1)

        self.reboot_btn = ui.Button(ui.col_rect(0, 6, 3, 2), 'Reboot')
        self.reboot_btn.on_clicked.connect(self.reboot_button_click)
        self.add_child(self.reboot_btn)
        
        self.shutdown_btn = ui.Button(ui.col_rect(9, 6, 3, 2), 'Shutdown')
        self.shutdown_btn.on_clicked.connect(self.shutdown_button_click)
        self.add_child(self.shutdown_btn)
        
    def hoge(self, obj):
        self.show_proccess_spinner(self.search_proccess, 'Scanning for WiFi networks...')
        
    def hoge2(self, obj):
        text = self.show_virtual_keyboard()
        print text
        
    def hoge3(self, obj):
#         self.label1.text = 'hogehoge'
        self.stringlistview1.string_items = ["hoge", "hoge2"]
        
    def hoge4(self, obj):
        ui.use_scene(1)
        
    def reboot_button_click(self, btn):
        ui.quit()
        
    def shutdown_button_click(self, btn):
        threading.Timer(1, self.shutdown_proccess).start()
        ui.quit()
    
    def shutdown_proccess(self):
        self.shutdown()
        
    # Get Your External IP Address
    def get_ip(self):
        ip_msg = "Not connected"
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            s.connect(('<broadcast>', 0))
            ip_msg="IP:" + s.getsockname()[0]
        except Exception:
            pass
        return ip_msg
    
    # Restart Raspberry Pi
    def restart(self):
        command = "/usr/bin/sudo /sbin/shutdown -r now"
        process = Popen(command.split(), stdout=PIPE)
        output = process.communicate()[0]
        return output
    
    def dummyrestart(self):
        time.sleep(1)

# Shutdown Raspberry Pi
    def shutdown(self):
        command = "/usr/bin/sudo /sbin/shutdown -h now"
        process = Popen(command.split(), stdout=PIPE)
        output = process.communicate()[0]
        return output
        
    def search_proccess(self):
        print 'hoge'
        time.sleep(3)
        print 'hoge'
        self.add_child(self.obj_r3)
