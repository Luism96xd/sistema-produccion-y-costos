import utils.mvc_exceptions as mvc_exceptions
from utils.database import DB
from datetime import datetime
from models.product import Product

class ProductController:
    def __init__(self, view=None, model=None):
        self._productos = {}
        self.db = DB()
        self.view = view
        self.model = model

    def getAllProducts(self):
        products = self.db.select("tbl_subproductos")
        return products
    
    def getProduct(self, name):
        products = self.db.select_one("tbl_subproductos")
        return products

    def getProductNames(self):
        products = self.model.getProductNames()
        return products

    def add_product(self, name, description, cost, quantity, creation_date, parent, entry_date, expiration_date, id_empresa):
        try:         
            if (name == '' or description == '' or quantity < 0 or cost < 0 or parent['index'] == 0):
                self.view.display_empty_fields_error()
                return False
            else:
                if parent['name'] != None:
                    parent_id = self.model.getProductIdByName(parent['name'])
                else:
                    parent_id = None

                response = self.model.create_product(name, description, cost, quantity, creation_date, parent_id, entry_date, expiration_date, id_empresa)
                if response == True:
                    last_id = self.model.getLastProduct()
                    self.update_parent_cost(last_id)
                    self.view.display_item_stored('Producto', name)
                    products = self.getAllProducts()
                    self.view.updateView(products)
                    self.view.mostrarPrincipal()
                    print('Producto añadido')
                    return True
        except mvc_exceptions.ItemAlreadyStored as e:
            print(e)
            self.view.display_item_already_stored_error('Producto', name, e)

    def updateProduct(self, product_id, name, description, quantity, cost, parent):
        date   = datetime.today().strftime("%Y-%m-%d %H:%M:%S") 

        if parent['index'] != 0:
            parent_id = self.model.getProductIdByName(parent['name'])
        else:
            parent_id = None
        if name != '' and description != '' and quantity > 0:
            response = self.model.update_product(product_id, name, description, quantity, cost, date, parent_id)
            if response == True:
                self.view.display_message('Operación exitosa', 'Almacén actualizado satisfactoriamente')
                products = self.getAllProducts()
                self.view.updateView(products)
                self.view.mostrarPrincipal()
        else:
            self.view.display_empty_fields_error()
            response = False
        return response

    def search_product(self, name, parent):
        filters = dict()
        if parent != None:
            id = self.db.select_one('id_subproducto', 'tbl_subproductos', {'nombre_producto': parent})
            filters['id_producto'] = id
        
        if name != None:
            filters['nombre_producto'] = name

        try:
            products = self.db.select_all('tbl_subproductos', filters=filters)
            self.view.updateView(products)
            return True
        except mvc_exceptions.ItemNotStored as e:
            print(e)
            self.view.display_not_stored_error('Producto', name, e)
    
    def search_product_by_name(self, name):
        filters = {
            'nombre_producto': name,
        }
        try:
            products = self.db.select_all('tbl_subproductos', filters=filters)
            self.view.updateView(products)
            return True
        except mvc_exceptions.ItemNotStored as e:
            print(e)
            self.view.display_not_stored_error(name, e)
    
    def search_product_by_code(self, code):
        filters = {
            'codigo_producto': code,
        }
        try:
            products = self.db.select_all('tbl_subproductos', filters=filters)
            self.view.updateView(products)
            return True
        except mvc_exceptions.ItemNotStored as e:
            print(e)
            self.view.display_not_stored_error(code, e)
    
    def search_product_by_mark(self, mark):
        filters = {
            'marca': mark,
        }
        try:
            products = self.db.select_all('tbl_subproductos', filters=filters)
            self.view.updateView(products)
            return True
        except mvc_exceptions.ItemNotStored as e:
            print(e)
            self.view.display_not_stored_error(mark, e)

    def search_product_by_model(self, model):
        filters = {
            'modelo': model,
        }
        try:
            products = self.db.select_all('tbl_subproductos', filters=filters)
            self.view.updateView(products)
            return True
        except mvc_exceptions.ItemNotStored as e:
            print(e)
            self.view.display_not_stored_error(model, e)
    
    def select_product_by_id(self, product_id):
        product = self.model.getProductById(product_id)
        return product

    def delete_product_by_id(self, product_id):
        try:
            name = self.model.getName(product_id)
            confirmation = self.view.display_delete_confirmation('Producto', name)
            if confirmation == True:
                response = self.model.delete_product_by_id(product_id)
                if response == True:
                    products = self.getAllProducts()
                    self.view.updateView(products)
                    self.view.display_message('Producto eliminado', f'El producto {name} ha sido eliminado satisfactoriamente')
                    print(f'Producto {name} ha sido eliminado satisfactoriamente')
                    return True
        except mvc_exceptions.ItemNotStored as e:
            print(e)

    def delete_product_by_name(self, name):
        try:
            confirmation = self.view.display_delete_confirmation('Producto', name)
            if confirmation == True:
                response = self.model.delete_product_by_name(name)
                if response == True:
                    products = self.getAllProducts()
                    self.view.updateView(products)
                    self.view.display_message('Producto eliminado', f'El producto {name} ha sido eliminado satisfactoriamente')
                    print(f'Producto {name} ha sido eliminado satisfactoriamente')
                    return True
        except mvc_exceptions.ItemNotStored as e:
            print(e)

    def update_parent_cost(self, last_id):
        modified_date = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        parent_id = self.model.getParentIdById(last_id)

        if(parent_id != None):
            self.model.updateCost(modified_date, parent_id, last_id)
            self.update_parent_cost(parent_id)

