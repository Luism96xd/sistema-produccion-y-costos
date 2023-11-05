# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'usuario_claveyDiKEA.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)
from views.messages import Messages
import qtawesome as qta
import os

class ViewIniciarSesion(QMainWindow, Messages):
    def __init__(self, root = None, empresa = None):
        super().__init__()
        self._mainWindow = root
        self.empresa = empresa
        self.basedir = os.path.dirname(__file__)

    def assignController(self, controller):
        self._controller = controller
        print(self._controller)
        self.setupUi(self)
    
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(415, 442)

        icon = qta.icon('ei.adult')
        self.setWindowIcon(icon)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        logo_path = self.empresa.getLogo()
        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"label_4")
        self.logo.setGeometry(QRect(56, 40, 312, 101))
        self.logo.setStyleSheet(u"border-image: url({});".format(logo_path))

        self.l_usuario = QLabel(self.centralwidget)
        self.l_usuario.setObjectName(u"l_usuario")
        self.l_usuario.setGeometry(QRect(80, 140, 81, 51))

        self.l_clave = QLabel(self.centralwidget)
        self.l_clave.setObjectName(u"l_clave")
        self.l_clave.setGeometry(QRect(80, 230, 101, 51))

        self.txt_usuario = QLineEdit(self.centralwidget)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setGeometry(QRect(80, 190, 251, 31))
        self.txt_usuario.setPlaceholderText("Ingrese su usuario")
        self.txt_usuario.setStyleSheet(u"background:rgb(218, 218, 218); border: 2px solid black; border-radius: 8px")

        self.txt_clave = QLineEdit(self.centralwidget)
        self.txt_clave.setObjectName(u"txt_clave")
        self.txt_clave.setGeometry(QRect(80, 280, 251, 31))
        self.txt_clave.setPlaceholderText("Ingrese su contraseña")
        self.txt_clave.setStyleSheet(u"background:rgb(218, 218, 218); lineedit-password-character: 9679; border: 2px solid black; border-radius: 8px")
        self.txt_clave.setEchoMode(QLineEdit.Password)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(150, -10, 111, 51))

        self.Boton_Iniciar_Sesion = QPushButton(self.centralwidget)
        self.Boton_Iniciar_Sesion.setObjectName(u"Boton_Iniciar_Sesion")
        self.Boton_Iniciar_Sesion.setStyleSheet(u"background: #0077ee; border: 1px solid #222; font-family:'Arial'; font-size: 14px; font-weight: 700; border-radius: 16px; color: white")
        self.Boton_Iniciar_Sesion.setGeometry(QRect(140, 340, 128, 32))
        self.Boton_Iniciar_Sesion.setCursor(QCursor(Qt.PointingHandCursor))

        self.Boton_Salir = QPushButton(self.centralwidget)
        self.Boton_Salir.setObjectName(u"Boton_Salir")
        self.Boton_Salir.setStyleSheet(u"background: #111111; border: 1px solid #222; font-family:'Arial'; font-size: 14px; font-weight: 700; border-radius: 16px; color: white")
        self.Boton_Salir.setGeometry(QRect(140, 380, 128, 32))
        self.Boton_Salir.setCursor(QCursor(Qt.PointingHandCursor))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 415, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.Boton_Iniciar_Sesion.clicked.connect(self.iniciar_sesion)
        self.Boton_Salir.clicked.connect(self.closeWindows)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sistema de Producción y Costos", None))
        self.l_usuario.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Usuario:</span></p></body></html>", None))
        self.l_clave.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Contrase\u00f1a:</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">\u00a1Bienvenido!</span></p></body></html>", None))
        self.Boton_Iniciar_Sesion.setText(QCoreApplication.translate("MainWindow", u"Iniciar Sesi\u00f3n", None))
        self.Boton_Salir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
    # retranslateUi

    def iniciar_sesion(self):
        usuario = self.txt_usuario.text().strip()
        clave = self.txt_clave.text().strip()
        self._controller.iniciar_sesion(usuario, clave)

    def mostrarPrincipal(self):
        self._mainWindow.show()
        self.hide()

    def closeWindows(self):
        self.close()