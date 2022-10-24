from vehiculo import*

class coche (vehiculo):
    def __init__(self,color,ruedas,velocidad,cilindrada):
        vehiculo.__init__(self,color,ruedas)
        self.velocidad =velocidad
        self.cilindrada =cilindrada

        ef __str__(self):
        return vehiculo.__str__(self) + ", {} km/h, {} cc".format(self.velocidad,self.cilindrada)




