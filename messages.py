from PySide6.QtWidgets import QMessageBox

class Messages():
    def __init__(self):
        pass
    def display_empty_fields_error(self):
        msgBox = QMessageBox(self)
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setWindowTitle('Ingreso de datos')
        msgBox.setText('Debe rellenar todos los campos')
        msgBox.show()


    def display_item_stored(self, item, name):
        msgBox = QMessageBox(self)
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setWindowTitle(f'{item} Añadido')
        msgBox.setText(f'El {item} {name} ha sido añadido satisfactoriamente')
        msgBox.show()

    def display_item_already_stored_error(self, item, name, error):
        msgBox = QMessageBox(self)
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setWindowTitle('Error')
        msgBox.setText(f'El {item} {name} ya se encuentra en la base de datos')
        msgBox.show()

    def display_message(self, title, message):
        msgBox = QMessageBox(self)
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.show()
