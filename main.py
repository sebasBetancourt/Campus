from importaciones import *



while True:
    print(menuPrincipal)
    print('a')
    print(menu1)
    opcion = getInt('Escoge una opcion :')

    match opcion:
        case 1:
            campers()
        case 2:
            Trainer()
        case 3:
            coordinacion()
        case 4:
            print('Has cerrado tu sesion. Bye')
            input('Presiona cualquier tecla............')
            break
        case _:
            print('¡¡¡Ingresaste una opcion invalida!!!!')

