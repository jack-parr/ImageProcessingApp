'''
This file takes user inputs from components on the view, and connects them to the necessary functions in the model and view.
'''

import config
from functools import partial

class MainController:
    
    def __init__(self, model, view):
        self._model = model
        self._view = view
        self._connectSignalsAndSlots()


    def _connectSignalsAndSlots(self):
        pass
        # self._view.menuBtn2.clicked.connect(self._view.changeImageBoxColour)
        # self._view.menuBtn1.clicked.connect(self._view.addToTree)
