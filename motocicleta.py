from vehiculo import*
from bicicleta import*

class motocicleta(bicicleta)
    def __init__(self,color,ruedas,tipo,velocidad,cilindrada)
    super().__init__(color,ruedas,tipo)
    self.velocidad=velocidad
    self.ilindrada=cilindrada

