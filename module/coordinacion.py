from funciones.funciones import *



#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#CASE 2_Agregar Trainer
def agregarTrainer(baseDatos):
    print('--------------------------Registrar Trainer---------------------------')
    nombre = input('Escribe nombre completo del trainer:')
    cedula = getInt('Escribe cedula del trainer :')
    for i in range(len(baseDatos["trainer"])):
        if baseDatos["trainer"][i]["cedula"] == cedula:
            print (baseDatos["trainer"][i]["cedula"],"ya se encuentra registrado :)")
            pressEnter()
            return baseDatos
    print('Escribe fecha de nacimiento del trainer :')
    dia = intDosDigitos('Dia: ')
    mes = getInt('Mes: ')
    año = intDosDigitos('Año: ')
    fechaNacimiento = (f'{dia}/{mes}/{año}')
    skills = input('Ingresa las skills del trainer: \n')
    

    newTrainer = {
        'nombre':nombre,
        'cedula':cedula,
        'fechaNacimiento':fechaNacimiento,
        'skills':skills
    }
    baseDatos['trainer'].append(newTrainer)
    return baseDatos
def addTrainer():
    baseDatos = abrirArchivo(RUTA_BASE_DATOS)
    baseDatos = agregarTrainer(baseDatos)
    guardarArchivo(RUTA_BASE_DATOS,baseDatos)

def viewTrainers():
    datos = abrirArchivo(RUTA_BASE_DATOS)
    contT = 0
    for i in datos["trainer"]:
        contT += 1
        print("")
        print(f"{contT}. {i['nombre']} - cedula: {i['cedula']}")
        print(f"Fecha de Nacimiento: {i['fechaNacimiento']} - Skills: {i['skills']}")

def viewStudentReport():
    datos = abrirArchivo(RUTA_BASE_DATOS)
    count = 0
    for camper in datos['camper']:
        if camper['estado']['Cursando'] == True:
            if camper['riesgo'] == True:
                count += 1
                print("")
                print(f"{count}. {camper['nombre']} - cedula: {camper['cedula']}")
                pressEnter()
            else:
                print("")
                print('No existen campers reportados al momento.')
                pressEnter()
                break

def viewRendCamper():
    datos = abrirArchivo(RUTA_BASE_DATOS)
    camperEncontrado = False
    cedula = getInt('Ingrese la cedula del Camper: ')
    
    for camper in datos["camper"]:
        if camper["cedula"] == str(cedula):
            camperEncontrado = True
            if camper['riesgo'] == True:
                print("")
                print("El camper se encuentra en Bajo Rendimiento.")
                print(f"Modulo1 = {camper['notas']['modulo1']}")
                print(f"Modulo2 = {camper['notas']['modulo2']}")
                print(f"Modulo3 = {camper['notas']['modulo3']}")
                print(f"Modulo4 = {camper['notas']['modulo4']}")
                print(f"Modulo5 = {camper['notas']['modulo5']}")
                pressEnter()
            else:
                print('El camper tiene sus notas bien.')
                pressEnter()
            break 

    if not camperEncontrado:
        print('Cédula incorrecta.')
        pressEnter()

    


#----------------------------------------------------------------------------------------------------------------------------------------------------------
#CASE 3_Coordinacion

