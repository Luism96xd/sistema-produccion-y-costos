from models.model import Model

class Traslado(Model):
    def __init__(self, name='Producto', quantity=1, origin=None, destination=None, transact_type=None):
        super().__init__(self)
        self.name = name
        self.quantity = quantity
        self.origin = origin
        self.destination = destination
        self._type = transact_type

    def get_type(self):
        return self.type

    def set_type(self, transact_type):
        self._type = transact_type

    def register_transfer(self, product, origin, destination, quantity, creation_date):
        columns = ['id_subproducto', 'almacen_origen', 'almacen_destino', 'cantidad', 'fecha_creacion']
        response = self.db.insert_one('tbl_traslados', columns, product, origin, destination, quantity, creation_date)
        return response

    def verify_stock(self, id_subproducto):
        filters = {
            'tipo_movimiento': 1,
            'id_subproducto': id_subproducto
        }
        cargos = self.db.select_one('COALESCE(SUM(cantidad), 0) AS CARGOS', 'tbl_movimientos', filters)
        filters = {
            'tipo_movimiento': 2,
            'id_subproducto': id_subproducto
        }
        descargos = self.db.select_one('COALESCE(SUM(cantidad), 0) AS DESCARGOS', 'tbl_movimientos', filters)
        existencias = abs(cargos - descargos)
        return existencias

    def get_transfers_list(self):
        conn = self.db.connect()
        sql = "SELECT id_traslado, nombre_producto, tbl_almacenes.nombre AS almacen_origen, \
                tbl_almacenes2.nombre AS almacen_destino, tbl_traslados.cantidad, tbl_traslados.fecha_creacion \
                FROM tbl_traslados LEFT JOIN tbl_almacenes \
                ON (tbl_traslados.almacen_origen = tbl_almacenes.id_almacen) \
                LEFT JOIN tbl_almacenes as tbl_almacenes2 \
                ON (tbl_traslados.almacen_destino = tbl_almacenes2.id_almacen) \
                INNER JOIN tbl_subproductos \
                ON (tbl_traslados.id_subproducto = tbl_subproductos.id_subproducto)"
        cursor = conn.cursor()
        cursor.execute(sql)

        result = cursor.fetchall()

        return result
