# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewListaAlmacenessrcWnB.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QRect, QMetaObject, QCoreApplication
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QDialog, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel
from utils.tables import TableModel, CustomTable
from models.almacen import Almacen
from controllers.almacenController import AlmacenController
from views.almacenes.ui_viewEditarAlmacen import ViewEditarAlmacen
from views.messages import Messages
import qtawesome as qta

class viewListaAlmacenes(QDialog, Messages):
    def __init__(self, root = None):
        super().__init__()
        self._mainWindow = root
        self.w = None

    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(640, 480)

        warehouse_icon = qta.icon('mdi6.warehouse')
        self.setWindowIcon(warehouse_icon)

        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        font.setBold(True)

        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 160, 581, 301))

        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        data = self._controller.get_warehouses()

        self.headers = ['ID Almacén', 'Nombre', 'Descripción', 'Ubicación']
        keys = ['id_almacen', 'nombre', 'descripcion', 'ubicacion']
        
        data = self._controller.get_warehouses()
        self.model = TableModel(data, self.headers, keys, 'id_almacen')
        
        self.table = CustomTable(self.verticalLayoutWidget)
        self.table.setObjectName(u"tableView")

        self.table.setModel(self.model)
        self.verticalLayout.addWidget(self.table)

        self.verticalLayoutWidget_2 = QWidget(Dialog)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(450, 30, 160, 83))
        
        self.buttonGroup = QVBoxLayout(self.verticalLayoutWidget_2)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.setContentsMargins(0, 0, 0, 0)
        
        self.btn_buscar = QPushButton(self.verticalLayoutWidget_2)
        self.btn_buscar.setObjectName(u"btn_buscar")
        self.buttonGroup.addWidget(self.btn_buscar)
        self.btn_buscar.clicked.connect(self.buscarAlmacen)

        self.btn_editar = QPushButton(self.verticalLayoutWidget_2)
        self.btn_editar.setObjectName(u"btn_editar")
        self.btn_editar.clicked.connect(self.open_edit_warehouse_window)
        self.buttonGroup.addWidget(self.btn_editar)

        self.btn_borrar = QPushButton(self.verticalLayoutWidget_2)
        self.btn_borrar.setObjectName(u"btn_borrar")
        self.btn_borrar.clicked.connect(self.borrarAlmacen)
        self.buttonGroup.addWidget(self.btn_borrar)

        self.l_nombre = QLabel(Dialog)
        self.l_nombre.setObjectName(u"l_nombre")
        self.l_nombre.setGeometry(QRect(30, 20, 161, 24))
        self.l_nombre.setFont(font)

        self.txt_nombre = QLineEdit(Dialog)
        self.txt_nombre.setObjectName(u"txt_nombre")
        self.txt_nombre.setGeometry(QRect(30, 50, 351, 24))

        self.l_ubicacion = QLabel(Dialog)
        self.l_ubicacion.setObjectName(u"l_ubicacion")
        self.l_ubicacion.setGeometry(QRect(30, 80, 141, 24))
        self.l_ubicacion.setFont(font)

        self.txt_ubicacion = QLineEdit(Dialog)
        self.txt_ubicacion.setObjectName(u"txt_ubicacion")
        self.txt_ubicacion.setGeometry(QRect(30, 110, 351, 24))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Lista de Almacenes", None))
        self.btn_buscar.setText(QCoreApplication.translate("Dialog", u"Buscar", None))
        self.btn_editar.setText(QCoreApplication.translate("Dialog", u"Editar", None))
        self.btn_borrar.setText(QCoreApplication.translate("Dialog", u"Borrar", None))
        self.l_nombre.setText(QCoreApplication.translate("Dialog", u"Nombre del Almac\u00e9n", None))
        self.l_ubicacion.setText(QCoreApplication.translate("Dialog", u"Ubicaci\u00f3n:", None))
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

    def closeWindows(self):
        self.close()
    
    def buscarAlmacen(self):
        name      = str(self.txt_nombre.text().strip())
        location    = str(self.txt_ubicacion.text().strip())
        self._controller.search_warehouse(name, location)

    def updateView(self, data):
        self.table.refresh(data, self.header)

    def open_edit_warehouse_window(self):
        warehouse_id = self.table.getSelectedItem()
        print(warehouse_id)
        if warehouse_id != None:
            if self.w is None:
                model = Almacen()
                self.w = ViewEditarAlmacen(self, warehouse_id)
                self._controller = AlmacenController(self.w, model)
                self.w.assignController(self._controller)
                self.w.show()
            else:
                self.w.close() 
                self.w = None
        self.table.clearSelection()

    def borrarAlmacen(self):
        name   = str(self.txt_nombre.text().strip())
        warehouse_id = self.table.getSelectedItem()
        print(warehouse_id)
        if warehouse_id != None:
            self._controller.delete_warehouse_by_id(warehouse_id)
        else:
            if name != '':
                self._controller.delete_warehouse_by_name(name)