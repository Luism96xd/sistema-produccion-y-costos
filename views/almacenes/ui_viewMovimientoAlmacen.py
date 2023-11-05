# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewMovimientoInventariohXiuoo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QRect, QCoreApplication, QMetaObject
from PySide6.QtGui import *
from PySide6.QtWidgets import QDialog, QLabel, QLineEdit, QComboBox, QDialogButtonBox
from datetime import datetime
from views.messages import Messages

class ViewMovimientoAlmacen(QDialog, Messages):
    def __init__(self, root = None, transact_type=None):
        super().__init__()
        self._mainWindow = root
        self._type = str(transact_type).lower()
        self.selected_product = {'index': None, 'name': None}
        self.selected_warehouse = {'index': None, 'name': None}

    def setupUi(self, viewMovimientoInventario):
        if not viewMovimientoInventario.objectName():
            viewMovimientoInventario.setObjectName(u"viewMovimientoInventario")
        viewMovimientoInventario.resize(512, 329)

        self.buttonBox = QDialogButtonBox(viewMovimientoInventario)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(416, 20, 81, 241))
        self.buttonBox.setOrientation(Qt.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.buttonBox.accepted.connect(self.registarMovimiento)
        self.buttonBox.rejected.connect(self.closeWindows)

        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        font.setBold(True)
        
        self.l_producto = QLabel(viewMovimientoInventario)
        self.l_producto.setObjectName(u"l_producto")
        self.l_producto.setGeometry(QRect(24, 40, 200, 32))
        self.l_producto.setFont(font)

        self.combo_producto = QComboBox(viewMovimientoInventario)
        self.combo_producto.setObjectName(u"combo_producto")
        self.combo_producto.addItems(['Seleccionar valor...'] + self._controller.getProductNames())
        self.combo_producto.setGeometry(QRect(24, 75, 216, 32))
        
        self.combo_producto.currentIndexChanged.connect(self.product_index_changed)
        self.combo_producto.currentTextChanged.connect(self.product_text_changed)

        self.l_almacen1 = QLabel(viewMovimientoInventario)
        self.l_almacen1.setObjectName(u"l_almacen")
        self.l_almacen1.setGeometry(QRect(24, 115, 190, 32))
        self.l_almacen1.setFont(font)

        self.combo_origen = QComboBox(viewMovimientoInventario)
        self.combo_origen.addItems(['Seleccionar valor...'] + self._controller.getWarehousesNames())
        self.combo_origen.setGeometry(QRect(24, 155, 216, 32))

        self.combo_origen.currentIndexChanged.connect(self.warehouse_index_changed)
        self.combo_origen.currentTextChanged.connect(self.warehouse_text_changed)

        self.l_cantidad = QLabel(viewMovimientoInventario)
        self.l_cantidad.setObjectName(u"l_cantidad")
        self.l_cantidad.setGeometry(QRect(24, 195, 128, 32))
        self.l_cantidad.setFont(font)

        self.txt_cantidad = QLineEdit(viewMovimientoInventario)
        self.txt_cantidad.setObjectName(u"txt_cantidad")
        self.txt_cantidad.setGeometry(QRect(24, 230, 216, 24))

        self.l_tipo = QLabel(viewMovimientoInventario)
        self.l_tipo.setObjectName(u"l_tipo")
        self.l_tipo.setGeometry(QRect(24, 260, 141, 32))
        self.l_tipo.setFont(font)

        onlyInteger = QIntValidator()
        self.txt_cantidad.setValidator(onlyInteger)

        self.retranslateUi(viewMovimientoInventario)

        QMetaObject.connectSlotsByName(viewMovimientoInventario)
    # setupUi

    def retranslateUi(self, viewMovimientoInventario):
        if self._type == 'cargo':
            viewMovimientoInventario.setWindowTitle(QCoreApplication.translate("viewMovimientoInventario", u"Registrar cargo de inventario", None))
        elif self._type == 'descargo':
             viewMovimientoInventario.setWindowTitle(QCoreApplication.translate("viewMovimientoInventario", u"Registrar descargo de inventario", None))
       
        self.l_producto.setText(QCoreApplication.translate("viewMovimientoInventario", u"Nombre del producto:", None))
        self.l_cantidad.setText(QCoreApplication.translate("viewMovimientoInventario", u"Cantidad:", None))
        self.l_almacen1.setText(QCoreApplication.translate("viewMovimientoInventario", u"Almac\u00e9n:", None))
        self.l_tipo.setText(QCoreApplication.translate("viewMovimientoInventario", u"Tipo: " + self._type.capitalize(), None))
    # retranslateUi
    
    def assignController(self, controller):
        self._controller = controller
        print(self._controller)
        self.setupUi(self)
    
    def registarMovimiento(self):
        producto     = self.selected_product
        almacen      = self.selected_warehouse
        cantidad     = int(self.txt_cantidad.text().strip()) if self.txt_cantidad.text() != '' else 0

        productSelected = self.selected_product['index'] != None
        warehouseSelected = self.selected_warehouse['index'] != None

        if (productSelected and warehouseSelected and cantidad > 0):
            if (self._type == "cargo"):
                response = self._controller.register_load(producto, almacen, cantidad)
            else:
                response = self._controller.register_unload(producto, almacen, cantidad)
            return response

    def product_index_changed(self, i): # i is an int
        print(i)
        self.selected_product['index'] = i

    def product_text_changed(self, s): # s is a str
        print(s)
        self.selected_product['name'] = s

    def warehouse_index_changed(self, i): # i is an int
        print(i)
        self.selected_warehouse['index'] = i

    def warehouse_text_changed(self, s): # s is a str
        print(s)
        self.selected_warehouse['name'] = s

    def closeEvent(self, event):
        self._mainWindow.w = None
        
    def mostrarPrincipal(self):
        self._mainWindow.show()
        self.hide()
    
    def closeWindows(self):
        self._mainWindow.w = None
        self.close()
