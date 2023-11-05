# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewAgregarProductoscZLxkZ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import Qt, QRect, QCoreApplication, QMetaObject
from datetime import datetime
from PySide6.QtGui import QIntValidator, QFont, QDoubleValidator, QIcon
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QDialogButtonBox, QComboBox, QSpinBox
from views.messages import Messages

class ViewEditarProductos(QWidget, Messages):
    def __init__(self, root = None, product_id=None):
        super().__init__()
        self._mainWindow = root
        self.selected_parent = {'index': 0, 'name': None}
        self.product_id = product_id
    
    def setupUi(self, viewAgregarProductos):
        if not viewAgregarProductos.objectName():
            viewAgregarProductos.setObjectName(u"viewAgregarProductos")

        viewAgregarProductos.resize(512, 329)
        self.buttonBox = QDialogButtonBox(viewAgregarProductos)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(420, 20, 81, 241))
        self.buttonBox.setOrientation(Qt.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.buttonBox.accepted.connect(self.updateProduct)
        self.buttonBox.rejected.connect(self.closeWindows)
    
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        font.setBold(True)

        self.l_nombre = QLabel(viewAgregarProductos)
        self.l_nombre.setObjectName(u"l_nombre")
        self.l_nombre.setGeometry(QRect(16, 40, 191, 32))
        self.l_nombre.setFont(font)

        self.txt_nombre = QLineEdit(viewAgregarProductos)
        self.txt_nombre.setObjectName(u"txt_nombre")
        self.txt_nombre.setStyleSheet("border: 2px solid black; border-radius: 3px;")
        self.txt_nombre.setGeometry(QRect(16, 75, 256, 28))

        self.l_descripcion = QLabel(viewAgregarProductos)
        self.l_descripcion.setObjectName(u"l_descripcion")
        self.l_descripcion.setGeometry(QRect(16, 100, 128, 32))
        self.l_descripcion.setFont(font)
        
        self.txt_descripcion = QLineEdit(viewAgregarProductos)
        self.txt_descripcion.setStyleSheet("border: 2px solid black; border-radius: 3px;")
        self.txt_descripcion.setObjectName(u"txt_descripcion")
        self.txt_descripcion.setGeometry(QRect(16, 135, 256, 28))

        self.l_cantidad = QLabel(viewAgregarProductos)
        self.l_cantidad.setObjectName(u"l_cantidad")
        self.l_cantidad.setGeometry(QRect(16, 165, 128, 32))
        self.l_cantidad.setFont(font)

        self.txt_cantidad = QSpinBox(viewAgregarProductos)
        self.txt_cantidad.setObjectName(u"txt_cantidad")
        self.txt_cantidad.setStyleSheet("border: 2px solid black; border-radius: 3px;")
        self.txt_cantidad.setGeometry(QRect(16, 200, 256, 28))

        self.l_costo = QLabel(viewAgregarProductos)
        self.l_costo.setObjectName(u"costo_txt")
        self.l_costo.setGeometry(QRect(16, 230, 128, 32))
        self.l_costo.setFont(font)

        self.txt_costo = QLineEdit(viewAgregarProductos)
        self.txt_costo.setObjectName(u"txt_costo")
        self.txt_costo.setStyleSheet("border: 2px solid black; border-radius: 3px;")
        self.txt_costo.setGeometry(QRect(16, 258, 256, 28))

        self.l_parent = QLabel(viewAgregarProductos)
        self.l_parent.setObjectName(u"l_parent")
        self.l_parent.setGeometry(QRect(320, 230, 128, 28))
        self.l_parent.setFont(font)

        self.combo_parent = QComboBox(viewAgregarProductos)
        self.combo_parent.addItems(['Seleccionar valor...'] + self._controller.getProductNames())
        self.combo_parent.setGeometry(QRect(320, 258, 128, 28))

        # The default signal from currentIndexChanged sends the index
        self.combo_parent.currentIndexChanged.connect(self.index_changed)
        # The same signal can send a text string
        self.combo_parent.currentTextChanged.connect(self.text_changed)

        onlyDouble  = QDoubleValidator()
        self.txt_costo.setValidator(onlyDouble)

        self.retranslateUi(viewAgregarProductos)

        self.populateInputs()

        QMetaObject.connectSlotsByName(viewAgregarProductos)
    # setupUi

    def retranslateUi(self, viewAgregarProductos):
        viewAgregarProductos.setWindowTitle(QCoreApplication.translate("viewAgregarProductos", u"Agregar producto", None))
        self.l_nombre.setText(QCoreApplication.translate("viewAgregarProductos", u"Nombre del producto:", None))
        self.l_cantidad.setText(QCoreApplication.translate("viewAgregarProductos", u"Cantidad:", None))
        self.l_descripcion.setText(QCoreApplication.translate("viewAgregarProductos", u"Descripci\u00f3n:", None))
        self.l_costo.setText(QCoreApplication.translate("viewAgregarProductos", u"Costo:", None))
        self.l_parent.setText(QCoreApplication.translate("viewAgregarProductos", u"Pertenece a:", None))
    # retranslateUi

    def populateInputs(self):
        data = self._controller.select_product_by_id(self.product_id)
        self.txt_nombre.setText(str(data[2]))
        self.txt_descripcion.setText(str(data[3]))
        self.txt_cantidad.setValue(int(data[4]))
        self.txt_costo.setText(str(data[5]))

    def assignController(self, controller):
        self._controller = controller
        print(self._controller)
        self.setupUi(self)
    
    def index_changed(self, i): # i is an int
        print(i)
        self.selected_parent['index'] = i

    def text_changed(self, s): # s is a str
        print(s)
        self.selected_parent['name'] = s

    def updateView(self, data):
        self._mainWindow.updateView(data)

    def closeEvent(self, event):
        self._mainWindow.w = None
        
    def mostrarPrincipal(self):
        self._mainWindow.show()
        self.hide()

    def closeWindows(self):
        self._mainWindow.w = None
        self.close()

    def updateProduct(self):
        name        = str(self.txt_nombre.text().strip())
        description = str(self.txt_descripcion.text().strip())
        quantity    = int(self.txt_cantidad.value())
        cost        = float(self.txt_costo.text().strip())
        parent      = self.selected_parent

        self._controller.updateProduct(self.product_id, name, description, quantity, cost, parent)
        