def cambiarCandidato(baseDatos):
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
                        camper['estado']['Inscrito'] = True
                        camper['estado']['Aprobado'] = True
                        print("El Camper ha sido aprobado con éxito.")
                    else:
                        camper['estado']['Inscrito'] = True
                        camper['estado']['Denegado'] = True
                        print("El Camper no alcanzó la puntuación de aprobación.")
                    encontrado = True
                    break
            if not encontrado:
                print("Cédula no encontrada.")
        case 3:
            datos = abrirArchivo(RUTA_BASE_DATOS)
            count = 0
            encontrado = False
            for camper in datos['camper']:
                for estado, valor in camper['estado'].items(): 
                    if estado == "Inscrito" and valor == True: 
                        encontrado = True
                        print(f"Nombre: {camper['nombre']} {camper['apellido']}, cedula: {camper['cedula']}")
                        pressEnter()
            if not encontrado:
                print('No hay ningun camper Inscrito aun.')
        case 4:
            datos = abrirArchivo(RUTA_BASE_DATOS)
            count = 0
            encontrado = False
            for camper in datos['camper']:
                for estado, valor in camper['estado'].items(): 
                    if estado == "Aprobado" and valor == True: 
                        encontrado = True
                        print(f"Nombre: {camper['nombre']} {camper['apellido']}, cedula: {camper['cedula']}")
                        pressEnter()
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
        print(f"{cont}. {i['ruta']}")  
    rut = input("Ingrese el número de la ruta: ") 
    rut = str(rut)
    if rut in datos["rutas"]:
        print("---- Estudiantes ----")
        for h in datos["grupos"]:
            if rut == str(h["ruta"]):
                print(f"Grupo: {h['nombre']}")
                for c in datos["camper"]:
                    if c["grupo"] == h["nombre"]:
                        print(f"Cédula: {c['cedula']}")
                        print(f"Nombre: {c['nombre']} {c['apellido']}")
                        print("")
                        pressEnter()
    else:
        print("La ruta seleccionada no es válida.")
        
def verGrupos():
    datos = abrirArchivo(RUTA_BASE_DATOS)
    count = 0
    for grupo in datos["grupos"]:
        count += 1
        print(f"{count}. Grupo: {grupo['nombre']} - Trainer: {grupo['trainer']} - Jornada: {grupo['jornada']}")
        print(f"Ruta: {grupo['ruta']} - Salon: {grupo['salon']} - Cantidad: {grupo['cantidad']}")
   





def createGrupo(baseDatos):
    grupo = {}
    print("..Ingresa el nombre")
    grupo["nombre"] = getDosDigitos('Ingresa la primer letra del grupo :')
    contT = 0
    salir = False
    while not salir:
        contT = 0
        for i in baseDatos["trainer"]:
            contT += 1
            print(f"{contT}. {i['nombre']} - cedula: {i['cedula']}")
        trainer = input("Ingresa la cedula del trainer: ")
        contT = 0
        for j in baseDatos["trainer"]:
            if j["cedula"] == trainer:
                grupo["trainer"] = j["cedula"]
                salir = True
        if not salir:
            print("Cedula de trainer invalida, ingresa un trainer existente")
    # --------------------------------------------------------------------
    grupo['jornada'] = showFind(baseDatos,'jornadas', "Ingrese la jornada :")
    # -------------------------------------------------------------------
    grupo['ruta'] = showFind(baseDatos,'rutas', "Ingrese la ruta :")
    # ------------------------------------------------------------------
    grupo['salones'] = showFind(baseDatos,'salones','Ingrese el salon :')
    # -----------------------------------
    grupo["cantidad"] = 0
    baseDatos['grupos'].append(grupo)
    return baseDatos



def crearGrupo():
    baseDatos = abrirArchivo(RUTA_BASE_DATOS)
    baseDatos = createGrupo(baseDatos)
    guardarArchivo(RUTA_BASE_DATOS, baseDatos)

