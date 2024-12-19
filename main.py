from importaciones import *



while True:
    print(menuPrincipal)
    print('a')
    print(menu1)
    opcion = getInt('Escoge una opcion :')

    match opcion:
        case 1:
            pressEnter()
            campers()
        case 2:
            pressEnter()
            Trainer()

        case 3:
            pressEnter()
            coordinacion()

        case 4:
            print('Has cerrado tu sesion. Bye')
            input('Presiona cualquier tecla............')
            break
        case _:
            print('¡¡¡Ingresaste una opcion invalida!!!!')

