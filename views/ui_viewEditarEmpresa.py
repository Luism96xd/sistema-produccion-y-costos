# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'view_EmpresauVNIJb.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QRect, QMetaObject, QCoreApplication
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QLineEdit, QPushButton, QLabel, QComboBox, QDialog, QFileDialog
import shutil
import os

from views.messages import Messages


class ViewEditarEmpresa(QDialog, Messages):
    def __init__(self, parent = None, empresa = None):
        super().__init__()
        self._mainWindow = parent
        self.empresa = empresa
        self.selected_id = self.empresa.getId()
        self.basedir = os.path.dirname(__file__)

    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(720, 480)
        
        self.btn_guardar = QPushButton(Dialog)
        self.btn_guardar.setObjectName(u"btn_guardar")
        self.btn_guardar.setGeometry(QRect(200, 430, 128, 32))
        self.btn_guardar.clicked.connect(self.editarEmpresa)
        
        self.btn_cancelar = QPushButton(Dialog)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setGeometry(QRect(380, 430, 128, 32))
        self.btn_cancelar.clicked.connect(self.closeWindow)

        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        font.setBold(True)

        self.l_nombre = QLabel(Dialog)
        self.l_nombre.setObjectName(u"l_nombre")
        self.l_nombre.setGeometry(QRect(32, 90, 181, 32))
        self.l_nombre.setFont(font)

        self.txt_nombre = QLineEdit(Dialog)
        self.txt_nombre.setObjectName(u"txt_nombre")
        self.txt_nombre.setGeometry(QRect(210, 90, 401, 24))
        
        self.l_direccion1 = QLabel(Dialog)
        self.l_direccion1.setObjectName(u"l_direccion1")
        self.l_direccion1.setGeometry(QRect(32, 200, 171, 32))
        self.l_direccion1.setFont(font)
        
        self.txt_direccion1 = QLineEdit(Dialog)
        self.txt_direccion1.setObjectName(u"txt_direccion1")
        self.txt_direccion1.setGeometry(QRect(210, 200, 401, 24))
        
        self.l_direccion2 = QLabel(Dialog)
        self.l_direccion2.setObjectName(u"l_direccion2")
        self.l_direccion2.setGeometry(QRect(32, 250, 181, 32))
        self.l_direccion2.setFont(font)
       
        self.txt_direccion2 = QLineEdit(Dialog)
        self.txt_direccion2.setObjectName(u"txt_direccion2")
        self.txt_direccion2.setGeometry(QRect(210, 250, 401, 24))
        
        self.l_RIF = QLabel(Dialog)
        self.l_RIF.setObjectName(u"l_RIF")
        self.l_RIF.setGeometry(QRect(32, 140, 181, 32))
        self.l_RIF.setFont(font)
        
        self.txt_RIF = QLineEdit(Dialog)
        self.txt_RIF.setObjectName(u"txt_RIF")
        self.txt_RIF.setGeometry(QRect(210, 140, 141, 24))

        font1 = QFont()
        font1.setFamily(u"Alef")
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setUnderline(False)
        
        self.l_titulo = QLabel(Dialog)
        self.l_titulo.setObjectName(u"l_titulo")
        self.l_titulo.setGeometry(QRect(32, 20, 321, 40))
        self.l_titulo.setFont(font1)
        
        self.l_estado = QLabel(Dialog)
        self.l_estado.setObjectName(u"l_estado")
        self.l_estado.setGeometry(QRect(32, 310, 181, 32))
        self.l_estado.setFont(font)
        
        self.comboBox = QComboBox(Dialog)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(210, 310, 111, 24))
        self.comboBox.addItems(['Carabobo'])
        
        self.txt_ciudad = QLineEdit(Dialog)
        self.txt_ciudad.setObjectName(u"txt_ciudad")
        self.txt_ciudad.setGeometry(QRect(450, 310, 161, 24))
        
        self.l_telefono1 = QLabel(Dialog)
        self.l_telefono1.setObjectName(u"l_telefono1")
        self.l_telefono1.setGeometry(QRect(370, 140, 181, 32))
        self.l_telefono1.setFont(font)
        
        self.txt_telefono1 = QLineEdit(Dialog)
        self.txt_telefono1.setObjectName(u"txt_telefono1")
        self.txt_telefono1.setGeometry(QRect(470, 140, 141, 24))
        
        self.l_logo = QLabel(Dialog)
        self.l_logo.setObjectName(u"l_logo")
        self.l_logo.setGeometry(QRect(32, 360, 91, 32))
        self.l_logo.setFont(font)
        
        self.l_ciudad = QLabel(Dialog)
        self.l_ciudad.setObjectName(u"l_ciudad")
        self.l_ciudad.setGeometry(QRect(360, 310, 181, 21))
        self.l_ciudad.setFont(font)
        
        self.txt_logo = QLineEdit(Dialog)
        self.txt_logo.setObjectName(u"txt_logo")
        self.txt_logo.setGeometry(QRect(210, 370, 321, 24))
        
        self.btn_buscar = QPushButton(Dialog)
        self.btn_buscar.setObjectName(u"btn_buscar")
        self.btn_buscar.setGeometry(QRect(540, 370, 75, 24))
        self.btn_buscar.clicked.connect(self.select_file)

        self.populateInputs(self.empresa)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.btn_guardar.setText(QCoreApplication.translate("Dialog", u"Guardar", None))
        self.btn_cancelar.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
        self.l_nombre.setText(QCoreApplication.translate("Dialog", u"Nombre de la empresa:", None))
        self.l_direccion1.setText(QCoreApplication.translate("Dialog", u"Direcci\u00f3n 1:", None))
        self.l_direccion2.setText(QCoreApplication.translate("Dialog", u"Direcci\u00f3n 2:", None))
        self.l_RIF.setText(QCoreApplication.translate("Dialog", u"RIF:", None))
        self.l_titulo.setText(QCoreApplication.translate("Dialog", u"Datos de la empresa", None))
        self.l_estado.setText(QCoreApplication.translate("Dialog", u"Estado:", None))
        self.l_telefono1.setText(QCoreApplication.translate("Dialog", u"Tel\u00e9fono 1:", None))
        self.l_logo.setText(QCoreApplication.translate("Dialog", u"Logo:", None))
        self.l_ciudad.setText(QCoreApplication.translate("Dialog", u"Ciudad:", None))
        self.btn_buscar.setText(QCoreApplication.translate("Dialog", u"Buscar", None))
    # retranslateUi


    def assignController(self, controller):
        self._controller = controller
        print(self._controller)
        self.setupUi(self)

    def closeEvent(self, event):
        self._mainWindow.w = None

    def closeWindow(self):
        self.close()

    def populateInputs(self, empresa):
        self.txt_nombre.setText(empresa.getName())  
        self.txt_RIF.setText(empresa.getRIF())
        self.txt_direccion1.setText(empresa.getDireccion1())
        self.txt_direccion2.setText(empresa.getDireccion2())
        self.txt_telefono1.setText(empresa.getTelefono1())
        self.txt_ciudad.setText(empresa.getCiudad())
        self.txt_logo.setText(empresa.getLogo())

    def select_file(self):
        file_path = QFileDialog.getOpenFileName()[0]
        self.txt_logo.setText(file_path)
        
    def editarEmpresa(self):
        nombre_empresa = self.txt_nombre.text().strip()
        rif_empresa = self.txt_RIF.text().strip()
        telefono1 = self.txt_telefono1.text().strip()
        direccion1 = self.txt_direccion1.text().strip()
        direccion2 = self.txt_direccion2.text().strip()
        estado     = self.comboBox.currentText().strip()
        ciudad     = self.txt_ciudad.text().strip()
        logo_path  = self.txt_logo.text().strip()

        try:
            new_path = shutil.copy(logo_path, 'assets/')
        except Exception as e:
            new_path = logo_path

        self._controller.editar_empresa(nombre_empresa, rif_empresa, telefono1, direccion1, direccion2, new_path, ciudad, estado, self.selected_id)
        