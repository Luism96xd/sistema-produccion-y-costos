from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
    QMenu
)

class Validator():  
    def __init__(self, view):
        self.view = view

    def Validate(self):
        widgets = [
            QCheckBox,
            QComboBox,
            QDateEdit,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLCDNumber,
            QLabel,
            QLineEdit,
            QProgressBar,
            QPushButton,
            QRadioButton,
            QSlider,
            QSpinBox,
            QTimeEdit,
        ]
        self.elements = [w for w in (dir(self.view) and widgets)]
        for widget in dir(self.view):
            if widget.text() == '' or widget.text() == None:
                print(f'{widget} value is null')

from views.ui_viewAgregarProductos import viewAgregarProductos

v = Validator(viewAgregarProductos)
v.Validate()
            
