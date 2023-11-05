from utils.database import DB

class Model:
    def __init__(self, modelImpl=None):
        self.model = modelImpl
        self.db = DB()

    def getConnection(self):
        return self.db

    def getModel(self):
        return self.model

    def update_items(self, table_name, *args, **kwargs):
        columns = ""

        if kwargs:
            # kwargs is a dictionary.
            for key, value in kwargs.items():
                #print("%s = %s" % (key, value))
                if type(value) == str:
                    value = f"'{value}'"
                columns += "{0} = {1}".format(str(key), str(value))
                columns += ', '
            columns = columns[:-2]
            print(f'UPDATE {table_name} SET {columns}')
    
        if args:
            for value in args:
                if type(value) == str:
                    value = f"'{value}'"
                columns += str(value)
                columns += ', '
            columns = columns[:-2]
            print(f'UPDATE {table_name} SET price={args[0]}, quantity={args[1]}')

# model = Model()
# model.create_item('tabla', 1, "planta", 3)

# price = 5
# quantity = 10

# model.update_items('tabla', price, quantity)
# model.update_items('tabla', nombre_producto='Planta Eléctrica', cantidad=1, costo = 5.00)