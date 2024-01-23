import config
from functools import partial

class MainController:
    # this is the controller class.
    def __init__(self, model, view):
        self._view = view
        self._connectSignalsAndSlots()

    def _connectSignalsAndSlots(self):
        self._view.menuBtn1.clicked.connect(self._view._changeImageBoxColour)

