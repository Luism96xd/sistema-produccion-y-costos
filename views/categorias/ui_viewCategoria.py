# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'view_agregar_categoriaMTFWNz.ui'
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
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QLineEdit, QSizePolicy, QWidget)
from messages import Messages

class ViewCategoria(QWidget, Messages):
    def __init__(self, root = None):
        super().__init__()
        self.w = None
        self._mainWindow = root

    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(420, 256)

        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        font.setBold(True)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 271, 32))
        self.label.setFont(font)
   
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(10)
        font1.setBold(False)

        self.label_nombre = QLabel(Dialog)
        self.label_nombre.setObjectName(u"label_nombre")
        self.label_nombre.setGeometry(QRect(30, 80, 81, 31))
        self.label_nombre.setFont(font1)
        
        self.label_descripcion = QLabel(Dialog)
        self.label_descripcion.setObjectName(u"label_descripcion")
        self.label_descripcion.setGeometry(QRect(30, 150, 81, 31))
        self.label_descripcion.setFont(font1)
        
        self.txt_nombre = QLineEdit(Dialog)
        self.txt_nombre.setObjectName(u"txt_nombre")
        self.txt_nombre.setGeometry(QRect(130, 80, 231, 31))
        
        self.txt_descripcion = QLineEdit(Dialog)
        self.txt_descripcion.setObjectName(u"txt_descripcion")
        self.txt_descripcion.setGeometry(QRect(130, 150, 231, 31))
        
        self.buttonBox_2 = QDialogButtonBox(Dialog)
        self.buttonBox_2.setObjectName(u"buttonBox_2")
        self.buttonBox_2.setGeometry(QRect(140, 220, 156, 24))
        self.buttonBox_2.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Agregar Categor\u00eda de Productos", None))
        self.label_nombre.setText(QCoreApplication.translate("Dialog", u"Nombre", None))
        self.label_descripcion.setText(QCoreApplication.translate("Dialog", u"Descripci\u00f3n", None))
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
