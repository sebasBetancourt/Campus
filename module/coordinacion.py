from funciones.funciones import *



#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#CASE 2_Agregar Trainer
def addTrainer(baseDatos):
    print('--------------------------Registrar camper---------------------------')
    nombre = input('Escribe tu nombre completo :')
    cedula = int(input('Escribe tu cedula :'))
    print('Escribe tu fecha de nacimiento :')
    dia = int(input('Dia: '))
    mes = int(input('Mes: '))
    año = int(input('Año: '))
    fechaNacimiento = (f'{dia}/{mes}/{año}')
    skills = input('Ingresa tus habilidades aqui: \n')
    hDisponibles = print('Escoge una opcion: \n1. 6am a 2pm\n2. 2pm a 10pm')
    hDisponibles = int(input('Elige una opcion: '))
    if hDisponibles == 1:
        hDisponibles = '6am-2pm'
    elif hDisponibles == 2:
        hDisponibles = '2pm-10pm'
    salon = 0
    

    newTrainer = {
        'nombre':nombre,
        'cedula':cedula,
        'fechaNacimiento':fechaNacimiento,
        'skills':skills,
        'hDisponible':hDisponibles,
        'salon': salon
    }
    baseDatos['trainer'].append([newTrainer])
    return baseDatos
def agregarTrainer():
    baseDatos = abrirArchivo(RUTA_BASE_DATOS)
    baseDatos = addTrainer(baseDatos)
    guardarArchivo(RUTA_BASE_DATOS,baseDatos)


#----------------------------------------------------------------------------------------------------------------------------------------------------------
#CASE 3_Coordinacion

def cambiarCandidato(baseDatos):
    opcion = getInt('Ingrese una opción: ')
    
    match opcion:
        case 1:
            pass  # Aquí puedes agregar lógica para la opción 1 si lo necesitas
        case 2:
            print(menuCandidatosCoordinador)
            opcion = getInt('Ingrese una opción: ')
            match opcion:
                case 1:
                    ingresar = input('Ingrese cédula del candidato: ')
                    encontrado = False
                    for camper in baseDatos['camper']:
                        if ingresar == str(camper['cedula']):
                            camper['estado']['En proceso'] = False
                            camper['estado']['Inscrito'] = True
                            print("El Camper ha sido inscrito para el examen.")
                            encontrado = True
                            break
                    if not encontrado:
                        print("Cédula no encontrada.")
                case 2:
                    ingresar = input('Ingrese cédula del candidato: ')
                    encontrado = False
                    for camper in baseDatos['camper']:
                        if ingresar == str(camper['cedula']):
                            notaPractica = getInt('Ingrese la nota de la práctica: ')
                            notaTeorica = getInt('Ingrese la nota teórica: ')
                            totalNota = (notaPractica + notaTeorica) / 2
                            if totalNota >= 60:
                                camper['estado']['Inscrito'] = False
                                camper['estado']['Aprobado'] = True
                                print("El Camper ha sido aprobado con éxito.")
                            else:
                                camper['estado']['Inscrito'] = False
                                camper['estado']['Denegado'] = True
                                print("El Camper no alcanzó la puntuación de aprobación.")
                            encontrado = True
                            break
                    if not encontrado:
                        print("Cédula no encontrada.")
    return baseDatos

def changeCandidato():
    baseDatos = abrirArchivo(RUTA_BASE_DATOS)
    baseDatos = cambiarCandidato(baseDatos)
    guardarArchivo(RUTA_BASE_DATOS, baseDatos)

def verInfoDeRutas():
    datos = abrirArchivo(RUTA_BASE_DATOS)
    cont = 0
    for i in datos["rutas"].values():
        cont += 1
        print(f"{cont}. {i}")
    rut = getInt("Ingrese la ruta: ")
    rut = str(rut)
    for j in datos["rutas"]:
        if rut == j:
            print("---- Estudiantes ----")
            for h in datos["camper"]:
                if rut == h["ruta"]:
                    print("")
                    print(h["cedula"])
                    print(f"{h["nombre"]} {h["apellido"]}")
                    print("")
            print("---- Profesores ----")
            for z in datos["trainer"]:
                if rut == z["ruta"]:
                    print("")
                    print(z["cedula"])
                    print(f"{z["nombre"]}: {z["skills"]}")
                    print("")
            pressEnter()
            return
        


def administrarCampers ():
    while True:
        print(menuCamperCoordinador)
        opc1 = getInt('Ingrese una opción: ')
        match opc1:
            case 1:
                print(menuCampersCoordinador)
                opc1_1 = getInt('Ingrese una opción: ')
                match opc1_1:
                    case 1: verInfoDeRutas()
                    case 2: print("Grupo asignado")
                    case 3: 
                        print("Menu anterior")
                        break
                    case _:
                        print("Opcion no valida")
            case 2: changeCandidato()  # Llamamos solo a changeCandidato aquí
            case 3: 
                pressEnter()
                return 
            case _: print("opcion invalida")

def administrarTrainers ():
    while True:
        print(menuCoordinadorTrainer)
        opc1 = getInt('Ingrese una opción: ')
        match opc1:
            case 1: print("addTrainer()")
            case 2: print("viewTrainers()")
            case 3: print("asigneRuta()")
            case 4: print("asigneSalon()")
            case 5: print("asigneEstudiantes()")
            case 6: print("asigneHorario()")
            case 7: 
                pressEnter()
                return
            case _: print("opcion invalida")


def reportes ():
    while True:
        print(menuCoordinadorTrainer)
        opc1 = getInt('Ingrese una opción: ')
        match opc1:
            case 1: print("addTrainer()")
            case 2: print("viewTrainers()")
            case 3: print("asigneRuta()")
            case 4: print("asigneSalon()")
            case 5: print("asigneEstudiantes()")
            case 6: print("asigneHorario()")
            case 7: 
                pressEnter()
                return
            case _: print("opcion invalida")
def coordinacion():
    while True:
        print(menuCoordinador)
        opcion = getInt('Ingrese una opción: ')
        match opcion:
            case 1: administrarCampers()
            case 2: administrarCampers()
            case 3: reportes()
            case 4:
                print('Has cerrado tu sesión. ¡Adiós!')
                input('Presiona cualquier tecla para salir...')
                break
            case _:
                print('¡¡¡Opción inválida!!!')
