# -*- coding: utf-8 -*-
import time

import pygameuic as ui
import mycolors
import socket

class ControllerUI(ui.Scene):

    def __init__(self):
        ui.Scene.__init__(self)
        self.addr = None
        self.connect_flg = False
        self.tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.main_frame = ui.ObjectRectangle(
            ui.window.rect)  # ui.ObjectRectangle(ui.window.rect, mycolors.midnight_blue, None, 10, mycolors.belize_hole)
        self.main_frame.enabled = False
        self.main_frame.border_color = mycolors.belize_hole
        self.main_frame.border_widths = 9
        self.add_child(self.main_frame)

        btn = ui.Button(ui.col_rect(9, 7, 2, 1), 'Back')
        btn.on_clicked.connect(self.back)
        self.add_child(btn)

        self.ip_label = ui.Label(ui.col_rect(0, 0, 9, 2), '')
        self.add_child(self.ip_label)

        self.connect_btn = ui.Button(ui.col_rect(9, 0, 3, 1), 'Connect')
        self.connect_btn.on_clicked.connect(self.connect_tcp)
        self.add_child(self.connect_btn)

        self.close_btn = ui.Button(ui.col_rect(9, 1, 3, 1), 'Close')
        self.close_btn.on_clicked.connect(self.close_tcp)
        #self.add_child(self.close_btn)

        self.forward_btn = ui.Button(ui.col_rect(4, 2, 4, 2), 'FW')
        self.forward_btn.on_clicked.connect(self.send_forward)

        self.left_btn = ui.Button(ui.col_rect(0, 4, 4, 2), 'LT')
        self.left_btn.on_clicked.connect(self.send_left)

        self.brake_btn = ui.Button(ui.col_rect(4, 4, 4, 2), 'Brake')
        self.brake_btn.on_clicked.connect(self.send_brake)

        self.right_btn = ui.Button(ui.col_rect(8, 4, 4, 2), 'RT')
        self.right_btn.on_clicked.connect(self.send_right)

        self.back_btn = ui.Button(ui.col_rect(4, 6, 4, 2), 'BW')
        self.back_btn.on_clicked.connect(self.send_backward)

    def back(self, btn):
        ui.use_scene(0)

    def connect_tcp(self, btn):
        try:
            host = self.show_virtual_keyboard()
            port = int(self.show_virtual_keyboard())
            self.addr = (host, port)
            self.show_process_spinner(self.connecting, host+":"+str(port)+ " Connecting...")
            if not self.connect_flg:
                raise socket.error
            print 'connect!'
            self.ip_label.text = host+":"+str(port)
            self.show_connect_close(True)
        except:
            self.connect_flg = False
            print 'Dont connect'
    def connecting(self):
        try:
            self.tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.tcpCliSock.connect(self.addr)
            self.connect_flg = True
        except:
            self.connect_flg = False
        time.sleep(1)

    def close_tcp(self, btn):
        self.tcpCliSock.close()
        self.ip_label.text = ''
        self.show_connect_close(False)

    def send_forward(self, btn):
        self.tcpCliSock.send("Forward")

    def send_backward(self, btn):
        self.tcpCliSock.send("Backward")

    def send_left(self, btn):
        self.tcpCliSock.send("Left")

    def send_right(self, btn):
        self.tcpCliSock.send("Right")

    def send_brake(self, btn):
        self.tcpCliSock.send("Brake")

    def show_connect_close(self, flg):
        if flg:
            self.rm_child(self.connect_btn)
            self.add_child(self.close_btn)
            self.add_child(self.forward_btn)
            self.add_child(self.left_btn)
            self.add_child(self.brake_btn)
            self.add_child(self.right_btn)
            self.add_child(self.back_btn)
        else:
            self.add_child(self.connect_btn)
            self.rm_child(self.close_btn)
            self.rm_child(self.forward_btn)
            self.rm_child(self.left_btn)
            self.rm_child(self.brake_btn)
            self.rm_child(self.right_btn)
            self.rm_child(self.back_btn)