import os
import json
from codigo.interfaz import configuracion_personalizada

def cargar_usuarios():
    try:
        directorio_usuarios = os.path.join('guardados', 'usuarios.json')
        with open(directorio_usuarios, 'r') as archivo:
            usuarios = json.load(archivo)
    except:
        usuarios = []
    return usuarios

def guardar_usuarios(usuarios):
    directorio_usuarios = os.path.join('guardados', 'usuarios.json')
    with open(directorio_usuarios, 'w') as archivo:
        json.dump(usuarios, archivo)

def eliminar_partida(partida, usuarios):
    usuarios.remove(partida)
    guardar_usuarios(usuarios)
    filename_partida = os.path.join('guardados', f'partida_{partida}')
    if (os.path.isfile(filename_partida)):
        os.remove(filename_partida)
    configuracion_personalizada.eliminar_configuracion(partida)
