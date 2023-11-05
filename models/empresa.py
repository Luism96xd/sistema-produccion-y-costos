from models.model import Model
import os

class Empresa(Model):
    def __init__(self, nombre="Empresa"):
        super().__init__(self)
        self._id = ''
        self.nombre = nombre
        self.RIF = ''
        self.direccion1 = ''
        self.direccion2 = ''
        self.telefono1 = ''
        self.ciudad = ''
        self.estado =''
        self.logo = ''

    def getEmpresa(self):
        empresa = self.db.select_all('tbl_empresa', filters={'casa_matriz': 1})[0]
        self._id = empresa[0]if empresa[0] != None else ''
        self.nombre = empresa[1] if empresa[1] != None else ''
        self.RIF = empresa[2] if empresa[2] != None else ''
        self.logo = empresa[3] if empresa[3] != None else ''
        self.telefono1 = empresa[4] if empresa[4] != None else ''
        self.direccion1 = empresa[5] if empresa[5] != None else ''
        self.direccion2 = empresa[6] if empresa[6] != None else ''
        self.ciudad = empresa[7] if empresa[7] != None else ''
        self.estado = empresa[8] if empresa[8] != None else ''
        return self

    def getLogo(self):
        ROOT_DIR = "./" #os.path.join(".", os.path.pardir)
        if self.logo != None:
            self.logo = os.path.join(ROOT_DIR, self.logo)
        print(self.logo)
        return self.logo

    def getName(self):
        return self.nombre

    def getRIF(self):
        return self.RIF

    def getId(self):
        return self._id

    def getDireccion1(self):
        return self.direccion1
    
    def getDireccion2(self):
        return self.direccion2
 
    def getTelefono1(self):
        return self.telefono1

    def getCiudad(self):
        return self.ciudad

    def getEstado(self):
        return self.estado

    def update_empresa(self, nombre, rif, telefono1, direccion1, direccion2, logo, ciudad, estado, id_empresa):
        items_to_update = {
            'nombre_empresa': nombre,
            'rif': rif,
            'logo': logo,
            'telefono1': telefono1,
            'direccion1': direccion1,
            'direccion2': direccion2,
            'ciudad': ciudad,
            'estado': estado
        }
        response = self.db.update_one('tbl_empresa', items_to_update, 'id_empresa', id_empresa)
        return response