def editGroup(baseDatos):
    salirse = False
    while not salirse:
        verGrupos()  
        grupo = getDosDigitos('Ingresa la letra del grupo :') 
        for z in baseDatos["grupos"]:
            if z["nombre"] == grupo:
                contT = 0
                salir = False
                while not salir:
                    contT = 0
                    for i in baseDatos["trainer"]:
                        contT += 1
                        print(f"{contT}. {i['nombre']} - cedula: {i['cedula']}")
                    trainer = input("Ingresa la cedula del trainer: ")
                    contT = 0
                    for j in baseDatos["trainer"]:
                        if j["cedula"] == trainer:
                            z["trainer"] = j["cedula"]
                            salir = True
                    if not salir:
                        print("Cédula de trainer inválida, ingresa un trainer existente")
                

                salir = False
                while not salir:
                    contJ = 0
                    for key, ruta in baseDatos["rutas"].items():
                        contJ += 1
                        print(f"{contJ}. {ruta['ruta']}")
                    ru = str(getInt("Ingresa el número de la ruta: ")) 
                    if ru in baseDatos["rutas"]:
                        ruta_seleccionada = baseDatos["rutas"][ru]
                        z["ruta"] = ru
                        print(f"Ruta seleccionada: {ruta_seleccionada['ruta']}")
                        print("Módulos de la ruta seleccionada:")
                        for key, modulo in ruta_seleccionada.items():
                            if key.startswith("modulo"): 
                                print(f"{key}: {modulo}")
                        salir = True
                    else:
                        print("Valor no válido, por favor ingresa un número de ruta válido")

                salirse = True
    return baseDatos


def editarGrupo():
    baseDatos = abrirArchivo(RUTA_BASE_DATOS)
    baseDatos = editGroup(baseDatos)
    guardarArchivo(RUTA_BASE_DATOS, baseDatos)


def administrarGrupos():
    while True:
        print (menuAdministrarGrupos)
        opcion = getInt("Ingrese la opcion: ")
        match opcion:
            case 1: 
                verGrupos()
                pressEnter()
            case 2: crearGrupo()
            case 3: editarGrupo()
            case 4: 
                pressEnter()
                return
            case _: print("Opcion no valida")

def groupAsign():
    datos = abrirArchivo(RUTA_BASE_DATOS)
    encontrado = False
    cedula = getStr1('Escribe cedula del camper asignar :') 
    
    for i in datos["camper"]:
        if cedula == i['cedula']:
            if 'Cursando' in i['estado'] and i['estado']['Cursando'] == True: 
                encontrado = True
                verGrupos() 
                print('Escribe el nombre del grupo a asignar')
                elegir = getDosDigitos('Escribe la letra :')  
                i['grupo'] = elegir

                grupo_encontrado = False
                for u in datos['grupos']:
                    if u['nombre'] == elegir:
                        grupo_encontrado = True
                        if u['cantidad'] == 33:
                            print('El grupo esta lleno')
                        else:
                            u['cantidad'] += 1  
                            guardarArchivo(RUTA_BASE_DATOS, datos)  
                            pressEnter()
                            break
                if not grupo_encontrado:
                    print("El grupo no existe.")
            else:
                encontrado = True
                print('El camper no está cursando!!!')
                pressEnter()
    
    if not encontrado:
        print('El usuario no existe, regístrese.')
        pressEnter()



                 
        
def expulsarCamper():
    datos = abrirArchivo(RUTA_BASE_DATOS)
    encontrado = False
    cedula = getStr1('Escribe cedula del camper :') 
    
    for i in datos["camper"]:
        if cedula == i['cedula']:
            if i['estado']['Cursando'] == True:
                encontrado = True
                i['estado']['Cursando'] = False
                i['estado']['Expulsado'] = True
                guardarArchivo(RUTA_BASE_DATOS, datos)
                print('El Camper fue expulsado exitosamente.')
                pressEnter()
                break
    if not encontrado:
        print('El usuario no existe.')
        pressEnter()


def graduarCamper():
    datos = abrirArchivo(RUTA_BASE_DATOS)
    encontrado = False
    cedula = getStr1('Escribe cedula del camper :') 
    
    for i in datos["camper"]:
        if cedula == i['cedula']:
            if i['estado']['Cursando'] == True:
                encontrado = True
                i['estado']['Cursando'] = False
                i['estado']['Graduado'] = True
                guardarArchivo(RUTA_BASE_DATOS, datos)
                print('El Camper fue graduado.')
                pressEnter()
                break
    if not encontrado:
        print('El usuario no existe.')
        pressEnter()
    
    pass

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
                    case 2: groupAsign()
                    case 3: 
                        expulsarCamper()
                    case 4:
                        graduarCamper()
                    case 5:
                        break
                    case _:
                        print("Opcion no valida")
            case 2: 
                pressEnter()
                changeCandidato() 
            case 3:
                pressEnter()
                return 
            case _: print("opcion invalida")

