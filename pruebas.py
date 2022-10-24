from operator import attrgetter
from vehiculo import * 
from coche import *
from bicicleta import *
from motocicleta import *
from Camioneta import *

coche1 = coche("rojo",4,150,1200)
bicicleta1 = bicicleta("Azul",2,"Deportiva")
Motocicleta1 = Motocicleta("verde",4,"Deportiva",40,250)
camioneta1= Camioneta("Amarillo",4,120,780,400)

vehiculos = [coche1,bicicleta1,Motocicleta1,camioneta1]

print(vehiculos[0].ruedas)

def catalogar(lista,numRuedas):
    cantidad =0 
    for i in lista:
        if i.ruedas == numRuedas:
            cantidad +=1

    print ("Se han encontrado {} vehiculos con {} ruedas".format(cantidad, numRuedas))

"""
catalogar inicial
def catalogar(lista):
    for i in lista:
        print("Clase del objeto: ",type(i).__name__)
        print("Atributos del objeto:",vars(i))
ofvcc
"""
catalogar(vehiculos,4)