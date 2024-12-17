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

def intDiezDigitos(mensaje):
    while True:
        documento = getInt(mensaje)
        cad =str(documento)
        if len(cad)== 10: 
            return cad
        else : print("El  numero tiene que tener 10 digitos")

def pressEnter ():
    print ("Chaito...")
    input('Press Enter...........................')


def newcandidate(baseDatos):
    print('Registrate-----')
    cedula = intDiezDigitos("Ingrese su cedula: ")
    for i in range(len(baseDatos["camper"])):
        if baseDatos["camper"][i]["cedula"] == cedula:
            print (baseDatos["camper"][i]["cedula"],"ya se encuentra registrado :)")
            pressEnter()
            return baseDatos
    nombre = input('Escribe tu nombre :').capitalize()
    apellido = input('Escribe tus apellidos :').capitalize()
    direccion = input('Ingresa tu direccion :').capitalize()
    acudiente = input('Ingresa un acudiente :').capitalize()
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
        'riesgo': riesgo,
        'horario': horario,
        'ruta': ruta,
        'Trainer': Trainer,
        'notas': notas,
        'salon': salon
    }

    baseDatos['camper'].append(newCandidato)
    return baseDatos
def addCandidato():
    baseDatos = abrirArchivo(RUTA_BASE_DATOS)
    baseDatos = newcandidate(baseDatos)
    guardarArchivo(RUTA_BASE_DATOS,baseDatos)
#case 2_Ingresar......................................................
def ingresarCamper(ingresar, baseDatos):
    encontrado = False 
    for camper in baseDatos['camper']:
        if ingresar == str(camper['cedula']):
            encontrado = True
            print("El Camper ha sido encontrado con exito") 


            if camper['estado']['En proceso'] == True:
                print("Estás en proceso de ingreso, espera que te llamen para el examen.")
                input('Press Enter para volver al menu anterior...............')
                return baseDatos

            if camper['estado']['Inscrito'] == True:
                print('Estas Inscrito, espera los resultados.')
                input('Press Enter...........................')
            if camper['estado']['Aprobado'] == True:
                print('Ya estas ¡¡¡Aprobado!!!, espera que te asignen cuando puedes iniciar.')
                input('Press Enter..........................................')
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
    return baseDatos


def loginCamper():
    ingresar = input('Escriba su cedula para ingresar :')
    baseDatos = abrirArchivo(RUTA_BASE_DATOS)
    baseDatos =  ingresarCamper(ingresar, baseDatos)







