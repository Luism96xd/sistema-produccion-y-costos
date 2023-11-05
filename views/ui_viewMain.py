# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewMainWindowyMZTBD.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from models.product import Product
from controllers.productController import ProductController
from views.productos.ui_viewAgregarProductos import viewAgregarProductos
from reportes.export_products_excel import exportar_excel_productos
from utils.tables import CustomTable, TableModel
from menu import Menu
import qtawesome as qta

from PySide6.QtCore import QSize, Qt, QMetaObject, QCoreApplication, QRect
from PySide6.QtGui import QAction, QIcon, QCursor
from PySide6.QtWidgets import (
    QLabel,
    QLineEdit,
    QStatusBar,
    QMainWindow,
    QComboBox,
    QGroupBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QMenu
)
class MainWindow(QMainWindow):
    def __init__(self, parent = None, empresa = None):
        super().__init__(parent)
        self.w = None
        self.controller = None
        self.parent = parent
        self.empresa = empresa
        self.setWindowFlag(Qt.Window)

        home_icon = qta.icon('fa.home')
        self.setWindowIcon(home_icon)

        self.setWindowTitle("My App")
        self.setMinimumSize(QSize(800, 520))
        self.setupUi(self)
    
    #The view class should define the button and setup its event response. 
    #The button click event should call the controller that the view has a reference to.

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        self.centralWidget = QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralWidget)

        self.btn_agregar = QPushButton(self.centralWidget)
        self.btn_agregar.setObjectName(u"btn_agregar")
        self.btn_agregar.setGeometry(QRect(20, 38, 180, 40))
        self.btn_agregar.setStyleSheet("background: #0077ee; border: 2px solid #222; font-family:'Arial'; font-size: 14px; font-weight: 700; color: white; height: 32px;")
        self.btn_agregar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_agregar.clicked.connect(self.show_add_products_window)

        self.groupBox = QGroupBox(self.centralWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(220, 28, 440, 54))
        self.groupBox.setBaseSize(QSize(300, 0))

        self.combo_busqueda = QComboBox(self.groupBox)
        self.combo_busqueda.setObjectName(u"combo_busqueda")
        self.combo_busqueda.setGeometry(QRect(32, 20, 100, 24))
        self.combo_busqueda.addItems(['Código', 'Nombre', 'Marca', 'Modelo'])

        self.txt_busqueda = QLineEdit(self.groupBox)
        self.txt_busqueda.setObjectName(u"txt_busqueda")
        self.txt_busqueda.setGeometry(QRect(150, 20, 281, 24))

        self.btn_buscar = QPushButton(self.centralWidget)
        self.btn_buscar.setObjectName(u"btn_buscar")
        self.btn_buscar.setGeometry(QRect(680, 38, 100, 40))
        self.btn_buscar.setBaseSize(QSize(0, 0))
        self.btn_buscar.clicked.connect(self.buscarProducto)

        icon = QIcon()
        icon.addFile(u"./assets/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_buscar.setIcon(icon)
        self.btn_buscar.setIconSize(QSize(16, 16))
        self.btn_buscar.setCheckable(False)
        self.btn_buscar.setFlat(False)
        
        self.verticalLayoutWidget = QWidget(self.centralWidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(32, 96, 740, 400))

        layout = QVBoxLayout(self.verticalLayoutWidget)
        #self.button1 = QPushButton("Agregar Producto")
        #self.button1.setStyleSheet("background: #0077ee; border: 2px solid #222; height: 32px")
        #self.button1.clicked.connect(self.show_add_products_window)
        
        self.controller = ProductController(self)
        data = self.controller.getAllProducts()
        self.headers = ['Nombre', 'Descripción', 'Cantidad', 'Costo Unitario', 'Costo Total', 'Fecha Ingreso']
        keys = ['nombre_producto', 'descripcion', 'cantidad', 'costo_unitario', 'costo_total', 'fecha_ingreso']

        self.table = CustomTable(self)
        self.model = TableModel(data, self.headers, keys, 'id_subproducto')
        self.table.setModel(self.model)

        self.label = QLabel()
        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        self.btn_exportar_excel = QPushButton(self.centralWidget)
        self.btn_exportar_excel.setObjectName(u"btn_exportar_excel")
        self.btn_exportar_excel.setStyleSheet("background: #111111; color:white; border: 2px solid #222; height: 32px")
        self.btn_exportar_excel.setGeometry(QRect(680, 30, 100, 32))
        self.btn_exportar_excel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exportar_excel.clicked.connect(exportar_excel_productos)

        icon = qta.icon("ei.bell", color="#fd0")
        self.button2 = QPushButton(icon, "Press Me!")
        self.button2.setCheckable(True)
        self.button2.clicked.connect(self.action)

        #layout.addWidget(self.input)
        layout.addWidget(self.table)
        layout.addWidget(self.btn_exportar_excel)
        layout.addWidget(self.label)
        layout.addWidget(self.button2)
        
        self.verticalLayoutWidget.setLayout(layout)

        self.menubar = Menu(self, self.empresa)
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
    
    def action(self):
        print('Clicked!')
    
    def show_add_products_window(self, checked):
        if self.w is None:
            model = Product()
            self.w = viewAgregarProductos(self, empresa=self.empresa)
            self._controller = ProductController(self.w, model)
            self.w.assignController(self._controller)
            self.w.show()
        else:
            self.w.close() 
            self.w = None

    def assignController(self, controller):
        self._controller = controller

    def contextMenuEvent(self, e):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(e.globalPos())

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sistema de Producci\u00f3n y Costos", None))
        self.btn_buscar.setText(QCoreApplication.translate("Dialog", u"Buscar", None))
        self.btn_exportar_excel.setText(QCoreApplication.translate("Dialog", u"Exportar Excel", None))
        self.btn_agregar.setText(QCoreApplication.translate("Dialog", u"Agregar Producto", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Criterios de b\u00fasqueda", None))
    # retranslateUi
    
    def buscarProducto(self):
        selected_option = str(self.combo_busqueda.currentText().strip())
        parameter = str(self.txt_busqueda.text().strip())
        if selected_option == '':
            print('Debes seleccionar una opción')
        else:
            if parameter != '':
                if selected_option == 'Nombre':
                    self.controller.search_product_by_name(parameter)
                elif selected_option == 'Código':
                    self.controller.search_product_by_code(parameter)
                elif selected_option == 'Marca':
                    self.controller.search_product_by_mark(parameter)
                elif selected_option == 'Modelo':
                    self.controller.search_product_by_model(parameter)
            else:
                products = self.controller.getAllProducts()
                self.updateView(products)

    def updateView(self, data):
        self.table.refresh(data, header=self.headers)