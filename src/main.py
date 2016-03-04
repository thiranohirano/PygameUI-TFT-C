'''
Created on 2016/03/03

@author: hirano
'''
import pygameuic as ui  # @UnresolvedImport
import startui
import mytheme


if __name__ == '__main__':
    ui.init('pygameui ', (480, 320))
    mytheme.set_theme()
    ui.append_scene(startui.StartScene())
    ui.use_scene(0)
    ui.run()