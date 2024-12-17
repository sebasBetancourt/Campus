from funciones.funciones import *
from menssage.menssage import *

def newcandidate(baseDatos):
    print('---- Registrate ----')
    cedula = intDiezDigitos("Ingrese su cedula: ")
    for i in range(len(baseDatos["camper"])):
        if baseDatos["camper"][i]["cedula"] == cedula:
            print (baseDatos["camper"][i]["cedula"],"ya se encuentra registrado :)")
            pressEnter()
            return baseDatos
    nombre = input('Escribe tu nombre: ').capitalize()
    apellido = input('Escribe tus apellidos : ').capitalize()
    direccion = input('Ingresa tu direccion : ').capitalize()
    acudiente = input('Ingresa un acudiente : ').capitalize()
    telefono = intDiezDigitos("Ingrese su telefono: ")
    telefonoFijo = intDiezDigitos("Ingrese su numero de telefono fijo: ")
    estado = {"En proceso": True,
                "Inscrito": False,
                "Aprobado": False,
                "Cursando": False,
                "Graduado": False,
                "Expulsado": False,
                "Retirado": False
                }
    riesgo = False
    notas = {
        "modulo1": 0,
        "modulo2": 0,
        "modulo3": 0,
        "modulo4": 0,
        "modulo5": 0
    }
    newCandidato = {
        'cedula':cedula,
        'nombre':nombre,
        'apellido':apellido,
        'direccion':direccion,
        'acudiente':acudiente,
        'telefono':telefono,
        'telefonoFijo':telefonoFijo,
        'estado':estado,
        'notas': notas,
        'riesgo': riesgo,
        'grupo' : "0",
    }
    baseDatos['camper'].append(newCandidato)
    return baseDatos

def addCandidato():
    baseDatos = abrirArchivo(RUTA_BASE_DATOS)
    baseDatos = newcandidate(baseDatos)
    guardarArchivo(RUTA_BASE_DATOS,baseDatos)
    
#case 2_Ingresar......................................................
def ingresarCamper(baseDatos):
    encontrado = False 
    ingresar = str(intDiezDigitos('Escriba su cedula para ingresar : '))
    for camper in baseDatos['camper']:
        if ingresar == camper['cedula']:
            encontrado = True
            print("El Camper ha sido encontrado con exito") 
            if camper['estado']['En proceso'] == True:
                print("Estás en proceso de ingreso, espera que te llamen para el examen.")
                input('Press Enter para volver al menu anterior...............')
                return baseDatos
            elif camper['estado']['Inscrito'] == True:
                print('Estas Inscrito, espera los resultados.')
                input('Press Enter...........................')
            elif camper['estado']['Aprobado'] == True:
                print('Ya estas ¡¡¡Aprobado!!!, espera que te asignen cuando puedes iniciar.')
                input('Press Enter.......................................... ')
            elif camper['estado']['Cursando'] == True:
                print('acceder a laas notas e informacion de lo m demas')
                input('Press Enter.......................................... ')
            elif camper['estado']['Graduado'] == True:
                print('Estas graduado vete a la mrd')
                input('Press Enter.......................................... ')
            elif camper['estado']['Expulsado'] == True:
                print('Esta expulsado que te pasa, vete, chao')
                input('Press Enter.......................................... ')
            elif camper['estado']['Retirado'] == True:
                print('Chao con adios...')
                input('Press Enter.......................................... ')
    if encontrado == False:
        print('Usted no se encuentra REGISTRADO, vaya al menu anterior para registrarse.')
        input('Press Enter para acceder al menu anterior')
    return baseDatos


def loginCamper():
    baseDatos = abrirArchivo(RUTA_BASE_DATOS)
    baseDatos =  ingresarCamper(baseDatos)

def campers():
    while True:
        print(menuEntrarCamper1)
        print('Ingresa una opcion  ')
        opcion = getInt(':)')
        if opcion == 1:
            addCandidato()
            pressEnter()
        elif opcion == 2:
            loginCamper()
            pressEnter()
        elif opcion == 3:
            pressEnter()
            break
        else:
            print('Ingrese una opcion valida')
            input('Press Enter...............')