import utils.mvc_exceptions as mvc_exceptions
from utils.database import DB
from datetime import datetime
from models.almacen import Almacen
from models.product import Product

class MovimientosController():
    def __init__(self, view, model):
        self._traslados = {}
        self.db = DB()
        self.model = model
        self.view = view

    def getProductNames(self):
        producto = Product()
        return producto.getProductNames()

    def getProductIdByName(self, name):
        producto = Product()
        return producto.getProductIdByName(name)

    def getWarehousesNames(self):
        almacen = Almacen()
        return almacen.getWarehousesNames()
    
    def getWarehouseIdByName(self, name):
        almacen = Almacen()
        return almacen.getWarehouseIdByName(name)

    def validate_data(self, product, warehouse, quantity):
        productIsNotNull     = product['index'] != None
        warehouseIsNotNull   = warehouse['index'] != None

        if (productIsNotNull and warehouseIsNotNull and quantity > 0):
            return True
        else:
            return False

    def get_combo_data(self, product, warehouse):
        if product['name'] != None:
            product_id = self.getProductIdByName(product['name'])
        else:
            product_id = None

        if warehouse['name'] != None:
            warehouse_id = self.getWarehouseIdByName(warehouse['name'])
        else:
            warehouse_id = None
        return product_id, warehouse_id


    def register_load(self, product, warehouse, quantity):
        try:     
            creation_date = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
            product_id, warehouse_id = self.get_combo_data(product, warehouse)
            if (product_id != None and warehouse_id != None and quantity > 0):
                response =  self.model.add_warehouse_load(product_id, warehouse_id, quantity, creation_date)
                if response == True:
                    self.view.display_item_stored('Cargo', product['name'])
                    self.view.mostrarPrincipal()
                    print("Cargo registado")
                    return True
            else:
                self.view.display_empty_fields_error()
                return False

        except mvc_exceptions.ItemAlreadyStored as e:
            print(e)
            self.view.display_item_already_stored_error('Cargo', product['name'], e)
        
    def register_unload(self, product, warehouse, quantity):
        try:     
            creation_date = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
            product_id, warehouse_id = self.get_combo_data(product, warehouse)
            stock = self.model.verify_stock(product_id, warehouse_id)

            if(product_id != None and warehouse_id != None and quantity > 0):
                if stock >= quantity:
                    response =  self.model.add_warehouse_unload(product_id, warehouse_id, quantity, creation_date)
                else:
                    print("No hay cantidades suficientes para descargar. Existencias: ", stock)
                    self.view.display_message('Operación fallida', 'No hay cantidades suficientes para descargar. Existencias: ' + str(stock))
                    return False
                if response == True:
                    self.view.display_item_stored('Descargo', product['name'])
                    self.view.mostrarPrincipal()
                    print("Descargo registado")
                    return True
            else:
                self.view.display_empty_fields_error()
                return False
        
        except mvc_exceptions.ItemAlreadyStored as e:
            print(e)
            self.view.display_item_already_stored_error('Descargo', product['name'], e)
        

