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
def newcandidate(baseDatos):
    print('Registrate-----')
    cedula = getInt('Escribe tu cedula :')
    nombre = input('Escribe tu nombre :').capitalize()
    apellido = input('Escribe tus apellidos :').capitalize()
    direccion = input('Ingresa tu direccion :').capitalize()
    acudiente = input('Ingresa un acudiente :').capitalize()
    telefono = getInt('Ingrese su numero telefonico :')
    telefonoFijo = getInt('Ingrese su telefono Fijo :')
        

    estado = {"En proceso": True,
                "Inscrito": False,
                "Aprobado": False,
                "Cursando": False,
                "Graduado": False,
                "Expulsado": False,
                "Retirado": False
                }
    riesgo = False

    newCandidato = {
        'cedula':cedula,
        'nombre':nombre,
        'apellido':apellido,
        'direccion':direccion,
        'acudiente':acudiente,
        'telefono':telefono,
        'telefonoFijo':telefonoFijo,
        'estado':estado,
        'riesgo': riesgo
    }
    baseDatos['camper'].append(newCandidato)
    return baseDatos
def addCandidato():
    baseDatos = abrirArchivo(RUTA_BASE_DATOS)
    baseDatos = newcandidate(baseDatos)
    guardarArchivo(RUTA_BASE_DATOS,baseDatos)
#case 2_Ingresar......................................................
def ingresarCamper(ingresar):
    encontrado = False 
    for camper in baseDatos['camper']:
        if ingresar == str(camper['cedula']):
            encontrado = True
            print("El Camper ha sido encontrado con exito") 


            if camper['estado']['En proceso'] == True:
                print("Estás en proceso de ingreso, espera que te llamen para el examen.")
                input('Press Enter para volver al menu anterior...............')
                break  


            if camper['estado']['Inscrito'] == True:
                
                pass
            if camper['estado']['Aprobado'] == True:
                
                pass
            if camper['estado']['Cursando'] == True:
                
                pass
            if camper['estado']['Graduado'] == True:
                
                pass
            if camper['estado']['Expulsado'] == True:
                
                pass
            if camper['estado']['Retirado'] == True:
                
                pass

    if not encontrado:
        print('Usted no se encuentra REGISTRADO, vaya al menu anterior para registrarse.')
        input('Press Enter para acceder al menu anterior')


def loginCamper():
    ingresar = input('Escriba su cedula para ingresar :')
    ingresarCamper(ingresar)          





#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#CASE 2_Agregar Trainer
def addTrainer(baseDatos):
    print('--------------------------Registrate---------------------------')
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
        'hDisponible':hDisponibles

    }
    baseDatos['trainer'].append([newTrainer])
    return newTrainer


#----------------------------------------------------------------------------------------------------------------------------------------------------------
#CASE 3_Coordinacion
def changeCandidato():
    baseDatos = abrirArchivo(RUTA_BASE_DATOS)
    baseDatos = cambiarCandidato(baseDatos)
    guardarArchivo(RUTA_BASE_DATOS, baseDatos)
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

