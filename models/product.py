from models.model import Model
from utils.database import DB

class Product(Model):
    def __init__(self, name='Producto', quantity=1, cost=0, tipo='', description=None, parent=None, image=None, entry_date = None, expiration_date = None, lifetime=30):
        super().__init__(self)
        self.parent = parent
        self.name = name
        self.description = description
        self.quantity = quantity
        self.cost = cost
        self.tipoCosto = tipo
        self.productImage = image
        self.lifetime = lifetime
        self.entry_date = entry_date
        self.expiration_date = expiration_date
    
    def create_product(self, name, description, cost, quantity, creation_date, parent, entry_date, expiration_date, company_id):
        assert cost >= 0, 'price must be greater or equal than 0'
        assert quantity >= 0, 'quantity must be greater than or equal to 0'
    
        columns  = ['nombre_producto, descripcion, cantidad, costo_unitario, fecha_creacion, id_producto', 'fecha_ingreso', 'fecha_vencimiento', 'id_empresa']
        values = [name, description, cost, quantity, creation_date, parent, entry_date, expiration_date, company_id]
        response = self.db.insert_one('tbl_subproductos', columns, values)
        return response
    
    def update_product(self, product_id, name, description, quantity, cost, modified_date, parent_id=None):
        items_to_update = {
            'id_producto': parent_id,
            'nombre_producto': name,
            'descripcion': description,
            'cantidad': quantity,
            'costo_unitario': cost,
            'fecha_modificacion': modified_date,
        }
        response = self.db.update_one('tbl_subproductos', items_to_update, 'id_subproducto', product_id)
        return response

    def delete_product_by_id(self, product_id): 
        filters = ['id_subproducto']
        response = self.db.delete_one('tbl_subproductos', filters, product_id)
        return response

    def delete_product_by_name(self, item_name): 
        filters = ['nombre_producto']
        response = self.db.delete_one('tbl_subproductos', filters, item_name)
        return response

    def getProductById(self, product_id):
        filters = {
            'id_subproducto': product_id,
        }
        result = self.db.select_all('tbl_subproductos', filters=filters)[0]
        return result

    def getName(self, product_id):
        self.name = self.db.select_one('nombre_producto', 'tbl_subproductos', {'id_subproducto': product_id})
        return self.name

    def setName(self, name):
        self.name = name

    def getTipoCosto(self):
        return self.tipoCosto

    def setTipoCosto(self, tipoCosto):
        self.tipoCosto = tipoCosto

    def getQuantity(self):
        return self.quantity

    def setQuantity(self, quantity):
        self.quantity = quantity

    def getCost(self, id):
        self.cost = self.db.select_one('costo_unitario', 'tbl_subproductos', {'id_subproducto': id})
        return self.cost

    def setCost(self, cost, id=None):
        self.cost = cost
        self.db.update_one('tbl_subproductos', {'costo_unitario': cost}, 'id_subproducto', id)

    def getProductNames(self):
        products = self.db.select_all("tbl_subproductos",'nombre_producto')
        products = [item[0] for item in products]
        return products

    def getProductIdByName(self, name):
        filters = {
            'nombre_producto': name,
        }
        product_id = self.db.select_one('id_subproducto', 'tbl_subproductos', filters)
        return product_id

    def getLastProduct(self):
        product_id = self.db.select_one('MAX(id_subproducto)', 'tbl_subproductos')
        return product_id

    def getParentIdById(self, id):
        filters = {
            'id_subproducto': id,
        }
        parent_id = self.db.select_one('id_producto', 'tbl_subproductos', filters)
        return parent_id

    def updateCost(self, modified_date, parent_id, last_id):
        #prev_cost = self.getCost(parent_id) if self.getCost(parent_id) > 0 else 0
        #print("Costo anterior: ", prev_cost)
        unit_cost = self.db.select_one("SUM(costo_unitario)", "tbl_subproductos", {'id_producto': parent_id})
        cost = self.db.select_one("SUM(cantidad * costo_unitario)", "tbl_subproductos", {'id_producto': parent_id})
        #print("Nuevo costo: ", cost)
        items_to_update = {
            'costo_unitario': unit_cost,
            'costo_total': cost,
            'fecha_modificacion': modified_date,
        }
        self.db.update_one('tbl_subproductos', items_to_update, 'id_subproducto', parent_id)

        cost = self.db.select_one("SUM(cantidad * costo_unitario)", "tbl_subproductos", {'id_subproducto': last_id})
        items_to_update = {
            'costo_total': cost,
        }
        self.db.update_one('tbl_subproductos', items_to_update, 'id_subproducto', last_id)

    @staticmethod
    def get_all():
        db = DB()
        return db.select("tbl_subproductos")
