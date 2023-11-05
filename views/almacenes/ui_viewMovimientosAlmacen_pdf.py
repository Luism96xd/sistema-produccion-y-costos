# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'view_ListaMovimientosAlmacenWvULgR.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import QFont
from PySide6.QtWidgets import *
from utils.tables import TableModel, CustomTable
import os


class ViewReporteMovimientosAlmacen(QDialog):
    def __init__(self, root = None):
        super().__init__()
        self._mainWindow = root

    def setupUi(self, ViewListaTraslados):
        if not ViewListaTraslados.objectName():
            ViewListaTraslados.setObjectName(u"ViewListaTraslados")
        ViewListaTraslados.resize(640, 480)

        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        font.setBold(True)          

        self.verticalLayoutWidget = QWidget(ViewListaTraslados)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 140, 581, 311))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
 
        self.table = CustomTable(self.verticalLayoutWidget)
        self.table.setObjectName(u"table")
        
        self.header = ['ID Traslado', 'Id Producto', 'Almacén Origen', 'Almacén Destino', 'Cantidad', 'Reporte']
        data = self._controller.getTransactionsList()
        self.model = TableModel(data, self.header)

        self.table.setModel(self.model)
        self.verticalLayout.addWidget(self.table)

        self.verticalLayoutWidget_2 = QWidget(ViewListaTraslados)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(450, 30, 160, 83))
        self.buttonGroup = QVBoxLayout(self.verticalLayoutWidget_2)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.setContentsMargins(0, 0, 0, 0)
        self.btn_buscar = QPushButton(self.verticalLayoutWidget_2)
        self.btn_buscar.setObjectName(u"btn_buscar")

        self.buttonGroup.addWidget(self.btn_buscar)

        self.btn_abrir = QPushButton(self.verticalLayoutWidget_2)
        self.btn_abrir.setObjectName(u"btn_abrir")
        self.btn_abrir.clicked.connect(self.open_pdf)
        self.buttonGroup.addWidget(self.btn_abrir)

        self.btn_borrar = QPushButton(self.verticalLayoutWidget_2)
        self.btn_borrar.setObjectName(u"btn_borrar")

        self.buttonGroup.addWidget(self.btn_borrar)

        self.txt_producto = QLineEdit(ViewListaTraslados)
        self.txt_producto.setObjectName(u"txt_producto")
        self.txt_producto.setGeometry(QRect(120, 60, 281, 24))

        self.l_movimiento = QLabel(ViewListaTraslados)
        self.l_movimiento.setObjectName(u"l_movimiento")
        self.l_movimiento.setGeometry(QRect(30, 24, 171, 24))
        self.l_movimiento.setFont(font)

        self.horizontalLayoutWidget = QWidget(ViewListaTraslados)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(230, 100, 171, 31))
        self.tipo_movimiento = QHBoxLayout(self.horizontalLayoutWidget)

        self.tipo_movimiento.setSpacing(6)
        self.tipo_movimiento.setObjectName(u"tipo_movimiento")
        self.tipo_movimiento.setContentsMargins(16, 0, 16, 0)

        self.radio_descargos = QRadioButton(self.horizontalLayoutWidget)
        self.radio_descargos.setObjectName(u"radio_descargos")

        self.tipo_movimiento.addWidget(self.radio_descargos)

        self.radio_cargos = QRadioButton(self.horizontalLayoutWidget)
        self.radio_cargos.setObjectName(u"radio_cargos")

        self.tipo_movimiento.addWidget(self.radio_cargos)

        self.dateEdit = QDateEdit(ViewListaTraslados)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(120, 100, 100, 28))
        self.l_producto = QLabel(ViewListaTraslados)
        self.l_producto.setObjectName(u"l_producto")
        self.l_producto.setGeometry(QRect(30, 60, 91, 24))
        self.l_producto.setFont(font)
        self.l_fecha = QLabel(ViewListaTraslados)
        self.l_fecha.setObjectName(u"l_fecha")
        self.l_fecha.setGeometry(QRect(30, 100, 81, 28))
        self.l_fecha.setFont(font)

        self.retranslateUi(ViewListaTraslados)

        QMetaObject.connectSlotsByName(ViewListaTraslados)
    # setupUi

    def retranslateUi(self, ViewListaTraslados):
        ViewListaTraslados.setWindowTitle(QCoreApplication.translate("ViewListaTraslados", u"Dialog", None))
        self.btn_buscar.setText(QCoreApplication.translate("ViewListaTraslados", u"Buscar", None))
        self.btn_abrir.setText(QCoreApplication.translate("ViewListaTraslados", u"Abrir", None))
        self.btn_borrar.setText(QCoreApplication.translate("ViewListaTraslados", u"Cancelar", None))
        self.l_movimiento.setText(QCoreApplication.translate("ViewListaTraslados", u"Buscar Movimiento:", None))
        self.radio_descargos.setText(QCoreApplication.translate("ViewListaTraslados", u"Descargos", None))
        self.radio_cargos.setText(QCoreApplication.translate("ViewListaTraslados", u"Cargos", None))
        self.l_producto.setText(QCoreApplication.translate("ViewListaTraslados", u"Producto:", None))
        self.l_fecha.setText(QCoreApplication.translate("ViewListaTraslados", u"Fecha:", None))
    # retranslateUi

    def open_pdf(self, clickedIndex):
        selected_row = clickedIndex.row()
        if selected_row:
            path = selected_row[5].text()
            os.startfile(path)

    def assignController(self, controller):
        self._controller = controller
        print(self._controller)
        self.setupUi(self)

    def closeEvent(self, event):
        self._mainWindow.w = None
        
    def mostrarPrincipal(self):
        self._mainWindow.show()
        self.hide()
