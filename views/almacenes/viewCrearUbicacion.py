# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'view_CrearAlmacenesFMQLuI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import Qt, QRect, QCoreApplication, QMetaObject
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QDialogButtonBox, QLabel, QLineEdit, QDialog
from views.messages import Messages
import qtawesome as qta

class viewCrearUbicacion(QDialog, Messages):
    def __init__(self, root, warehouse_id = None):
        super().__init__()
        self.w = None
        self._mainWindow = root
        self.warehouse_id = warehouse_id

    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Ubicaciones")
        Dialog.resize(512, 400)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(380, 40, 81, 241))
        self.buttonBox.setOrientation(Qt.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        font.setBold(True)

        self.l_rack = QLabel(Dialog)
        self.l_rack.setObjectName(u"l_rack")
        self.l_rack.setGeometry(QRect(50, 60, 100, 24))
        self.l_rack.setFont(font)

        self.txt_rack = QLineEdit(Dialog)
        self.txt_rack.setObjectName(u"txt_rack")
        self.txt_rack.setStyleSheet("border: 2px solid black; border-radius: 3px;")
        self.txt_rack.setGeometry(QRect(50, 100, 256, 28))

        self.l_lado = QLabel(Dialog)
        self.l_lado.setObjectName(u"l_lado")
        self.l_lado.setGeometry(QRect(50, 160, 100, 24))
        self.l_lado.setFont(font)

        self.txt_lado = QLineEdit(Dialog)
        self.txt_lado.setStyleSheet("border: 2px solid black; border-radius: 3px;")
        self.txt_lado.setObjectName(u"txt_lado")
        self.txt_lado.setGeometry(QRect(50, 190, 256, 28))
        
        self.l_nivel = QLabel(Dialog)
        self.l_nivel.setObjectName(u"l_nivel")
        self.l_nivel.setGeometry(QRect(50, 250, 100, 24))
        self.l_nivel.setFont(font)

        self.txt_nivel = QLineEdit(Dialog)
        self.txt_nivel.setStyleSheet("border: 2px solid black; border-radius: 3px;")
        self.txt_nivel.setObjectName(u"txt_nivel")
        self.txt_nivel.setGeometry(QRect(50, 290, 256, 28))

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.createWarehouse)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        if self.warehouse_id != None:
            Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Editar ubicación", None))
        else:
            Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Crear nueva ubicación", None))

        self.l_rack.setText(QCoreApplication.translate("Dialog", u"Rack:", None))
        self.l_lado.setText(QCoreApplication.translate("Dialog", u"Lado", None))
        self.l_nivel.setText(QCoreApplication.translate("Dialog", u"Nivel", None))
    # retranslateUi

    def assignController(self, controller):
        self._controller = controller
        print(self._controller)
        self.setupUi(self)

    def closeEvent(self, event):
        self._mainWindow.w = None
        
    def mostrarPrincipal(self):
        self._mainWindow.show()
        self.hide()

    def createWarehouse(self):
        name        = self.txt_rack.text().strip()
        description = self.txt_lado.text().strip()
        location    = self.txt_nivel.text().strip()

        self._controller.create_warehouse(name, description, location)
