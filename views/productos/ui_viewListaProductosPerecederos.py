# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewListaProductosBstFjG.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import Qt, QRect, QMetaObject, QCoreApplication, QSize
from PySide6.QtGui import *
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QLabel, QLineEdit, QComboBox, QHBoxLayout, QGroupBox
from utils.tables import CustomTable, TableModel
from views.productos.ui_viewEditarProductos import ViewEditarProductos
from controllers.productController import ProductController
from models.product import Product
from models.categoria import Categoria
from views.messages import Messages
from datetime import datetime


class ViewListaProductosPerecederos(QWidget, Messages):
    def __init__(self, root = None):
        super().__init__()
        self.w = None
        self._mainWindow = root
        self.selected_parent = {'index': 0, 'name': 0}

    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(688, 480)

        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        font.setBold(True)

        self.label_nombre = QLabel(Dialog)
        self.label_nombre.setObjectName(u"Consultar Productos")
        self.label_nombre.setGeometry(QRect(32, 16, 624, 24))
        self.label_nombre.setFont(font)

        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 40, 624, 64))
        self.groupBox.setBaseSize(QSize(300, 0))

        self.combo_busqueda = QComboBox(self.groupBox)
        self.combo_busqueda.setObjectName(u"combo_busqueda")
        self.combo_busqueda.setGeometry(QRect(20, 20, 91, 30))
        self.combo_busqueda.addItems(['Nombre', 'Código', 'Marca', 'Modelo'])

        self.txt_busqueda = QLineEdit(self.groupBox)
        self.txt_busqueda.setObjectName(u"txt_busqueda")
        self.txt_busqueda.setGeometry(QRect(120, 20, 300, 30))

        self.btn_buscar = QPushButton(Dialog)
        self.btn_buscar.setObjectName(u"btn_buscar")
        self.btn_buscar.setGeometry(QRect(540, 60, 100, 40))
        self.btn_buscar.setBaseSize(QSize(0, 0))
        self.btn_buscar.clicked.connect(self.buscarProducto)

        icon = QIcon()
        icon.addFile(u"./assets/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_buscar.setIcon(icon)
        self.btn_buscar.setIconSize(QSize(16, 16))
        self.btn_buscar.setCheckable(False)
        self.btn_buscar.setFlat(False)

        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 124, 624, 340))

        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        #headers = ['Categoría', 'Nombre', 'Cantidad', 'Fecha Ingreso', 'Vida Útil', 'Estatus']
        #keys = ['categoria_producto', 'nombre_producto', 'cantidad', 'fecha_ingreso', 'vida_util', 'estatus']

        self.table = QTableWidget()
        self.table.resizeColumnsToContents()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(['Categoría', 'Producto', 'Descripción', 'Fecha de Ingreso', 'Vida Útil (días)', 'Estatus'])

        products = Product.get_all()
        products.sort(key=lambda x: x.get('fecha_ingreso'))

        for i, product in enumerate(products):
            nombre = product.get('nombre_producto')
            descripcion = product.get('descripcion')
            fecha_ingreso = product.get('fecha_ingreso').strftime('%Y-%m-%d')
            vida_util = product.get('vida_util')
            id_categoria = product.get('id_categoria')
            print(f"id_categoria {id_categoria}")
            categoria = Categoria.get_name_by_id(id_categoria)
            
            print(f"categoria {categoria}")
            # Calculate the difference between the expiration date and today's date
            days_diff = abs((product.get('fecha_ingreso') - datetime.today()).days)

            # Set the color of the status cell based on the difference
            status_item = QTableWidgetItem()
            print(vida_util)
            print(days_diff)
            if days_diff >= vida_util:
                status_item.setBackground(QColor('red'))
                status_item.setText('Expired')
            elif days_diff >= (vida_util / 2) and days_diff < vida_util:
                status_item.setBackground(QColor('yellow'))
                status_item.setText('Near')
            else:
                status_item.setText('OK')

            # Add the items to the table
            self.table.insertRow(i)
            self.table.setItem(i, 0, QTableWidgetItem(categoria))
            self.table.setItem(i, 1, QTableWidgetItem(nombre))
            self.table.setItem(i, 2, QTableWidgetItem(descripcion))
            self.table.setItem(i, 3, QTableWidgetItem(fecha_ingreso))
            self.table.setItem(i, 4, QTableWidgetItem(str(vida_util)))
            self.table.setItem(i, 5, status_item)
        self.verticalLayout.addWidget(self.table)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.btn_editar = QPushButton(self.verticalLayoutWidget)
        self.btn_editar.setObjectName(u"btn_editar")
        self.btn_editar.clicked.connect(self.open_edit_product_window)
        self.horizontalLayout_2.addWidget(self.btn_editar)

        self.btn_borrar = QPushButton(self.verticalLayoutWidget)
        self.btn_borrar.setObjectName(u"btn_borrar")
        self.btn_borrar.clicked.connect(self.borrarProducto)
        self.horizontalLayout_2.addWidget(self.btn_borrar)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Lista de Productos", None))
        self.btn_buscar.setText(QCoreApplication.translate("Dialog", u"Buscar", None))
        self.btn_editar.setText(QCoreApplication.translate("Dialog", u"Editar", None))
        self.btn_borrar.setText(QCoreApplication.translate("Dialog", u"Borrar", None))
        self.label_nombre.setText(QCoreApplication.translate("Dialog", u"Buscar Producto:", None))
        self.btn_buscar.setText(QCoreApplication.translate("Dialog", u"Buscar", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Criterios de b\u00fasqueda", None))
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

    def buscarProducto(self):
        selected_option = str(self.combo_busqueda.currentText().strip())
        parameter = str(self.txt_busqueda.text().strip())
        if selected_option == '':
            print('Debes seleccionar una opción')
        else:
            if parameter != '':
                if selected_option == 'Nombre':
                    self._controller.search_product_by_name(parameter)
                elif selected_option == 'Código':
                    self._controller.search_product_by_code(parameter)
                elif selected_option == 'Marca':
                    self._controller.search_product_by_mark(parameter)
                elif selected_option == 'Modelo':
                    self._controller.search_product_by_model(parameter)
            else:
                products = self._controller.getAllProducts()
            
            self.updateView(products)

    def borrarProducto(self):
        name   = str(self.txt_busqueda.text().strip())
        parent = str(self.combo_parent.currentText())
        product_id = self.table.getSelectedItem()
        print(product_id)
        if product_id != None:
            self._controller.delete_product_by_id(product_id)
        else:
            if name != '':
                self._controller.delete_product_by_name(name)
        
    def updateView(self, data):
        self.table.refresh(data, self.header)

    def open_edit_product_window(self):
        product_id = self.table.getSelectedItem()
        print(product_id)
        if product_id != None:
            if self.w is None:
                model = Product()
                self.w = ViewEditarProductos(self, product_id)
                self._controller = ProductController(self.w, model)
                self.w.assignController(self._controller)
                self.w.show()
            else:
                self.w.close() 
                self.w = None
        self.table.clearSelection()