from vehiculo import*

class bicicleta (vehiculo):
    def __init__(self,color,ruedas,tipo):
        vehiculo.__init__(self,color,ruedas)
        self.tipo=tipo
bici1=bicicleta("rojo",2,"urbana")
print(bici1.tipo)

