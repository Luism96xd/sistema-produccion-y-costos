from PySide6.QtWidgets import QMenuBar, QMenu
from PySide6.QtGui import QAction
from PySide6.QtCore import QRect, QCoreApplication
from models.descargo import Traslado
from models.product import Product
from models.almacen import Almacen
from models.categoria import Categoria
from controllers.productController import ProductController
from controllers.almacenController import AlmacenController
from controllers.trasladosController import TrasladosController
from controllers.movimientosController import MovimientosController
from views.almacenes.ui_viewMovimientoAlmacen import ViewMovimientoAlmacen
from reportes.export_products_pdf import exportar_pdf_productos
from reportes.export_perishables_pdf import exportar_pdf_perecederos

class Menu(QMenuBar):
    def __init__(self, MainWindow, empresa):
        super().__init__(MainWindow)
        self.root = MainWindow
        self.w = None
        self.empresa = empresa

        self.setupUi(self.root)

    def setupUi(self, MainWindow):
        #Actions
        self.actionEditCompany = QAction(MainWindow)
        self.actionEditCompany.setObjectName(u"actionEditCompany")
        self.actionEditCompany.triggered.connect(self.show_edit_company_window)

        self.actionCreateAccount = QAction(MainWindow)
        self.actionCreateAccount.setObjectName(u"actionCreateAccount")
        self.actionCreateAccount.triggered.connect(self.show_create_account_window)

        self.actionAdd_Product = QAction(MainWindow)
        self.actionAdd_Product.setObjectName(u"actionAdd_Product")
        self.actionAdd_Product.triggered.connect(self.show_add_product_window)

        self.actionSearch_Products = QAction(MainWindow)
        self.actionSearch_Products.setObjectName(u"actionSearch_Products")
        self.actionSearch_Products.triggered.connect(self.show_products_list_window)

        self.actionPerishables = QAction(MainWindow)
        self.actionPerishables.setObjectName(u"actionPerishables")
        self.actionPerishables.triggered.connect(self.show_perishables_list_window)

        self.actionCreateCategory = QAction(MainWindow)
        self.actionCreateCategory.setObjectName(u"actionCreateCategory")
        self.actionCreateCategory.triggered.connect(self.show_create_category_window)

        self.actionAdd_Warehouse = QAction(MainWindow)
        self.actionAdd_Warehouse.setObjectName(u"actionAdd_Warehouse")
        self.actionAdd_Warehouse.triggered.connect(self.show_add_warehouse_window)

        self.actionWarehouse_List = QAction(MainWindow)
        self.actionWarehouse_List.setObjectName(u"actionWarehouse_List")
        self.actionWarehouse_List.triggered.connect(self.show_warehouse_list_window)

        self.actionLoad_Merchandise = QAction(MainWindow)
        self.actionLoad_Merchandise.setObjectName(u"actionLoad_Merchandise")
        self.actionLoad_Merchandise.triggered.connect(self.show_load_merchandise_window)
        
        self.actionUnload_Merchandise = QAction(MainWindow)
        self.actionUnload_Merchandise.setObjectName(u"actionUnload_Merchandise")
        self.actionUnload_Merchandise.triggered.connect(self.show_unload_merchandise_window)

        self.actionSearch_Transfers = QAction(MainWindow)
        self.actionSearch_Transfers.setObjectName(u"actionSearch_Transfers")
        self.actionSearch_Transfers.triggered.connect(self.show_transfers_list_window)

        self.actionRegister_Transfer = QAction(MainWindow)
        self.actionRegister_Transfer.setObjectName(u"actionRegister_Transfer")
        self.actionRegister_Transfer.triggered.connect(self.show_register_transfer_window)

        self.actionCalc_Cost_Product = QAction(MainWindow)
        self.actionCalc_Cost_Product.setObjectName(u"action_Calculate_Cost_Product")
        self.actionCalc_Cost_Product.triggered.connect(self.show_cost_window)

        self.actionCreate_Products_PDF = QAction(MainWindow)
        self.actionCreate_Products_PDF.setObjectName(u"action_Calculate_Cost_Product")
        self.actionCreate_Products_PDF.triggered.connect(exportar_pdf_productos)

        self.actionPerecederos_PDF = QAction(MainWindow)
        self.actionPerecederos_PDF.setObjectName(u"actionPerecederos_PDF")
        self.actionPerecederos_PDF.triggered.connect(exportar_pdf_perecederos)

        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionExit.triggered.connect(self.closeWindow)

        #MenuBar
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        #Menus
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuProductos = QMenu(self.menubar)
        self.menuProductos.setObjectName(u"menuProductos")
        self.menuAlmacenes = QMenu(self.menubar)
        self.menuAlmacenes.setObjectName(u"menuAlmacenes")
        self.menuReportes = QMenu(self.menubar)
        self.menuReportes.setObjectName(u"menuReportes")
        #
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuProductos.menuAction())
        self.menubar.addAction(self.menuAlmacenes.menuAction())
        self.menubar.addAction(self.menuReportes.menuAction())
        #
        self.menuArchivo.addAction(self.actionEditCompany)
        self.menuArchivo.addAction(self.actionCreateAccount)
        self.menuArchivo.addAction(self.actionExit)
        
        self.menuProductos.addAction(self.actionAdd_Product)
        self.menuProductos.addAction(self.actionSearch_Products)
        self.menuProductos.addAction(self.actionPerishables)
        self.menuProductos.addAction(self.actionCreateCategory)
        self.menuProductos.addAction(self.actionCalc_Cost_Product)
        
        self.menuAlmacenes.addAction(self.actionAdd_Warehouse)
        self.menuAlmacenes.addAction(self.actionWarehouse_List)
        self.menuAlmacenes.addAction(self.actionLoad_Merchandise)
        self.menuAlmacenes.addAction(self.actionUnload_Merchandise)
        self.menuAlmacenes.addAction(self.actionSearch_Transfers)
        self.menuAlmacenes.addAction(self.actionRegister_Transfer)
        
        self.menuReportes.addAction(self.actionCreate_Products_PDF)
        self.menuReportes.addAction(self.actionPerecederos_PDF)
        
        self.retranslateUi(self)
    #setupUi
    
    def retranslateUi(self, MainWindow):
        self.actionEditCompany.setText(QCoreApplication.translate("MainWindow", u"Datos de la Empresa", None))
        self.actionCreateAccount.setText(QCoreApplication.translate("MainWindow", u"Crear cuentas de usuario", None))
        self.actionAdd_Product.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir Producto", None))
        self.actionSearch_Products.setText(QCoreApplication.translate("MainWindow", u"Consultar Productos", None))
        self.actionPerishables.setText(QCoreApplication.translate("MainWindow", u"Productos Perecederos", None))
        self.actionCreateCategory.setText(QCoreApplication.translate("MainWindow", u"Crear Categoría", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Configurar", None))
        self.menuProductos.setTitle(QCoreApplication.translate("MainWindow", u"Productos", None))
        self.menuAlmacenes.setTitle(QCoreApplication.translate("MainWindow", u"Almacenes", None))
        self.actionAdd_Warehouse.setText(QCoreApplication.translate("MainWindow", u"Crear Almacenes", None))
        self.actionWarehouse_List.setText(QCoreApplication.translate("MainWindow", u"Lista de Almacenes", None))
        self.actionLoad_Merchandise.setText(QCoreApplication.translate("MainWindow", u"Registrar cargo de inventario", None))
        self.actionUnload_Merchandise.setText(QCoreApplication.translate("MainWindow", u"Registrar descargo de inventario", None))
        self.actionRegister_Transfer.setText(QCoreApplication.translate("MainWindow", u"Registrar traslado", None))
        self.actionSearch_Transfers.setText(QCoreApplication.translate("MainWindow", u"Consultar traslados", None))
        self.actionCalc_Cost_Product.setText(QCoreApplication.translate("MainWindow", u"Calcular costos", None))
        self.menuReportes.setTitle(QCoreApplication.translate("MainWindow", u"Reportes", None))
        self.actionCreate_Products_PDF.setText(QCoreApplication.translate("MainWindow", u"Lista de Productos (PDF)", None))
        self.actionPerecederos_PDF.setText(QCoreApplication.translate("MainWindow", u"Lista de Productos Perecederos (PDF)", None))

    # retranslateUi 

    def show_add_product_window(self):
        from views.productos.ui_viewAgregarProductos import viewAgregarProductos
        if self.w is None:
            model = Product()
            self.w = viewAgregarProductos(self)
            self._controller = ProductController(self.w, model)
            self.w.assignController(self._controller)
            self.w.show()
        else:
            self.w.close() 
            self.w = None
    
    def show_products_list_window(self, selected_item=None):
        from views.productos.ui_viewListaProductos import viewListaProductos
        if self.w is None:
            model = Product()
            self.w = viewListaProductos(self)
            self._controller = ProductController(self.w, model)
            self.w.assignController(self._controller)
            self.w.show()
        else:
            self.w.close() 
            self.w = None

    def show_perishables_list_window(self, selected_item=None):
        from views.productos.ui_viewListaProductosPerecederos import ViewListaProductosPerecederos
        if self.w is None:
            model = Product()
            self.w = ViewListaProductosPerecederos(self)
            self._controller = ProductController(self.w, model)
            self.w.assignController(self._controller)
            self.w.show()
        else:
            self.w.close() 
            self.w = None

    def show_create_category_window(self):
        from views.categorias.ui_viewCategoria import ViewCategoria
        if self.w is None:
            model = Categoria()
            self.w = ViewCategoria(self)
            self._controller = ProductController(self.w, model)
            self.w.assignController(self._controller)
            self.w.show()
        else:
            self.w.close() 
            self.w = None

    def show_add_warehouse_window(self):
        from views.almacenes.ui_viewCrearAlmacenes import viewCrearAlmacen
        if self.w is None:
            model = Almacen()
            self.w = viewCrearAlmacen(self)
            self._controller = AlmacenController(self.w, model)
            self.w.assignController(self._controller)
            self.w.show()
        else:
            self.w.close() 
            self.w = None
            
    def show_warehouse_list_window(self):
        from views.almacenes.ui_viewListaAlmacenes import viewListaAlmacenes
        if self.w is None:
            model = Almacen()
            self.w = viewListaAlmacenes(self)
            self._controller = AlmacenController(self.w, model)
            self.w.assignController(self._controller)
            self.w.show()
        else:
            self.w.close() 
            self.w = None

    def show_load_merchandise_window(self):
        from models.cargo import Cargo
        if self.w is None:
            model = Cargo()
            self.w = ViewMovimientoAlmacen(self, 'cargo')
            self._controller = MovimientosController(self.w, model)
            self.w.assignController(self._controller)
            self.w.show()
        else:
            self.w.close() 
            self.w = None

    def show_unload_merchandise_window(self):
        from models.descargo import Descargo
        if self.w is None:
            model = Descargo()
            self.w = ViewMovimientoAlmacen(self, 'descargo')
            self._controller = MovimientosController(self.w, model)
            self.w.assignController(self._controller)
            self.w.show()
        else:
            self.w.close() 
            self.w = None
    
    def show_register_transfer_window(self):
        from views.ui_viewRegistarTraslado import ViewRegistarTraslado
        if self.w is None:
            model = Traslado()
            self.w = ViewRegistarTraslado(self)
            self._controller = TrasladosController(self.w, model)
            self.w.assignController(self._controller)
            self.w.show()
        else:
            self.w.close() 
            self.w = None
            
    def show_transfers_list_window(self):
        from views.ui_viewListaMovimientosAlmacen import ViewListaMovimientosAlmacen
        if self.w is None:
            model = Traslado()
            self.w = ViewListaMovimientosAlmacen(self)
            self._controller = TrasladosController(self.w, model)
            self.w.assignController(self._controller)
            self.w.show()
        else:
            self.w.close() 
            self.w = None
                    
    def show_cost_window(self):
        from models.costos import Costos
        from views.costos.ui_viewCostos import ViewCostos 
        if self.w is None:
            model = Costos()
            self.w = ViewCostos(self, self.empresa)
            self._controller = ProductController(self.w, model)
            self.w.assignController(self._controller)
            self.w.show()
        else:
            self.w.close() 
            self.w = None

    def show_edit_company_window(self):
        from models.empresa import Empresa
        from controllers.empresaController import EmpresaController
        from views.ui_viewEditarEmpresa import ViewEditarEmpresa
        if self.w is None:
            model = Empresa()
            self.w = ViewEditarEmpresa(self, self.empresa)
            self._controller = EmpresaController(self.w, model)
            self.w.assignController(self._controller)
            self.w.show()
        else:
            self.w.close() 
            self.w = None

    def show_create_account_window(self):
        self._controller = None
        from models.usuario import Usuario
        from controllers.usuariosController import UsuariosController
        from views.ui_ViewCrearEditarCuentas import ViewCrearCuentas
        if self.w is None:
            model = Usuario()
            self.w = ViewCrearCuentas(self, self.empresa)
            self._controller = UsuariosController(self.w, model)
            self.w.assignController(self._controller)
            self.w.show()
        else:
            self.w.close() 
            self.w = None

    def create_products_pdf(self):
        creating = False
        if creating != True:

            creating = True

    def closeWindow(self):
        self.w = None
        self.root.close()