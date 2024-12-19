from funciones.funciones import *
from menssage.menssage import *

def newcandidate(baseDatos):
    print('---- Registrate ----')
    cedula = getInt("Ingrese su cedula: ")
    cedula = str(cedula)
    for i in range(len(baseDatos["camper"])):
        if baseDatos["camper"][i]["cedula"] == cedula:
            print (baseDatos["camper"][i]["cedula"],"ya se encuentra registrado :)")
            pressEnter()
            return baseDatos
    nombre = input('Escribe tu nombre: ').capitalize()
    apellido = input('Escribe tus apellidos : ').capitalize()
    direccion = input('Ingresa tu direccion : ').capitalize()
    acudiente = input('Ingresa un acudiente : ').capitalize()
    telefono = getInt("Ingrese su telefono: ")
    telefonoFijo = getInt("Ingrese su numero de telefono fijo: ")
    telefono = str(telefono)
    telefonoFijo = str(telefonoFijo)
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
        'grupo' : "0"
    }
    pressEnter()
    baseDatos['camper'].append(newCandidato)
    return baseDatos

def addCandidato():
    baseDatos = abrirArchivo(RUTA_BASE_DATOS)
    baseDatos = newcandidate(baseDatos)
    guardarArchivo(RUTA_BASE_DATOS, baseDatos)


def loginDatosCamper(ingresar):
    datos = abrirArchivo(RUTA_BASE_DATOS)
    for camper in baseDatos['camper']:
        if ingresar == camper['cedula']:
            for student in camper['cedula']:
                print(f'Hola {student["nombre"]} ')
                print(f'Cedula: {student["cedula"]} ')
                print(f'Direccion: {student["direccion"]} ')
                print(f'Acudiente: {student["acudiente"]} ')
                print(f'Telefono: {student["telefono"]} ')
                print(f'Telefono Fijo: {student["telefonoFijo"]} ')
                print(f"Estado: Cursando ")
                countNotas = 0
                for notas in student["notas"]:
                    countNotas += 1
                    print(f'Modulo {countNotas}: {notas[f"modulo{countNotas}"]}')
                if student["riesgo"] == True:
                    print(f'Riesgo: Alto')
                elif student["riesgo"] == False:
                    print(f'Riesgo: Alto')
                print(f'Grupo: {student["grupo"]} ')


   
#case 2_Ingresar......................................................
def retirarCamper():
    datos = abrirArchivo(RUTA_BASE_DATOS)
    encontrado = False
    cedula = getStr1('Escribe cedula del camper :') 
    
    for i in datos["camper"]:
        if cedula == i['cedula']:
            if i['estado']['Cursando'] == True:
                encontrado = True
                i['estado']['Cursando'] = False
                i['estado']['Retirado'] = True
                guardarArchivo(RUTA_BASE_DATOS, datos)
                print('Te has retiraste de CampusLands.')
                pressEnter()
                break
    if not encontrado:
        print('El usuario no existe.')
        pressEnter()
def ingresarCamper(baseDatos):
    encontrado = False 
    ingresar = str(getInt('Escriba su cedula para ingresar : '))
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
                loginCamper(ingresar)
            elif camper['estado']['Graduado'] == True:
                print('Estas graduado!!Bye')
                input('Press Enter.......................................... ')
            elif camper['estado']['Expulsado'] == True:
                print('Esta expulsado de campus, intenta otra vez dentro de 5 años.')
                pressEnter()
            elif camper['estado']['Retirado'] == True:
                print('Te retiraste de CampusLands, intenta registrarte otra vez dentro de 4 meses.')
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
        elif opcion == 2:
            loginCamper()
            pressEnter()
        elif opcion == 3:
            datos = abrirArchivo(RUTA_BASE_DATOS)
            encontrado = False
            cedula = getStr1('Escribe cedula del camper :') 

            for i in datos["camper"]:
                if cedula == i['cedula']:
                    if i['estado']['Cursando'] == True:
                        encontrado = True
                        i['estado']['Cursando'] = False
                        i['estado']['Retirado'] = True
                        guardarArchivo(RUTA_BASE_DATOS, datos)
                        print('Te has retirado de CampusLands exitosamente.')
                        pressEnter()
                        break
            if not encontrado:
                print('El usuario no existe.')
                pressEnter()
        elif opcion == 4:
            pressEnter()
            break
        else:
            print('Ingrese una opcion valida')
            input('Press Enter...............')