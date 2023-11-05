from models.traslado import Traslado

class Descargo(Traslado):
    def __init__(self):
        super().__init__(self)

    def verify_stock(self, id_subproducto, id_almacen):
        filters = {
            'id_subproducto': id_subproducto,
            'id_almacen': id_almacen
        }
        existencias = self.db.select_one('COALESCE(SUM(cantidad),0) AS EXISTENCIAS', 'tbl_movimientos', filters)
        return existencias

    def add_warehouse_unload(self, product_id, warehouse_id, quantity, creation_date):
        columns = ['id_subproducto', 'id_almacen', 'cantidad', 'tipo_movimiento', 'fecha_creacion']
        stock = self.verify_stock(product_id, warehouse_id)
        if stock >= quantity:
            response = self.db.insert_one('tbl_movimientos', columns, product_id, warehouse_id, - quantity, 2, creation_date)
        else: 
            response = False
        return response