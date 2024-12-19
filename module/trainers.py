from funciones.funciones import *

def calificar():
    datos = abrirArchivo(RUTA_BASE_DATOS)
    cedula = getInt('Ingrese cedula del camper :')
    encontrado = False
    for camper in datos['camper']:
        if camper['cedula'] == str(cedula):
            encontrado = True
            if camper['estado']['Cursando'] == True:
                print('--------Ingresa las notas-----')
                print('....Modulo 1......')
                modulo1Teorica = getInt('Nota Teorica :')
                modulo1Practica = getInt('Nota Practica: ')
                modulo1Quizes = getInt('Ingrese la nota de los trabajos y los quizes :')
                pressEnter()
                modulo1 = (modulo1Teorica * 0.3) + (modulo1Practica * 0.6) + (modulo1Quizes * 0.1)
                print('....Modulo 2......')
                print('Si el camper todavia no ha presentado el siguiente modulo, ingresar (0)')
                modulo2Teorica = getInt('Nota Teorica :')
                modulo2Practica = getInt('Nota Practica :')
                modulo2Quizes = getInt('Ingrese la nota de los trabajos y los quizes :')
                modulo2 = (modulo2Teorica * 0.3) + (modulo2Practica * 0.6) + (modulo2Quizes * 0.1)
                pressEnter()
                print('....Modulo 3......')
                print('Si el camper todavia no ha presentado el siguiente modulo, ingresar (0)')
                modulo3Teorica = getInt('Nota Teorica :')
                modulo3Practica = getInt('Nota Practica :')
                modulo3Quizes = getInt('Ingrese la nota de los trabajos y los quizes :')
                modulo3 = (modulo3Teorica * 0.3) + (modulo3Practica * 0.6) + (modulo3Quizes * 0.1)
                pressEnter()
                print('....Modulo 4......')
                print('Si el camper todavia no ha presentado el siguiente modulo, ingresar (0)')
                modulo4Teorica = getInt('Nota Teorica :')
                modulo4Practica = getInt('Nota Practica :')
                modulo4Quizes = getInt('Ingrese la nota de los trabajos y los quizes :')
                modulo4 = (modulo4Teorica * 0.3) + (modulo4Practica * 0.6) + (modulo4Quizes * 0.1) 
                pressEnter()
                print('....Modulo 5......')
                print('Si el camper todavia no ha presentado el siguiente modulo, ingresar (0)')
                modulo5Teorica = getInt('Nota Teorica :')
                modulo5Practica = getInt('Nota Practica :')
                modulo5Quizes = getInt('Ingrese la nota de los trabajos y los quizes :')
                modulo5 = (modulo5Teorica * 0.3) + (modulo5Practica * 0.6) + (modulo5Quizes * 0.1) 
                pressEnter()

                notas = {
                    "modulo1": modulo1,
                    "modulo2": modulo2,
                    "modulo3": modulo3,
                    "modulo4": modulo4,
                    "modulo5": modulo5
                }

                camper['notas'] = notas

                guardarArchivo(RUTA_BASE_DATOS, datos)
                break
            else:
                print("")
                print("El Camper no se encuentra cursando.")
                pressEnter()
    
    if not encontrado:
        print('La cedula es incorrecta')
        pressEnter()

def viewTrainer():
    datos = abrirArchivo(RUTA_BASE_DATOS)
    cedula = getInt('Ingrese su cedula :')
    encontrado = False
    for trainer in datos['trainer']:
        if trainer['cedula'] == str(cedula):
            encontrado = True
            print("")
            print(f"-----Datos {trainer['nombre']}----")
            print("")
            print(f'Nombre: {trainer["nombre"]}')
            print(f'cedula: {trainer["cedula"]}')
            print(f'fechaNacimiento: {trainer["fechaNacimiento"]}')
            print(f'skills: {trainer["skills"]}')
            pressEnter()
    if not encontrado:
        print('La cedula es incorrecta')
        pressEnter()
    

def viewEstudiantes():
    datos = abrirArchivo(RUTA_BASE_DATOS)
    count = 0
    cedula = getInt('Ingrese su cedula :')
    encontrado = False
    for grupo in datos['grupos']:
        for trainer in datos['trainer']:
            if trainer['cedula'] == str(cedula):
                print('--------Estudiantes-------------')
                if grupo['trainer'] == str(cedula):
                    for camper in datos['camper']:
                        if camper['grupo'] == grupo['nombre']:
                            count += 1
                            print(f"{count}. Camper = nombre: {camper['nombre']} {camper['apellido']}\ncedula: {camper['cedula']}")
                            pressEnter()
                    encontrado = True
                    break
        if encontrado:
            break

    if not encontrado:
        print('La cedula es incorrecta')
        pressEnter()



#-------------------------------callTrainer
def Trainer():
    while True:
        print(menuTrainer)
        opcion = getInt(':) ')
        match opcion:
            case 1: calificar()
            case 2: viewTrainer()
            case 3: viewEstudiantes()
            case 4:
                input('Press enter.......')
                break