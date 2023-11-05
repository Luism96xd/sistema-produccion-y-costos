# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewAgregarProductoscZLxkZ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import Qt, QRect, QCoreApplication, QMetaObject, QDateTime
from datetime import datetime
from PySide6.QtGui import QIntValidator, QFont, QDoubleValidator, QIcon
from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QDialogButtonBox, QComboBox, QDateEdit, QSpinBox, QCheckBox
from views.messages import Messages

class viewAgregarProductos(QWidget, Messages):
    def __init__(self, root = None, empresa = None):
        super().__init__()
        self._mainWindow = root
        self.selected_parent = {'index': None, 'name': None}
        self.empresa = empresa
    
    def setupUi(self, viewAgregarProductos):
        if not viewAgregarProductos.objectName():
            viewAgregarProductos.setObjectName(u"viewAgregarProductos")

        viewAgregarProductos.resize(600, 384)
        self.buttonBox = QDialogButtonBox(viewAgregarProductos)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(48, 336, 256, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.buttonBox.accepted.connect(self.addProduct)
        self.buttonBox.rejected.connect(self.closeWindows)
    
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        font.setBold(True)

        self.l_nombre = QLabel(viewAgregarProductos)
        self.l_nombre.setObjectName(u"l_nombre")
        self.l_nombre.setGeometry(QRect(48, 40, 191, 32))
        self.l_nombre.setFont(font)

        self.txt_nombre = QLineEdit(viewAgregarProductos)
        self.txt_nombre.setObjectName(u"txt_nombre")
        self.txt_nombre.setStyleSheet("border: 1px solid black; border-radius: 2px;")
        self.txt_nombre.setGeometry(QRect(48, 75, 256, 28))

        self.l_descripcion = QLabel(viewAgregarProductos)
        self.l_descripcion.setObjectName(u"l_descripcion")
        self.l_descripcion.setGeometry(QRect(48, 100, 128, 32))
        self.l_descripcion.setFont(font)
        
        self.txt_descripcion = QLineEdit(viewAgregarProductos)
        self.txt_descripcion.setStyleSheet("border: 1px solid black; border-radius: 2px;")
        self.txt_descripcion.setObjectName(u"txt_descripcion")
        self.txt_descripcion.setGeometry(QRect(48, 135, 256, 28))

        self.l_fecha_ingreso = QLabel(viewAgregarProductos)
        self.l_fecha_ingreso.setObjectName(u"l_fecha_ingreso")
        self.l_fecha_ingreso.setGeometry(QRect(352, 40, 256, 32))
        self.l_fecha_ingreso.setFont(font)

        self.txt_fecha_ingreso = QDateEdit(viewAgregarProductos)
        self.txt_fecha_ingreso.setObjectName(u"txt_fecha_ingreso")
        self.txt_fecha_ingreso.setGeometry(QRect(352, 75, 128, 28))

        # Checkbox
        self.checkbox = QCheckBox(viewAgregarProductos)
        self.checkbox.setObjectName(u"checkbox")
        self.checkbox.setGeometry(QRect(352, 135, 128, 32))

        self.l_cantidad = QLabel(viewAgregarProductos)
        self.l_cantidad.setObjectName(u"l_cantidad")
        self.l_cantidad.setGeometry(QRect(48, 165, 128, 32))
        self.l_cantidad.setFont(font)

        self.txt_cantidad = QSpinBox(viewAgregarProductos)
        self.txt_cantidad.setObjectName(u"txt_cantidad")
        self.txt_cantidad.setStyleSheet("border: 1px solid black; border-radius: 2px;")
        self.txt_cantidad.setGeometry(QRect(48, 200, 256, 28))

        self.l_fecha_vencimiento = QLabel(viewAgregarProductos)
        self.l_fecha_vencimiento.setObjectName(u"l_fecha_vencimiento")
        self.l_fecha_vencimiento.setGeometry(QRect(352, 165, 256, 32))
        self.l_fecha_vencimiento.setFont(font)

        self.txt_fecha_vencimiento = QDateEdit(viewAgregarProductos)
        self.txt_fecha_vencimiento.setObjectName(u"txt_fecha_vencimiento")
        self.txt_fecha_vencimiento.setEnabled(False)
        self.txt_fecha_vencimiento.setGeometry(QRect(352, 200, 128, 28))

        
        # self.l_ubicacion = QLabel(viewAgregarProductos)
        # self.l_ubicacion.setObjectName(u"l_ubicacion")
        # self.l_ubicacion.setGeometry(QRect(352, 165, 128, 32))
        # self.l_ubicacion.setFont(font)

        # self.btn_ubicacion = QPushButton(viewAgregarProductos)
        # self.btn_ubicacion.setObjectName(u"btn_buscar_ubicacion")
        # self.btn_ubicacion.setGeometry(QRect(352, 200, 128, 28))

        self.l_costo = QLabel(viewAgregarProductos)
        self.l_costo.setObjectName(u"costo_txt")
        self.l_costo.setGeometry(QRect(48, 230, 128, 32))
        self.l_costo.setFont(font)

        self.txt_costo = QLineEdit(viewAgregarProductos)
        self.txt_costo.setObjectName(u"txt_costo")
        self.txt_costo.setStyleSheet("border: 1px solid black; border-radius: 2px;")
        self.txt_costo.setGeometry(QRect(48, 258, 256, 28))

        self.l_parent = QLabel(viewAgregarProductos)
        self.l_parent.setObjectName(u"l_parent")
        self.l_parent.setGeometry(QRect(352, 230, 128, 28))
        self.l_parent.setFont(font)

        self.combo_parent = QComboBox(viewAgregarProductos)
        self.combo_parent.addItems(['Seleccionar valor...'] + self._controller.getProductNames())
        self.combo_parent.setGeometry(QRect(352, 258, 128, 28))

        # The default signal from currentIndexChanged sends the index
        self.combo_parent.currentIndexChanged.connect(self.index_changed)
        # The same signal can send a text string
        self.combo_parent.currentTextChanged.connect(self.text_changed)
        # Connect the checkbox to the date picker
        self.checkbox.stateChanged.connect(self.enable_date_picker)

        onlyDouble  = QDoubleValidator()
        self.txt_costo.setValidator(onlyDouble)

        self.retranslateUi(viewAgregarProductos)

        QMetaObject.connectSlotsByName(viewAgregarProductos)
    # setupUi

    def retranslateUi(self, viewAgregarProductos):
        viewAgregarProductos.setWindowTitle(QCoreApplication.translate("viewAgregarProductos", u"Agregar producto", None))
        self.l_nombre.setText(QCoreApplication.translate("viewAgregarProductos", u"Nombre del producto:", None))
        self.l_cantidad.setText(QCoreApplication.translate("viewAgregarProductos", u"Cantidad:", None))
        self.l_descripcion.setText(QCoreApplication.translate("viewAgregarProductos", u"Descripci\u00f3n:", None))
        self.l_costo.setText(QCoreApplication.translate("viewAgregarProductos", u"Costo:", None))
        self.checkbox.setText(QCoreApplication.translate("viewAgregarProductos", u"¿Perecedero?", None))
        self.l_fecha_vencimiento.setText(QCoreApplication.translate("viewAgregarProductos", u"Fecha de Vencimiento", None))
        self.l_parent.setText(QCoreApplication.translate("viewAgregarProductos", u"Categoría:", None))
        self.l_fecha_ingreso.setText(QCoreApplication.translate("viewAgregarProductos", u"Fecha de Ingreso:", None))
        #self.btn_ubicacion.setText(QCoreApplication.translate("viewAgregarProductos", u"Buscar", None))
    # retranslateUi

    def enable_date_picker(self, state):
        self.txt_fecha_vencimiento.setEnabled(state == Qt.Checked)

    def get_date(self):
        date = None
        if self.checkbox.isChecked():
            # Get the selected date and convert it to a datetime object
            date = self.txt_fecha_vencimiento.date().toPython().strftime("%Y-%m-%d %H:%M:%S")
            print(date)
            # Do something with the datetime object
            print(f'Selected date: {date}')
        else:
            print('Date picker not enabled')
        return date

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

    def addProduct(self):
        id_empresa        = 1 #self.empresa.getId()
        name              = str(self.txt_nombre.text().strip())
        descripcion       = str(self.txt_descripcion.text().strip())
        cantidad          = int(self.txt_cantidad.value())
        costo             = float(self.txt_costo.text().strip()) if self.txt_costo.text() != '' else 0
        fecha_creacion    = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        parent            = self.selected_parent
        fecha_ingreso     = self.txt_fecha_ingreso.date().toPython().strftime("%Y-%m-%d %H:%M:%S")
        fecha_vencimiento = self.get_date()

        if (name != '' and descripcion != '' and cantidad > 0 and costo >= 0 and self.selected_parent['index'] != 0):
            response = self._controller.add_product(name, descripcion, cantidad, costo, fecha_creacion, parent, fecha_ingreso, fecha_vencimiento, id_empresa)
            return response

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
