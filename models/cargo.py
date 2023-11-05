from models.traslado import Traslado

class Cargo(Traslado):
    def __init__(self):
        super().__init__(self)

    def add_warehouse_load(self, product_id, warehouse_id, quantity, creation_date):
        columns = ['id_subproducto', 'id_almacen', 'cantidad', 'tipo_movimiento', 'fecha_creacion']
        response = self.db.insert_one('tbl_movimientos', columns, product_id, warehouse_id, quantity, 1, creation_date)
        return response
