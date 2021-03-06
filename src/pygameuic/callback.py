'''
Created on 2016/03/03

@author: hirano
'''

class Signal(object):
    "A simple signal - slot mechanism"

    # TODO use weak refs? really?

    def __init__(self):
        self.slots = []

    def connect(self, slot):
        "slot: is a function / method"

        assert callable(slot)
        self.slots.append(slot)

    def __call__(self, *args, **kwargs):
        "Fire the signal to connected slots"

        for slot in self.slots:
            slot(*args, **kwargs)
