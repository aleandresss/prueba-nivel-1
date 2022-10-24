from vehiculo import *
from coche import *

class camioneta(coche):
    def __init__ (self, color, ruedas, velocidad, cilindrada,carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga 
        