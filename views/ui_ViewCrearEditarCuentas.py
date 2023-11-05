# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_account_uinGTdvP.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QLineEdit, QLabel, QDialog, QPushButton
from views.messages import Messages
import qtawesome as qta


class ViewCrearCuentas(QDialog, Messages):
    def __init__(self, root = None, empresa=None, user=None):
        super().__init__()
        self._mainWindow = root
        self.empresa = empresa
        self.user = user
        self.w = None

    def assignController(self, controller):
        self._controller = controller
        print(self._controller)
        self.setupUi(self)

    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(450, 420)

        icon = qta.icon('ei.adult')
        self.setWindowIcon(icon)

        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(16)
        font.setBold(True)

        self.l_titulo = QLabel(Dialog)
        self.l_titulo.setObjectName(u"l_titulo")
        self.l_titulo.setGeometry(QRect(80, 30, 300, 41))
        self.l_titulo.setFont(font)

        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(12)
        font1.setBold(True)

        self.l_username = QLabel(Dialog)
        self.l_username.setObjectName(u"l_username")
        self.l_username.setGeometry(QRect(60, 90, 181, 31))
        self.l_username.setFont(font1)

        self.txt_username = QLineEdit(Dialog)
        self.txt_username.setObjectName(u"txt_username")
        self.txt_username.setGeometry(QRect(60, 120, 320, 24))
        
        self.txt_email = QLineEdit(Dialog)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setGeometry(QRect(60, 180, 320, 24))

        self.l_email = QLabel(Dialog)
        self.l_email.setObjectName(u"l_email")
        self.l_email.setGeometry(QRect(60, 150, 181, 31))
        self.l_email.setFont(font1)

        self.l_password = QLabel(Dialog)
        self.l_password.setObjectName(u"l_password")
        self.l_password.setGeometry(QRect(60, 210, 181, 31))
        self.l_password.setFont(font1)

        self.txt_password1 = QLineEdit(Dialog)
        self.txt_password1.setObjectName(u"txt_password1")
        self.txt_password1.setGeometry(QRect(60, 240, 320, 24))
        
        self.txt_password2 = QLineEdit(Dialog)
        self.txt_password2.setObjectName(u"txt_password2")
        self.txt_password2.setGeometry(QRect(60, 310, 320, 24))
        self.l_password2 = QLabel(Dialog)

        self.l_password2.setObjectName(u"l_password2")
        self.l_password2.setGeometry(QRect(60, 280, 181, 31))
        self.l_password2.setFont(font1)

        self.btn_crear = QPushButton(Dialog)
        self.btn_crear.setObjectName(u"btn_crear")
        self.btn_crear.setGeometry(QRect(90, 370, 101, 31))
        self.btn_crear.clicked.connect(self.crearCuentaUsuario)

        self.btn_cancelar = QPushButton(Dialog)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setGeometry(QRect(240, 370, 101, 31))
        self.btn_crear.clicked.connect(self.closeWindow)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Crear Cuentas de Usuarios", None))
        self.l_titulo.setText(QCoreApplication.translate("Dialog", u"Crear una cuenta de usuario", None))
        self.l_username.setText(QCoreApplication.translate("Dialog", u"Nombre de usuario:", None))
        self.l_email.setText(QCoreApplication.translate("Dialog", u"Email:", None))
        self.l_password.setText(QCoreApplication.translate("Dialog", u"Contrase\u00f1a:", None))
        self.l_password2.setText(QCoreApplication.translate("Dialog", u"Confirme contrase\u00f1a", None))
        self.btn_crear.setText(QCoreApplication.translate("Dialog", u"Crear cuenta", None))
        self.btn_cancelar.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
    # retranslateUi

    def closeEvent(self, event):
        self._mainWindow.w = None
        
    def mostrarPrincipal(self):
        self._mainWindow.show()
        self.hide()

    def closeWindow(self):
        self.close()

    def crearCuentaUsuario(self):
        username  = self.txt_username.text().strip()
        email     = self.txt_email.text().strip()
        password1 = self.txt_password1.text().strip()
        password2 = self.txt_password2.text().strip()

        self._controller.registrar_cuenta(username, email, password1, password2)
