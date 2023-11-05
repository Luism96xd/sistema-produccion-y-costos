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
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QComboBox, QHBoxLayout, QGroupBox
from utils.tables import CustomTable, TableModel
from views.productos.ui_viewEditarProductos import ViewEditarProductos
from controllers.productController import ProductController
from models.product import Product
from views.messages import Messages

class viewListaProductos(QWidget, Messages):
    def __init__(self, root = None):
        super().__init__()
        self.w = None
        self._mainWindow = root
        self.selected_parent = {'index': 0, 'name': 0}

    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(640, 480)

        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        font.setBold(True)

        self.label_nombre = QLabel(Dialog)
        self.label_nombre.setObjectName(u"Consultar Productos")
        self.label_nombre.setGeometry(QRect(32, 16, 576, 24))
        self.label_nombre.setFont(font)

        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 40, 411, 54))
        self.groupBox.setBaseSize(QSize(300, 0))

        self.combo_busqueda = QComboBox(self.groupBox)
        self.combo_busqueda.setObjectName(u"combo_busqueda")
        self.combo_busqueda.setGeometry(QRect(20, 20, 91, 24))
        self.combo_busqueda.addItems(['Nombre', 'Código', 'Marca', 'Modelo'])

        self.txt_busqueda = QLineEdit(self.groupBox)
        self.txt_busqueda.setObjectName(u"txt_busqueda")
        self.txt_busqueda.setGeometry(QRect(120, 20, 281, 24))

        self.l_parent = QLabel(Dialog)
        self.l_parent.setObjectName(u"l_parent")
        self.l_parent.setGeometry(QRect(30, 100, 196, 24))
        self.l_parent.setFont(font)

        self.combo_parent = QComboBox(Dialog)
        self.combo_parent.addItems(['Seleccionar producto...'] + self._controller.getProductNames())
        self.combo_parent.currentIndexChanged.connect(self.index_changed)    
        self.combo_parent.currentTextChanged.connect(self.text_changed)

        self.combo_parent.setGeometry(QRect(30, 132, 196, 24))

        self.btn_buscar = QPushButton(Dialog)
        self.btn_buscar.setObjectName(u"btn_buscar")
        self.btn_buscar.setGeometry(QRect(506, 48, 100, 40))
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
        self.verticalLayoutWidget.setGeometry(QRect(30, 176, 576, 276))

        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        headers = ['Nombre', 'Descripción', 'Cantidad', 'Costo Unitario', 'Costo Total', 'Fecha Ingreso']
        keys = ['nombre_producto', 'descripcion', 'cantidad', 'costo_unitario', 'costo_total', 'fecha_ingreso']

        data = self._controller.getAllProducts()
        self.model = TableModel(data, headers, keys, 'id_subproducto')
            
        self.table = CustomTable(self.verticalLayoutWidget)
        self.table.setObjectName(u"table")
        self.table.setModel(self.model)
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
        self.l_parent.setText(QCoreApplication.translate("Dialog", u"Pertenece a:", None))
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

    def index_changed(self, i): # i is an int
        print(i)
        self.selected_parent['index'] = i

    def text_changed(self, s): # s is a str
        print(s)
        self.selected_parent['name'] = s
    
    def buscarProducto(self):
        parent_index = str(self.combo_parent.currentIndex())
        selected_option = str(self.combo_busqueda.currentText().strip())
        parameter = str(self.txt_busqueda.text().strip())
        parent    = str(self.combo_parent.currentText())
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
                if self.selected_parent['index']  == 0:
                    products = self._controller.getAllProducts()
                    self.updateView(products)
                else:
                    print(parent)
                    self._controller.search_product(parameter, parent)

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