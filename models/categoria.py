from models.model import Model
from utils.database import DB

class Categoria(Model):
    def __init__(self, name='', description=''):
        super().__init__(self)
        self.name = name
        self.description = description

    def getName(self):
        return self.name
    
    def setName(self, name: str):
        self.name = name

    @staticmethod
    def get_name_by_id(id):
        db = DB()
        categoria = db.select('tbl_categoria_producto', fields=['nombre'], filters={'id_categoria': id})
        return categoria[0].get('nombre')