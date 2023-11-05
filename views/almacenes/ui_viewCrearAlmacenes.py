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

class viewCrearAlmacen(QDialog, Messages):
    def __init__(self, root, warehouse_id=None):
        super().__init__()
        self.w = None
        self._mainWindow = root
        self.warehouse_id = warehouse_id

    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Almacenes")
        Dialog.resize(489, 388)

        warehouse_icon = qta.icon('mdi6.warehouse')
        self.setWindowIcon(warehouse_icon)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(380, 40, 81, 241))
        self.buttonBox.setOrientation(Qt.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        font.setBold(True)

        self.txt_nombre = QLineEdit(Dialog)
        self.txt_nombre.setObjectName(u"txt_nombre")
        self.txt_nombre.setStyleSheet("border: 2px solid black; border-radius: 3px;")
        self.txt_nombre.setGeometry(QRect(50, 100, 256, 28))

        self.txt_descripcion = QLineEdit(Dialog)
        self.txt_descripcion.setStyleSheet("border: 2px solid black; border-radius: 3px;")
        self.txt_descripcion.setObjectName(u"txt_descripcion")
        self.txt_descripcion.setGeometry(QRect(50, 190, 256, 28))

        self.txt_ubicacion = QLineEdit(Dialog)
        self.txt_ubicacion.setStyleSheet("border: 2px solid black; border-radius: 3px;")
        self.txt_ubicacion.setObjectName(u"txt_ubicacion")
        self.txt_ubicacion.setGeometry(QRect(50, 290, 256, 28))

        self.l_nombre = QLabel(Dialog)
        self.l_nombre.setObjectName(u"l_nombre")
        self.l_nombre.setGeometry(QRect(50, 60, 100, 24))
        self.l_nombre.setFont(font)

        self.l_descripcion = QLabel(Dialog)
        self.l_descripcion.setObjectName(u"l_descripcion")
        self.l_descripcion.setGeometry(QRect(50, 160, 100, 24))
        self.l_descripcion.setFont(font)

        self.l_ubicacion = QLabel(Dialog)
        self.l_ubicacion.setObjectName(u"l_ubicacion")
        self.l_ubicacion.setGeometry(QRect(50, 250, 100, 24))
        self.l_ubicacion.setFont(font)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.createWarehouse)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        if self.warehouse_id != None:
            Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Editar almacén", None))
        else:
            Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Crear un nuevo almacén", None))

        self.l_nombre.setText(QCoreApplication.translate("Dialog", u"Nombre", None))
        self.l_descripcion.setText(QCoreApplication.translate("Dialog", u"Descripci\u00f3n", None))
        self.l_ubicacion.setText(QCoreApplication.translate("Dialog", u"Ubicaci\u00f3n", None))
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
        name        = self.txt_nombre.text().strip()
        description = self.txt_descripcion.text().strip()
        location    = self.txt_ubicacion.text().strip()

        self._controller.create_warehouse(name, description, location)
