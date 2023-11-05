# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ViewCostoProduccionZVOygc.ui'
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
from views.messages import Messages
import os

class ViewCosto3(QDialog, Messages):
    def __init__(self, root = None, tipo = None, empresa = None):
        super().__init__()
        self._mainWindow = root
        self.tipo = tipo
        self.empresa = empresa
        self.basedir = os.path.dirname(__file__)

    def assignController(self, controller):
        self._controller = controller
        print(self._controller)
        self.setupUi(self)

    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(460, 474)
        
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(170, 380, 81, 61))
        self.buttonBox.setOrientation(Qt.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.L_titulo = QLabel(Dialog)
        self.L_titulo.setObjectName(u"L_titulo")
        self.L_titulo.setGeometry(QRect(20, 150, 241, 41))

        logo_path = self.empresa.getLogo()
        self.l_logo = QLabel(Dialog)
        self.l_logo.setObjectName(u"l_logo")
        self.l_logo.setGeometry(QRect(72, 30, 320, 101))
        self.l_logo.setStyleSheet(u"border-image: url({});".format(logo_path))

        self.l_valor1 = QLabel(Dialog)
        self.l_valor1.setObjectName(u"l_valor1")
        self.l_valor1.setGeometry(QRect(32, 200, 180, 51))

        self.txt_valor1 = QLineEdit(Dialog)
        self.txt_valor1.setObjectName(u"txt_valor1")
        self.txt_valor1.setGeometry(QRect(240, 190, 190, 24))

        self.l_valor2 = QLabel(Dialog)
        self.l_valor2.setObjectName(u"l_valor2")
        self.l_valor2.setGeometry(QRect(32, 250, 320, 31))

        self.txt_valor2 = QLineEdit(Dialog)
        self.txt_valor2.setObjectName(u"txt_valor2")
        self.txt_valor2.setGeometry(QRect(240, 250, 190, 24))

        self.l_valor3 = QLabel(Dialog)
        self.l_valor3.setObjectName(u"l_valor3")
        self.l_valor3.setGeometry(QRect(32, 310, 320, 24))

        self.txt_valor3 = QLineEdit(Dialog)
        self.txt_valor3.setObjectName(u"txt_valor3")
        self.txt_valor3.setGeometry(QRect(240, 310, 190, 24))

        self.retranslateUi(Dialog)

        if self.tipo == "costo de producción":
            self.buttonBox.accepted.connect(self.calcular_costo_produccion)
            self.buttonBox.rejected.connect(self.closeWindows) 

        elif self.tipo == "precio de venta": 
            self.buttonBox.accepted.connect(self.calcular_precio_venta)
            self.buttonBox.rejected.connect(self.closeWindows)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):

        if self.tipo== "costo de producción": 
            Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Costo de Producción", None))
            self.L_titulo.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Costo de Producción</span></p><p><br/></p></body></html>", None))
            self.l_valor1.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Material Directo:</span></p><p><br/></p></body></html>", None))
            self.l_valor2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Mano de Obra Directa:</span></p><p><br/></p></body></html>", None))
            self.l_logo.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><br/></p></body></html>", None))
            self.l_valor3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Carga Fabril:</span></p></body></html>", None))
           
        elif self.tipo== "precio de venta":
            Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Precio de Venta", None))
            self.L_titulo.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Precio de Venta</span></p><p><br/></p></body></html>", None))
            self.l_valor1.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Costo de Venta:</span></p><p><br/></p></body></html>", None))
            self.l_valor2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Gastos de Operación:</span></p><p><br/></p></body></html>", None))
            self.l_logo.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><br/></p></body></html>", None))
            self.l_valor3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Utilidad Deseada:</span></p></body></html>", None))
    # retranslateUi

    def mostrarPrincipal(self):
        self._mainWindow.show()
        self.hide()

    def closeWindows(self):
        self._mainWindow.w = None
        self.close()

    def calcular_costo_produccion(self):
        material_directo = float(self.txt_valor1.text().strip())
        mano_obra_ditecta = float(self.txt_valor2.text().strip())
        carga_fabril = float(self.txt_valor3.text().strip())

        self._controller.calcularCostoProduccion(material_directo, mano_obra_ditecta, carga_fabril)

    def calcular_precio_venta(self):
        costo_venta = float(self.txt_valor1.text().strip())
        gastos_operacion = float(self.txt_valor2.text().strip())
        utilidad_deseada = float(self.txt_valor3.text().strip())

        self._controller.calcular_precio_venta(costo_venta, gastos_operacion, utilidad_deseada)