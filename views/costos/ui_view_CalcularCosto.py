# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ViewCostoPrimovPrOga.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from views.messages import Messages
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap,QDoubleValidator, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QLineEdit, QSizePolicy, QWidget)


class ViewCalcularCostos(QDialog, Messages):
    def __init__(self, root = None, costo=None):
        super().__init__()
        self._mainWindow = root 
        self.costo = costo

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
        self.L_titulo.setGeometry(QRect(20, 150, 400, 41))
        self.l_valor1 = QLabel(Dialog)
        self.l_valor1.setObjectName(u"l_valor1")
        self.l_valor1.setGeometry(QRect(20, 200, 300, 51))
        self.txt_valor1 = QLineEdit(Dialog)
        self.txt_valor1.setObjectName(u"txt_valor1")
        self.txt_valor1.setGeometry(QRect(20, 240, 170, 31))
        self.l_valor2 = QLabel(Dialog)
        self.l_valor2.setObjectName(u"l_valor2")
        self.l_valor2.setGeometry(QRect(20, 280, 300, 31))
        self.txt_valor2 = QLineEdit(Dialog)
        self.txt_valor2.setObjectName(u"txt_valor2")
        self.txt_valor2.setGeometry(QRect(20, 320, 170, 31))

        self.l_logo = QLabel(Dialog)
        self.l_logo.setObjectName(u"l_logo")
        self.l_logo.setGeometry(QRect(80, 30, 291, 101))
        self.l_logo.setStyleSheet(u"\n"
"border-image: url(./assets/logo de ZAYCO.jpg);")

        self.retranslateUi(Dialog)
                
        if self.costo == 'costo de conversión':
            self.buttonBox.accepted.connect(self.calcular_costo_conversion)
            self.buttonBox.rejected.connect(self.closeWindows)

        elif self.costo == 'costo total de productos en proceso':
            self.buttonBox.accepted.connect(self.calcular_costo_productos_proceso)
            self.buttonBox.rejected.connect(self.closeWindows)

        elif self.costo == 'costo del producto terminado':
            self.buttonBox.accepted.connect(self.calcular_costo_producto_terminado)
            self.buttonBox.rejected.connect(self.closeWindows)

        elif self.costo == 'costo de venta':
            self.buttonBox.accepted.connect(self.calcular_costo_venta)
            self.buttonBox.rejected.connect(self.closeWindows)

        elif self.costo == 'costo total de productos terminados':
            self.buttonBox.accepted.connect(self.calcular_costo_total_productos_terminados)
            self.buttonBox.rejected.connect(self.closeWindows)

        elif self.costo == 'costo total de producción y ventas':
            self.buttonBox.accepted.connect(self.calcular_costo_total_produccion_ventas)
            self.buttonBox.rejected.connect(self.closeWindows)

        elif self.costo == 'ganancias y pérdidas':
            self.buttonBox.accepted.connect(self.calcular_ganancias_perdidas)
            self.buttonBox.rejected.connect(self.closeWindows)
        
        elif self.costo == 'costo variable por unidad':
            self.buttonBox.accepted.connect(self.calcular_costo_variable_unidad)
            self.buttonBox.rejected.connect(self.closeWindows)

        else:
            self.buttonBox.accepted.connect(self.calcular_costo_primo)
            self.buttonBox.rejected.connect(self.closeWindows)
        #TODO: Agregar más elif self.cost == 'tipo de costo':

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi


    def retranslateUi(self, Dialog):

        print(self.costo)

        if self.costo == "costo semivariable":
            #TODO: Cambiar textos
            Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Costo Semivariable", None))
            self.L_titulo.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Costo Semivariable</span></p></body></html>", None))
            self.l_valor1.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Costo Fijo:</span></p></body></html>", None))
            self.l_valor2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Costo Variable:</span></p></body></html>", None))
            self.l_logo.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><br/></p></body></html>", None))
        
        elif self.costo == "costo de conversión":
            Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Costo de Conversión", None))
            self.L_titulo.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Costo de Conversión</span></p></body></html>", None))
            self.l_valor1.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Mano de Obra Directa:</span></p></body></html>", None))
            self.l_valor2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Carga Fabril:</span></p></body></html>", None))
            self.l_logo.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><br/></p></body></html>", None))
        
        elif self.costo == "costo total de productos en proceso":
            Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Costo Total de Productos en Proceso", None))
            self.L_titulo.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Costo Total de Productos en Proceso</span></p></body></html>", None))
            self.l_valor1.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Costos de Producción:</span></p></body></html>", None))
            self.l_valor2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Costo Iv. Inicial Productos en Proceso:</span></p></body></html>", None))
            self.l_logo.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><br/></p></body></html>", None))

        elif self.costo == "costo del producto terminado":
            Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Costo del Producto Terminado", None))
            self.L_titulo.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Costo del Producto Terminado</span></p></body></html>", None))
            self.l_valor1.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Costo de Productos Proceso:</span></p></body></html>", None))
            self.l_valor2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Costo Iv. Final Productos en Proceso:</span></p></body></html>", None))
            self.l_logo.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><br/></p></body></html>", None))
            
        elif self.costo == "costo de venta":
            Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Costo de Venta", None))
            self.L_titulo.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Costo de Venta</span></p></body></html>", None))
            self.l_valor1.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Costo Total Productos Terminados:</span></p></body></html>", None))
            self.l_valor2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Costo Iv. Final Productos Terminados:</span></p></body></html>", None))
            self.l_logo.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><br/></p></body></html>", None))
        
        elif self.costo == "costo total de productos terminados":
            Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Costo Total de Productos Terminados", None))
            self.L_titulo.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Costo Total de Productos Terminados</span></p></body></html>", None))
            self.l_valor1.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Costo Producto Terminado:</span></p></body></html>", None))
            self.l_valor2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Costo Iv. Inicial Productos Terminados:</span></p></body></html>", None))
            self.l_logo.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><br/></p></body></html>", None))

        elif self.costo == "costo total de producción y ventas":
            Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Costo Total de Producción y Ventas", None))
            self.L_titulo.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Costo Total de Producción y Ventas</span></p></body></html>", None))
            self.l_valor1.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Costo de Ventas:</span></p></body></html>", None))
            self.l_valor2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Gastos de Operación:</span></p></body></html>", None))
            self.l_logo.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><br/></p></body></html>", None))
        
        elif self.costo == "ganancias y pérdidas":
            Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Ganancias y Pérdidas", None))
            self.L_titulo.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Ganancias y Pérdidas</span></p></body></html>", None))
            self.l_valor1.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Ingresos:</span></p></body></html>", None))
            self.l_valor2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Gastos:</span></p></body></html>", None))
            self.l_logo.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><br/></p></body></html>", None))
        
        elif self.costo == "costo variable por unidad":
            Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Costo Variable por Unidad", None))
            self.L_titulo.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Costo Variable por Unidad</span></p></body></html>", None))
            self.l_valor1.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Costo Variable Unitario:</span></p></body></html>", None))
            self.l_valor2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Nro. Unidades Fabricadas:</span></p></body></html>", None))
            self.l_logo.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><br/></p></body></html>", None))

        #TODO: Agregar más elif self.costo == 'tipo de costo':
       
        else:
            Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
            self.L_titulo.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Costo Primo</span></p></body></html>", None))
            self.l_valor1.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Materia Prima Directas:</span></p></body></html>", None))
            self.l_valor2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Mano de Obra Directa:</span></p></body></html>", None))
            self.l_logo.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><br/></p></body></html>", None))
        
    # retranslateUi

    def mostrarPrincipal(self):
        self._mainWindow.show()
        self.hide()

    def closeWindows(self):
        self._mainWindow.w = None
        self.close()

    def calcular_costo_primo(self):
        materia_prima_ditrecta = float(self.txt_valor1.text().strip())
        mano_obra_ditecta = float(self.txt_valor2.text().strip())

        self._controller.calcularCostoPrimo(materia_prima_ditrecta, mano_obra_ditecta)

    def calcular_costo_conversion(self):
        mano_obra_ditecta = float(self.txt_valor1.text().strip())
        carga_fabril = float(self.txt_valor2.text().strip())

        self._controller.calcularCostoConversion(mano_obra_ditecta, carga_fabril)

    def calcular_costo_semivariable(self):
        costo_fijo = float(self.txt_valor1.text().strip())
        costo_variable = float(self.txt_valor2.text().strip())

        self._controller.calcularCostoSemivariable(costo_fijo, costo_variable)

    def calcular_costo_productos_proceso(self):
        costo_produccion = float(self.txt_valor1.text().strip())
        costo_inventario_inicial = float(self.txt_valor2.text().strip())

        self._controller.calcular_costo_productos_proceso(costo_produccion, costo_inventario_inicial)

    def calcular_costo_producto_terminado(self):
        costo_producto_proceso = float(self.txt_valor1.text().strip())
        costo_inventario_final_pp = float(self.txt_valor2.text().strip())

        self._controller.calcular_costo_producto_terminado(costo_producto_proceso, costo_inventario_final_pp)

    def calcular_costo_venta(self):
        costo_total_productos_terminados = float(self.txt_valor1.text().strip())
        costo_inventario_final_productos_terminados = float(self.txt_valor2.text().strip())

        self._controller.calcular_costo_venta(costo_total_productos_terminados, costo_inventario_final_productos_terminados)

    def calcular_costo_total_productos_terminados(self):
        costo_producto_terminado = float(self.txt_valor1.text().strip())
        costo_inventario_inicial_productos_terminados  = float(self.txt_valor2.text().strip())

        self._controller.calcular_costo_total_productos_terminados(costo_producto_terminado, costo_inventario_inicial_productos_terminados)
    
    def calcular_costo_total_produccion_ventas(self):
        costo_ventas = float(self.txt_valor1.text().strip())
        gastos_operacion = float(self.txt_valor2.text().strip())

        self._controller.calcular_costo_total_produccion_ventas(costo_ventas, gastos_operacion)
    
    def calcular_ganancias_perdidas(self):
        ingresos = float(self.txt_valor1.text().strip())
        gastos = float(self.txt_valor2.text().strip())

        self._controller.calcular_ganancias_perdidas(ingresos, gastos)

    def calcular_costo_variable_unidad(self):
        costo_variable_unitario = float(self.txt_valor1.text().strip())
        numero_unidades_fabricadas = float(self.txt_valor2.text().strip())

        self._controller.calcular_costo_variable_unidad(costo_variable_unitario, numero_unidades_fabricadas)





   

    
