from models.model import Model

class Almacen(Model):
    def __init__(self, name="Almacén", description="", location=""):
        super().__init__(self)
        self.name = name
        self.description = description
        self.location = location

    def createWarehouse(self, name, description, location):
        assert name != '', 'name must not be empty'
        assert description != '', 'description must not be empty'
        assert location != '', 'location must not be empty'

        columns = ['nombre', 'descripcion', 'ubicacion']
        response = self.db.insert_one('tbl_almacenes', columns, name, description, location)
        return response
    
    def updateWarehouse(self, name, description, location, warehouse_id):
        items_to_update = {
            'nombre': name,
            'descripcion': description,
            'ubicacion': location
        }
        response = self.db.update_one('tbl_almacenes', items_to_update, 'id_almacen', warehouse_id)
        return response

    def delete_warehouse_by_name(self, warehouse_id):
        assert warehouse_id != None, "El ID del almacén no puede ser nulo"
        response = self.db.delete_one('tbl_almacenes', ['id_almacen'], warehouse_id)
        return response

    def delete_warehouse_by_name(self, name):
        assert name != '', "El nombre del almacén no puede ser nulo"
        response = self.db.delete_one('tbl_almacenes', ['nombre'], name)
        return response

    def getWarehouses(self):
        almacenes = self.db.select('tbl_almacenes',filters={'id_empresa': 1})
        return almacenes

    def getWarehousesNames(self):
        almacenes = self.db.select_all('tbl_almacenes','nombre')
        almacenes = [item[0] for item in almacenes]
        return almacenes

    def getWarehouseById(self, warehouse_id):
        filters = {
            'id_almacen': warehouse_id,
        }
        result = self.db.select_all('tbl_almacenes', filters=filters)[0]
        return result
    
    def getWarehouseIdByName(self, name):
        filters = {
            'nombre': name,
        }
        warehouse_id = self.db.select_one('id_almacen', 'tbl_almacenes', filters)
        return warehouse_id

    def getName(self, warehouse_id):
        filters = {
            'id_almacen': warehouse_id,
        }
        self.name = self.db.select_one('nombre', 'tbl_almacenes', filters)
        return self.name

    def getDescription(self):
        return self.description
    
    def getLocation(self):
        return self.location
    
    def setName(self, name):
        self.name = name

    def getDescription(self, description):
        self.description = description
    
    def setLocation(self, location):
        self.location = location

    def createLocation(self, rack, side, level):
        assert rack != '', 'rack must not be empty'
        assert side != '', 'side must not be empty'
        assert level != '', 'level must not be empty'

        columns = ['rack', 'side', 'level']
        response = self.db.insert_one('tbl_ubicaciones_almacen', columns, rack, side, level)
        return response      
