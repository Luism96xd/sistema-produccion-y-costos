from models.empresa import Empresa
from models.model import Model
from views.ui_viewIniciarSesion import ViewIniciarSesion
from controllers.usuariosController import UsuariosController
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
import sys, os

basedir = os.path.dirname(__file__)

try:
    from ctypes import windll  # Only exists on Windows.
    myappid = 'melissa.SistemaCostos.app.001'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass


def run():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(os.path.join(basedir,'assets', 'logo.ico')))
    
    e = Empresa()
    empresa = e.getEmpresa()

    window = ViewIniciarSesion(empresa = empresa)
    window.show() 

    model = Model()
    controller = UsuariosController(window, model)
    window.assignController(controller)

    # Start the event loop.
    sys.exit(app.exec())

if __name__ == "__main__":
    run()

#pyinstaller --noconsole --onefile --name "Sistema de Producción y Costos" --add-binary 'C:\Users\luisrivas\Documents\Sistema_costos\python39.dll' main.py