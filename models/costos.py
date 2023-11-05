from models.model import Model

class Costos(Model):
    def __init__(self):
        super().__init__(self)    

    def calcular_costo_primo(self, mpd, mod):
        materia_prima_directa = float(mpd)
        mano_obra_directa = float(mod) 
        costo_primo = materia_prima_directa + mano_obra_directa
        return costo_primo

    def calcular_costo_produccion(self, md, mod, cf):
        material_directo = float(md)
        mano_obra_directa = float(mod) 
        carga_fabril =float(cf)
        costo_produccion = material_directo + mano_obra_directa + carga_fabril
        return costo_produccion

    def calcular_precio_venta (self, cv, go, ud):
        costo_venta = float(cv)
        gastos_operacion = float(go) 
        utilidad_deseada =float(ud)
        precio_venta = costo_venta + gastos_operacion + utilidad_deseada 
        return precio_venta

    def calcular_costo_conversion (self, mod, cf):
        mano_obra_directa = float(mod)
        carga_fabril = float(cf) 
        costo_conversion = mano_obra_directa + carga_fabril 
        return costo_conversion

    def calcular_costo_semivariable (self, cf, cv):
        costo_fijo = float(cf)
        costo_variable = float(cv) 
        costo_semivariable = costo_fijo + costo_variable 
        return costo_semivariable

    def calcular_costo_productos_proceso (self, cp, iv):
        costo_produccion = float(cp)
        costo_inventario_inicial = float(iv) 
        costo_productos_proceso = costo_produccion + costo_inventario_inicial 
        return costo_productos_proceso

    def calcular_costo_producto_terminado (self, cpt, ivf):
        costo_producto_proceso = float(cpt)
        costo_inventario_final_pp = float(ivf) 
        costo_producto_terminado = costo_producto_proceso + costo_inventario_final_pp 
        return costo_producto_terminado
        
    def calcular_costo_venta (self, ctpt, ivfpt):
        costo_total_productos_terminados = float(ctpt)
        costo_inventario_final_productos_terminados = float(ivfpt) 
        costo_venta = costo_total_productos_terminados - costo_inventario_final_productos_terminados
        return costo_venta
        
    def calcular_costo_total_productos_terminados (self, cpt, ivipt):
        costo_producto_terminado = float(cpt)
        costo_inventario_inicial_productos_terminados = float(ivipt) 
        costo_total_productos_terminados = costo_producto_terminado + costo_inventario_inicial_productos_terminados
        return costo_total_productos_terminados
        
    def calcular_costo_total_produccion_ventas (self, cv, go):
        costo_ventas = float(cv)
        gastos_operacion = float(go) 
        costo_total_produccion_ventas = costo_ventas + gastos_operacion
        return costo_total_produccion_ventas
    
    def calcular_ganancias_perdidas (self, ingr, gast):
        ingresos = float(ingr)
        gastos = float(gast) 
        ganancias_perdidas = ingresos - gastos
        return ganancias_perdidas

    def calcular_costo_variable_unidad(self, cvu, uf):
        costo_variable_unitario = float(cvu)
        numero_unidades_fabricadas = float(uf) 
        costo_variable_unidad = costo_variable_unitario / numero_unidades_fabricadas
        return costo_variable_unidad