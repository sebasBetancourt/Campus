from funciones.funciones import *

def coordinacion():
    while True:
        print(menuCoordinador)
        opcion = getInt('Ingrese una opción: ')
        match opcion:
            case 1:
                print(menuCamperCoordinador)
                changeCandidato()  # Llamamos solo a changeCandidato aquí
            case 2:
                pass  # Aquí podrías agregar más lógica si es necesario
            case 3:
                pass  # Aquí podrías agregar más lógica si es necesario
            case 4:
                print('Has cerrado tu sesión. ¡Adiós!')
                input('Presiona cualquier tecla para salir...')
                break
            case _:
                print('¡¡¡Opción inválida!!!')