def administrarTrainers ():
    while True:
        print(menuCoordinadorTrainer)
        opc1 = getInt('Ingrese una opción: ')
        match opc1:
            case 1: addTrainer()
            case 2: 
                viewTrainers()
                pressEnter()
            case 3: 
                pressEnter()
                return
            case _: print("opcion invalida")


def reportes ():
    while True:
        print(menuCoordinadorReportes)
        opc1 = getInt('Ingrese una opción: ')
        match opc1:
            case 1: viewStudentReport()
            case 2: viewRendCamper()
            case 3: 
                pressEnter()
                return
            case _: print("opcion invalida")

def viewRutas():
    datos = abrirArchivo(RUTA_BASE_DATOS)
    cont = 0
    for i in datos["rutas"].values():
        cont += 1
        print(f"{cont}. {i['ruta']}")

    rutas = getInt('¿Qué ruta quieres ver? :')
    encontrado = False
    for key, ruta in datos["rutas"].items():
        if int(key) == rutas: 
            encontrado = True
            print(f"-------------{ruta['ruta']}---------------")
            print(f"Modulo 1: {ruta['modulo1']}")
            print(f"Modulo 2: {ruta['modulo2']}")
            print(f"Modulo 3: {ruta['modulo3']}")
            print(f"Modulo 4: {ruta['modulo4']}")
            print(f"Modulo 5: {ruta['modulo5']}")
            pressEnter()
            break
    if not encontrado:
        print("La ruta no se encuentra registrada, intente de nuevo.")


def addRutas():
    datos = abrirArchivo(RUTA_BASE_DATOS)
    cont = 0
    print("-------------------Rutas-------------")
    for i in datos["rutas"].values():
        cont += 1
        print(f"{cont}. {i['ruta']}")

    name  = input('Escriba el nombre de la nueva ruta :')
    modulo1 = input('Escriba el nombre del Modulo 1 :')
    modulo2 = input('Escriba el nombre del Modulo 2 :')
    modulo3 = input('Escriba el nombre del Modulo 3 :')
    modulo4 = input('Escriba el nombre del Modulo 4 :')
    modulo5 = input('Escriba el nombre del Modulo 5 :')
    newruta  = {
        "name": name,
        "modulo1": modulo1,
        "modulo2": modulo2,
        "modulo3": modulo3,
        "modulo4": modulo4,
        "modulo5": modulo5
    }

    next_key = str(len(datos["rutas"]) + 1)

    datos["rutas"][next_key] = {
        "ruta": newruta["name"],
        "modulo1": newruta["modulo1"],
        "modulo2": newruta["modulo2"],
        "modulo3": newruta["modulo3"],
        "modulo4": newruta["modulo4"],
        "modulo5": newruta["modulo5"]
    }
    pressEnter()
    print("-------------------Rutas Actualizadas-------------")
    for i in datos["rutas"].values():
        print(i["ruta"])
    pressEnter()

def rutas():
    while True:
        print(menuCoordinadorRutas)
        opcion = getInt('Ingrese una opcion :')
        match opcion:
            case 1: viewRutas()
            case 2: addRutas()
            case 3: 
                print('¡Adiós!')
                input('Presiona cualquier tecla para salir...')
                break
            case _:
                print('¡¡¡Opción inválida!!!')



def coordinacion():
    while True:
        print(menuCoordinador)
        opcion = getInt('Ingrese una opción: ')
        match opcion:
            case 1: 
                pressEnter()
                administrarCampers()
            case 2: 
                pressEnter()
                administrarTrainers()
            case 3: 
                pressEnter()
                reportes()
            case 4: 
                pressEnter()
                administrarGrupos()
            case 5: 
                rutas()
            case 6:
                print('¡Adiós!')
                input('Presiona cualquier tecla para salir...')
                break
            case _:
                print('¡¡¡Opción inválida!!!')

