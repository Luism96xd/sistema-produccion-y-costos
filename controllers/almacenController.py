import utils.mvc_exceptions as mvc_exceptions
from utils.database import DB

class AlmacenController():
    def __init__(self, view, model):
        self._almacenes = {}
        self.db = DB()
        self.model = model
        self.view = view
    
    #Typically the MVC pattern would have a main class instantiating both view and controller, 
    #The view would receive a reference to the controller. (assignController)
    #Don't have the controller instantiating the view.

    def get_warehouses(self):
        warehouses = self.model.getWarehouses()
        return warehouses
    
    def select_warehouse_by_id(self, warehouse_id):
        warehouse = self.model.getWarehouseById(warehouse_id)
        return warehouse
    
    def create_warehouse(self, name, description, location):
        try:         
            if (name == '' or description == '' or location == ''):
                self.view.display_empty_fields_error()
                return False
            else:
                response = self.model.createWarehouse(name, description, location)
                if response == True:
                    self.view.display_item_stored('Almacén', name)
                    self.view.mostrarPrincipal()
        except mvc_exceptions.ItemAlreadyStored as e:
            print(e)
            self.view.display_item_already_stored_error('Almacén', name, e)
    
    def search_warehouse(self, name, location):
        filters = {
            'nombre': name,
            'ubicacion': location,
        }
        try:
            warehouses = self.db.select_all('tbl_almacenes', filters=filters)
            self.view.updateView(warehouses)
            return True
        except mvc_exceptions.ItemNotStored as e:
            print(e)

    def update_warehouse(self, name, description, location, warehouse_id):
        if name != '' and description != '' and location != '':
            response = self.model.updateWarehouse(name, description, location, warehouse_id)
            if response == True:
                self.view.display_message('Operación exitosa', 'Almacén actualizado satisfactoriamente')
                warehouses = self.get_warehouses()
                self.view.updateView(warehouses)
                self.view.mostrarPrincipal()
        else:
            self.view.display_empty_fields_error()
            response = False
        return response
    
    def delete_warehouse_by_id(self, warehouse_id):
        try:
            name = self.model.getName(warehouse_id)
            confirmation = self.view.display_delete_confirmation('Almacén', name)
            if confirmation == True:
                response = self.model.delete_warehouse_by_id(warehouse_id)
                if response == True:
                    warehouses = self.get_warehouses()
                    self.view.updateView(warehouses)
                    self.view.display_message('Almacén eliminado', f'El Almacén con el nombre {name} ha sido eliminado satisfactoriamente')
                    print(f'El Almacén {name} ha sido eliminado satisfactoriamente')
                    return True
        except mvc_exceptions.ItemNotStored as e:
            print(e)

    def delete_warehouse_by_name(self, name):
        try:
            confirmation = self.view.display_delete_confirmation('Almacén', name)
            if confirmation == True:
                response = self.model.delete_warehouse_by_name(name)
                if response == True:
                    warehouses = self.get_warehouses()
                    self.view.updateView(warehouses)
                    self.view.display_message('Almacén eliminado', f'El Almacén con el nombre {name} ha sido eliminado satisfactoriamente')
                    print(f'El Almacén {name} ha sido eliminado satisfactoriamente')
                    return True
                else:
                    self.view.display_message('Operación fallida', 'Ocurrió un error durante la eliminación')

        except mvc_exceptions.ItemNotStored as e:
            print(e)

    def create_location(self, rack, side, level):
        try:         
            if (rack == '' or side == '' or level == ''):
                self.view.display_empty_fields_error()
                return False
            else:
                response = self.model.createLocation(rack, side, level)
                if response == True:
                    self.view.display_item_stored('Ubicación', f'{rack}-{side}-{level}')
                    self.view.mostrarPrincipal()
        except mvc_exceptions.ItemAlreadyStored as e:
            print(e)
            self.view.display_item_already_stored_error('Almacén', f'{rack}-{side}-{level}', e)
    