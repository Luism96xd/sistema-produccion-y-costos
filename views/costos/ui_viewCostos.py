# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vista costo 1HoHQZC.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QComboBox, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)
from models.costos import Costos
from controllers.costosController import CostosController
from views.messages import Messages
from views.costos.ui_viewCosto3 import ViewCosto3
from views.costos.ui_viewCalcularCostos import ViewCalcularCostos

class ViewCostos(QMainWindow, Messages):
    def __init__(self, root = None, empresa = None):
        super().__init__()
        self._mainWindow = root
        self.w = None 
        self.costo_indice = None
        self.costo = None
        self.empresa = empresa

    def assignController(self, controller):
        self._controller = controller
        print(self._controller)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        MainWindow.resize(512, 600)
        self.setMinimumWidth(512)
        self.setMinimumHeight(600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.CostodeProduccion = QLabel(self.centralwidget)
        self.CostodeProduccion.setObjectName(u"CostodeProduccion")
        self.CostodeProduccion.setGeometry(QRect(16, 320, 231, 81))

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 380, 411, 51))

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(340, 390, 141, 31))

        # The default signal from currentIndexChanged sends the index
        self.comboBox.currentIndexChanged.connect(self.index_changed)
        # The same signal can send a text string
        self.comboBox.currentTextChanged.connect(self.text_changed)

        self.l_empresa_nombre = QLabel(self.centralwidget)
        self.l_empresa_nombre.setObjectName(u"l_empresa_nombre")
        self.l_empresa_nombre.setGeometry(QRect(28, 20, 451, 71))

        self.calendarWidget = QCalendarWidget(self.centralwidget)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(96, 140, 320, 184))

        self.welcome_text = QLabel(self.centralwidget)
        self.welcome_text.setObjectName(u"welcome_text")
        self.welcome_text.setGeometry(QRect(200, 100, 111, 21))

        self.boton_abrir = QPushButton(self.centralwidget)
        self.boton_abrir.setObjectName(u"boton_abrir")
        self.boton_abrir.setGeometry(QRect(120, 460, 75, 23))
        self.boton_abrir.clicked.connect(self.show_calculate_cost_window)

        self.boton_cancelar = QPushButton(self.centralwidget)
        self.boton_cancelar.setObjectName(u"boton_cancelar")
        self.boton_cancelar.setGeometry(QRect(320, 460, 75, 23))
        self.boton_cancelar.clicked.connect(self.closeWindows)
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calcular costos de los Productos", None))
        self.CostodeProduccion.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">C\u00e1lculo de los Costos</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Seleccione el tipo de costo que desea calcular:</span></p></body></html>", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Costo Primo", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Costo de Conversi\u00f3n", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Costo Semivariable", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Costo Variable por Unidad", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Costo de Producci\u00f3n", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Costo Total de Productos en Proceso", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Costo del Producto Terminado", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Costo Total de Productos Terminados", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Costo de Venta", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Costo Total de Producci\u00f3n y Ventas", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"Precio de Venta", None))
        self.comboBox.setItemText(11, QCoreApplication.translate("MainWindow", u"Ganancias y P\u00e9rdidas", None))

        self.l_empresa_nombre.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700; color:#55007f;\">ZAYCO PLANTAS EL\u00c9CTRICAS, </span></p><p align=\"center\"><span style=\" font-size:11pt; font-weight:700; color:#55007f;\">FABRICACI\u00d3N, ENSAMBLAJE Y SERVICIO</span></p></body></html>", None))
        self.boton_abrir.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.welcome_text.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">\u00a1Bienvenido!</span></p></body></html>", None))
        self.boton_cancelar.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
    # retranslateUi
         
    def mostrarPrincipal(self):
        self._mainWindow.show()
        self.hide()

    def closeWindows(self):
        self._mainWindow.w = None
        self.close()

    def show_calculate_cost_window(self):
        if self.w is None:
            model = Costos()

            if self.costo == "costo de producción":
                self.w = ViewCosto3(self, self.costo, self.empresa)

            elif self.costo == "precio de venta":
                self.w = ViewCosto3(self, self.costo, self.empresa)
            
            elif self.costo == "costo de conversión":
                self.w = ViewCalcularCostos(self, self.costo, self.empresa)

            elif self.costo == "costo semivariable":
                self.w = ViewCalcularCostos(self, self.costo, self.empresa)

            elif self.costo == "costo total de productos en proceso":
                self.w = ViewCalcularCostos(self, self.costo, self.empresa)

            elif self.costo == "costo del producto terminado":
                self.w = ViewCalcularCostos(self, self.costo, self.empresa)

            elif self.costo == "costo total de productos terminados":
                self.w = ViewCalcularCostos(self, self.costo, self.empresa)
            
            elif self.costo == "costo de venta":
                self.w = ViewCalcularCostos(self, self.costo, self.empresa)
            
            elif self.costo == "costo total de producción y ventas":
                self.w = ViewCalcularCostos(self, self.costo, self.empresa)
            
            elif self.costo == "costo variable por unidad":
                self.w = ViewCalcularCostos(self, self.costo, self.empresa)

            elif self.costo == "ganancias y pérdidas":
                self.w = ViewCalcularCostos(self, self.costo, self.empresa)

            else:
                self.w = ViewCalcularCostos(self, "costo primo", self.empresa)
            
            self._controller = CostosController(self.w, model)
            self.w.assignController(self._controller)
            self.w.show()
        else:
            self.w.close() 
            self.w = None

    def index_changed(self, i): # i is an int
        print(i)
        self.costo_indice = i

    def text_changed(self, texto): # s is a str
        print(texto)
        self.costo = texto.lower()