'''
Created on 2016/03/07

@author: hirano
'''
import pygameuic as ui
class PifiUI(ui.Scene):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        ui.Scene.__init__(self)
        
        btn = ui.Button(ui.Rect(10, 10, 100, 30), 'back')
        btn.on_clicked.connect(self.back)
        self.add_item(btn)
        
    def back(self, btn):
        ui.use_scene(0)
