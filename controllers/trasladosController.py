import utils.mvc_exceptions as mvc_exceptions
from utils.database import DB
from datetime import datetime
from models.almacen import Almacen
from models.cargo import Cargo
from models.descargo import Descargo
from models.product import Product

class TrasladosController():
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

    def validate_data(self, product, origin, destination, quantity):
        productIsNotNull     = product['index'] != None
        originIsNotNull      = origin['index'] != None
        destinationIsNotNull = destination['index'] != None

        if (productIsNotNull and originIsNotNull and destinationIsNotNull and quantity > 0):
            return True
        else:
            return False

    def get_combo_data(self, product, origin, destination):
        if product['name'] != None:
            product_id = self.getProductIdByName(product['name'])
        else:
            product_id = None

        if origin['name'] != None:
            origin_id = self.getWarehouseIdByName(origin['name'])
        else:
            origin_id = None

        if destination['name'] != None:
            destination_id = self.getWarehouseIdByName(destination['name'])
        else:
            destination_id = None
        return product_id, origin_id, destination_id

    
    def register_transfer(self, product, origin, destination, quantity):
        try:     
            creation_date = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
            product_id, origin_id, destination_id = self.get_combo_data(product, origin, destination)

            if (self.validate_data(product, origin, destination, quantity)):
                descargo = Descargo()
                stock = descargo.verify_stock(product_id, origin_id)

                if stock >= quantity:
                    response_1 = descargo.add_warehouse_unload(product_id, origin_id, quantity, creation_date)
                
                    if response_1 == True:
                        cargo = Cargo()
                        response_2 = cargo.add_warehouse_load(product_id, destination_id, quantity, creation_date)
                    
                    if response_2 == True:
                        response_3 = self.model.register_transfer(product_id, origin_id, destination_id, quantity, creation_date)
    
                    if response_3 == True: 
                        almacen = Almacen()
                        almacen_origen = almacen.getWarehouseById(origin_id)[1]
                        almacen_destino = almacen.getWarehouseById(destination_id)[1]
                        self.view.display_message('Traslado registrado', f'{quantity} unidades fueron trasladadas desde el {almacen_origen} al {almacen_destino}')
                        self.view.mostrarPrincipal()
                        print("Traslado registado")
                        return True
                else:
                    self.view.display_message('Operación fallida', 'No hay cantidades suficientes para descargar. Existencias: ' + str(stock))

            else:
                self.view.display_empty_fields_error()
                return False
        except mvc_exceptions.ItemAlreadyStored as e:
            print(e)
            self.view.display_item_already_stored_error('Traslado', product['name'], e)

    def getTransfersList(self):
        result = self.model.get_transfers_list()
        return result

