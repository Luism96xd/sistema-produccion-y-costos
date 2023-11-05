from models.model import Model

class Usuario(Model):
    def __init__(self, usuario=None):
        super().__init__(self)
        self.usuario = usuario
       
    def buscar_usuario(self, usuario, clave):
        filtros = {
            "nombre_usuario": usuario, 
            "clave" : clave, 
        }
        try:
            usuario = self.db.select_one("id_empresa, nombre_usuario" , "tbl_usuarios", filtros)
            if usuario == None:
                print("El usuario no se encuentra registrado en el sistema")
                return None
            else:
                print("Acceso concedido")
                return usuario
        except Exception as e:
            print(e)
            return None

    def search_username(self, username):
        filtros = {
            "nombre_usuario": username, 
        }
        try:
            username = self.db.select_one("nombre_usuario" , "tbl_usuarios", filtros)
            return username
        except Exception as e:
            print(e)
            return False

    def create_account(self, username, email, password, date):
        columns = ['nombre_usuario','email','clave','fecha_creacion']
        result = self.db.insert_one('tbl_usuarios', columns, username, email, password, date)
        return result 