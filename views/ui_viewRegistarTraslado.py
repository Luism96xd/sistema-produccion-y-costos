# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewMovimientoInventariohXiuoo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QRect, QCoreApplication, QMetaObject, QSize
from PySide6.QtGui import *
from PySide6.QtWidgets import QDialog, QLabel, QLineEdit, QComboBox, QDialogButtonBox
from datetime import datetime
from views.messages import Messages
import qtawesome as qta

class ViewRegistarTraslado(QDialog, Messages):
    def __init__(self, root = None, transact_type=None):
        super().__init__()
        self._mainWindow = root
        self._type = str(transact_type).lower()
        self.selected_product = {'index': None, 'name': None}
        self.selected_origin = {'index': None, 'name': None}
        self.selected_destination = {'index': None, 'name': None}

    def setupUi(self, viewMovimientoInventario):
        if not viewMovimientoInventario.objectName():
            viewMovimientoInventario.setObjectName(u"viewMovimientoInventario")
        viewMovimientoInventario.resize(512, 329)
        
        transfer_icon = qta.icon('mdi6.transfer')
        self.setWindowIcon(transfer_icon)

        self.buttonBox = QDialogButtonBox(viewMovimientoInventario)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(416, 20, 81, 241))
        self.buttonBox.setOrientation(Qt.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.buttonBox.accepted.connect(self.registarTraslado)
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
        self.l_almacen1.setObjectName(u"l_almacen1")
        self.l_almacen1.setGeometry(QRect(24, 115, 190, 32))
        self.l_almacen1.setFont(font)

        self.combo_origen = QComboBox(viewMovimientoInventario)
        self.combo_origen.addItems(['Seleccionar valor...'] + self._controller.getWarehousesNames())
        self.combo_origen.setGeometry(QRect(24, 155, 216, 32))

        self.combo_origen.currentIndexChanged.connect(self.origin_index_changed)
        self.combo_origen.currentTextChanged.connect(self.origin_text_changed)

        self.l_almacen2 = QLabel(viewMovimientoInventario)
        self.l_almacen2.setObjectName(u"l_almacen2")
        self.l_almacen2.setGeometry(QRect(280, 115, 141, 32))
        self.l_almacen2.setFont(font)

        self.combo_destino = QComboBox(viewMovimientoInventario)
        self.combo_destino.addItems(['Seleccionar valor...'] + self._controller.getWarehousesNames())
        self.combo_destino.setGeometry(QRect(280, 155, 216, 32))

        self.combo_destino.currentIndexChanged.connect(self.destination_index_changed)
        self.combo_destino.currentTextChanged.connect(self.destination_text_changed)

        self.l_cantidad = QLabel(viewMovimientoInventario)
        self.l_cantidad.setObjectName(u"l_cantidad")
        self.l_cantidad.setGeometry(QRect(24, 195, 128, 32))
        self.l_cantidad.setFont(font)

        self.txt_cantidad = QLineEdit(viewMovimientoInventario)
        self.txt_cantidad.setObjectName(u"txt_cantidad")
        self.txt_cantidad.setGeometry(QRect(24, 230, 216, 24))

        onlyInteger = QIntValidator()
        self.txt_cantidad.setValidator(onlyInteger)

        self.retranslateUi(viewMovimientoInventario)

        QMetaObject.connectSlotsByName(viewMovimientoInventario)
    # setupUi

    def retranslateUi(self, viewMovimientoInventario):
        viewMovimientoInventario.setWindowTitle(QCoreApplication.translate("viewMovimientoInventario", u"Registrar Traslado", None))
       
        self.l_producto.setText(QCoreApplication.translate("viewMovimientoInventario", u"Nombre del producto:", None))
        self.l_cantidad.setText(QCoreApplication.translate("viewMovimientoInventario", u"Cantidad:", None))
        self.l_almacen1.setText(QCoreApplication.translate("viewMovimientoInventario", u"Almac\u00e9n Origen:", None))
        self.l_almacen2.setText(QCoreApplication.translate("viewMovimientoInventario", u"Almac\u00e9n Destino:", None))
    # retranslateUi
    
    def assignController(self, controller):
        self._controller = controller
        print(self._controller)
        self.setupUi(self)
    
    
    def registarTraslado(self):
        producto     = self.selected_product
        origen       = self.selected_origin
        destino      = self.selected_destination
        cantidad     = int(self.txt_cantidad.text().strip()) if self.txt_cantidad.text() != '' else 0

        productSelected = self.selected_product['index'] != None
        almacen1Selected = self.selected_origin['index'] != None
        almacen2Selected = self.selected_destination['index'] != None

        if (productSelected and almacen1Selected and almacen2Selected and cantidad > 0):
            response = self._controller.register_transfer(producto, origen, destino, cantidad)
            return response

    def product_index_changed(self, i): # i is an int
        print(i)
        self.selected_product['index'] = i

    def product_text_changed(self, s): # s is a str
        print(s)
        self.selected_product['name'] = s

    def origin_index_changed(self, i): # i is an int
        print(i)
        self.selected_origin['index'] = i

    def origin_text_changed(self, s): # s is a str
        print(s)
        self.selected_origin['name'] = s

    def destination_index_changed(self, i): # i is an int
        print(i)
        self.selected_destination['index'] = i

    def destination_text_changed(self, s): # s is a str
        print(s)
        self.selected_destination['name'] = s

    def closeEvent(self, event):
        self._mainWindow.w = None
        
    def mostrarPrincipal(self):
        self._mainWindow.show()
        self.hide()
    
    def closeWindows(self):
        self._mainWindow.w = None
        self.close()