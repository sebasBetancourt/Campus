from importaciones import *


while True:
    print(menuPrincipal)
    print(menu1)
    opcion = int(input('Escoge una opcion :'))
    match opcion:
        case 1:
            campers()
        case 2:
            
            pass

            match opcion:
                case 1:
                    addTrainer(baseDatos)
                    abrirArchivo('baseDatos')
                    guardarArchivo('baseDatos',baseDatos)
                    print('Hecho')
                    input('Press enter...........')
        case 3:
           coordinacion()
        case 4:
            print('Has cerrado tu sesion. Bye')
            input('Presiona cualquier tecla............')
            break
        case _:
            print('¡¡¡Ingresaste una opcion invalida!!!!')

