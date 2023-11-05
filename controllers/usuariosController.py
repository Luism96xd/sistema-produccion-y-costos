import utils.mvc_exceptions as mvc_exceptions
from utils.database import DB
from datetime import datetime
from models.usuario import Usuario
from views.ui_viewMain import MainWindow
import hashlib
import re

class UsuariosController:
    def __init__(self, view=None, model=None):
        self.db = DB()
        self.view = view
        self.model = model
    
    def iniciar_sesion(self, username, password): 
        if username == '':
            self.view.display_message ("Escriba su nombre de usuario", "Faltó escribir su nombre de usuario")
        elif password == '':
            self.view.display_message ("Escriba su contraseña", "Faltó escribir la contraseña")
        else:
            m = hashlib.sha256()   
            m.update(password.encode())
            hash = m.hexdigest()
            user = Usuario(username)
            user_data = user.buscar_usuario(username, hash)
            print(user_data)

            if user_data != None:
                window = MainWindow(self.view, empresa = self.view.empresa)
                window.show()
            else:
                self.view.display_message ("Acceso denegado", "El usuario o la contraseña es inválida")

    def registrar_cuenta(self, username, email, password1, password2):
        error = False
        if (username == '' or email == '' or password1 == '' or password2 == ''):
            self.view.display_empty_fields_error()
            error = True
        
        userExists = self.model.search_username(username)
        if userExists:
            self.view.display_message("Usuario ya existe", "Este nombre de usuario ya está tomado")
            error = True

        if password1 != password2:
            self.view.display_message("Claves no coinciden", "Las dos claves deben coincidir")
            error = True

        email_pattern = re.compile(r'[A-Za-z0-9._]+\@[A-Za-z0-9]+\.[A-Za-z]{2,3}')
        if not re.match(email_pattern, email):
            self.view.display_message("Correo inválido", "Escriba un correo válido")
            error = True
            
        if error == False:
            date = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
            m = hashlib.sha256()   
            m.update(password1.encode())
            hash = m.hexdigest()
            result = self.model.create_account(username, email, hash, date)
            if result == True:
                self.view.display_message('Operación Exitosa', f"Usuario {username} creado satisfactoriamente")
                self.view.mostrarPrincipal()