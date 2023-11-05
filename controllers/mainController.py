
import sys
from views.ui_viewMain import MainWindow
from PySide6.QtWidgets import QApplication

class MainController(object):
    def __init__(self, model, view):
        self._view = view
        self._model = model

