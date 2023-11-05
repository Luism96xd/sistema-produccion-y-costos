from utils.database import DB

class EmpresaController():
    def __init__(self, view, model):
        self.db = DB()
        self.model = model
        self.view = view

    def editar_empresa(self, nombre, rif, telefono1, direccion1, direccion2, logo, ciudad, estado, id_empresa):
        print(id_empresa)
        if id_empresa != None and nombre != None and rif != None:
            response = self.model.update_empresa(nombre, rif, telefono1, direccion1, direccion2, logo, ciudad, estado, id_empresa)
            
            if response == True:
                self.view.display_message('Operación exitosa', 'Los datos de la empresa han sido actualizados correctamente')
            
            else:
                self.view.display_message('Operación fallida', 'Hubo un error. Intente de nuevo')