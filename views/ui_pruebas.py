from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
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

class ExampleWindow(QWidget):
    def __init__(self):

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

        layout = QVBoxLayout()

        for w in widgets:
            layout.addWidget(w())

        widget = QCheckBox()
        widget.setCheckState(Qt.Checked)

        # For tristate: widget.setCheckState(Qt.PartiallyChecked)
        # Or: widget.setTriState(True)
        widget.stateChanged.connect(self.show_state)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)
    
    def show_state(self, s):
        print(s == Qt.Checked)
        print(s)

    def select_option(self):
        if self.excelente.isChecked():
            nivel_satisfaccion = 3
        elif self.bueno.isChecked():
            nivel_satisfaccion = 2
        elif self.regular.isChecked():
            nivel_satisfaccion = 1
        elif self.malo.isChecked():
            nivel_satisfaccion = 0
        return nivel_satisfaccion

        #self.fecha.setDate(QDate.currentDate())
        #self.fecha.date().toPyDate()
        #icon = qta.icon("ei.bell", color="#fd0")