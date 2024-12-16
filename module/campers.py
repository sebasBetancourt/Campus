from funciones.funciones import *
from menssage.menssage import *

def campers():
    while True:
        print(menuEntrarCamper1)
        print('Ingresa una opcion  ')
        opcion = getInt(':)')
        if opcion == 1:
            addCandidato()
            print('Hecho')
            input('Presiona enter...............')
        elif opcion == 2:
            loginCamper()
            print('Hecho')
            input('Press Enter................')
        elif opcion == 3:
            print('Has cerrado tu sesión.')
            input('Press a key.........')
            break
        else:
            print('Ingrese una opcion valida')
            input('Press Enter...............')