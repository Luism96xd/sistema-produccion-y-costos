import utils.mvc_exceptions as mvc_exceptions
from utils.database import DB
from datetime import datetime

class CostosController:
    def __init__(self, view=None, model=None):
        self.db = DB()
        self.view = view
        self.model = model    
    
    def calcular_costo_primo(self, mpd, mod):
        resultado = self.model.calcular_costo_primo(mpd, mod)
        self.view.display_message("Operación Exitosa", "El costo primo es: " + str(resultado))

    def calcular_costo_produccion(self, md, mod, cf):
        resultado = self.model.calcular_costo_produccion(md, mod, cf)
        self.view.display_message("Operación Exitosa", "El costo de producción es: " + str(resultado))

    def calcular_precio_venta (self, cv, go, ud):
        resultado = self.model.calcular_precio_venta(cv, go, ud)
        self.view.display_message("Operación Exitosa", "El precio de venta es: " + str(resultado))

    def calcular_costo_conversion (self, mod, cf):
        resultado = self.model.calcular_costo_conversion(mod, cf)
        self.view.display_message("Operación Exitosa", "El costo de conversión es: " + str(resultado))

    def calcular_costo_semivariable (self, cf, cv):
        resultado = self.model.calcular_costo_semivariable(cf, cv)
        self.view.display_message("Operación Exitosa", "El costo semivariable es: " + str(resultado))

    def calcular_costo_productos_proceso (self, cp, iv):
        resultado = self.model.calcular_costo_productos_proceso(cp, iv)
        self.view.display_message("Operación Exitosa", "El costo total de productos en proceso es de: " + str(resultado))

    def calcular_costo_producto_terminado (self, cpt, ivf):
        resultado = self.model.calcular_costo_producto_terminado(cpt, ivf)
        self.view.display_message("Operación Exitosa", "El costo del producto terminado es:  " + str(resultado))
    
    def calcular_costo_venta (self, ctpt, ivfpt):
        resultado = self.model.calcular_costo_venta(ctpt, ivfpt)
        self.view.display_message("Operación Exitosa", "El costo de venta es:  " + str(resultado))
    
    def calcular_costo_total_productos_terminados (self, cpt, ivipt):
        resultado = self.model.calcular_costo_total_productos_terminados(cpt, ivipt)
        self.view.display_message("Operación Exitosa", "El costo total de productos terminados es:  " + str(resultado))
        
    def calcular_costo_total_produccion_ventas (self, cv, go):
        resultado = self.model.calcular_costo_total_produccion_ventas(cv, go)
        self.view.display_message("Operación Exitosa", "El costo total de producción y ventas es:  " + str(resultado))
        
    def calcular_ganancias_perdidas (self, ingr, gast):
        resultado = self.model.calcular_ganancias_perdidas(ingr, gast)
        self.view.display_message("Operación Exitosa", "El valor de las ganancias y pérdidas es de:  " + str(resultado))

    def calcular_costo_variable_unidad(self, cvu, uf):
        resultado = self.model.calcular_costo_variable_unidad(cvu, uf)
        self.view.display_message("Operación Exitosa", "El costo variable por unidad es:  " + str(resultado))
        