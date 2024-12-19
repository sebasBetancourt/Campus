import json

def abrirArchivo(archivo):
    with open(f"./archivosJ/{archivo}.json","r") as archivoAbrir:
        final = json.load(archivoAbrir)
    return final
def guardarArchivo(archivo,diccionario):
    objetoJson= json.dumps(diccionario, indent=4)
    with open(f'./archivosJ/{archivo}.json',"w") as archivoAbrir:
        archivoAbrir.write(objetoJson)



RUTA_BASE_DATOS = 'baseDatos' 

baseDatos = abrirArchivo('baseDatos')