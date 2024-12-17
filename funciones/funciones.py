from menssage.menssage import *
from module.DatosJSON import *




#---------------------------------------------------------------------------------------------------------------------------------------
#CASE 1_Camper.................................................................
def getInt(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except Exception:
            print('Opcion Invalida, ingrese un valor valido.')
#case1_registrarse

def intDiezDigitos(mensaje):
    while True:
        documento = getInt(mensaje)
        cad =str(documento)
        if len(cad)== 10: 
            return cad
        else : print("El  numero tiene que tener 10 digitos")

def pressEnter ():
    print ("Hecho")
    input('Press Enter...........................')








