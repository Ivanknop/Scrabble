import PySimpleGUI as sg
from codigo.interfaz.tema import mi_tema
import os.path
import pickle
from codigo.logica import configuracion

def layout():
    '''Diseña el layout de la ventana de configuración.
    Keys de los elementos: filas, columnas, tiempo,
    cantidades_x, puntajes_x (donde "x", una letra en mayúsculas),
    guardar, cancelar'''
    fuente_texto = 'Arial'
    tamaño_fuente = 12
    tamaño_letras = 10
    layout = [[sg.Text('Ajuste los valores de la configuración según lo desee', pad=((115, 0), (0, 0)), justification='center', font=('Italic', 16))],
                [sg.Text('Cantidad de filas: ', font=(fuente_texto, tamaño_fuente)), sg.Spin([i for i in range(5, 21)], initial_value=5, key='filas'), sg.Text('Cantidad de columnas: ', font=(fuente_texto, tamaño_fuente)), sg.Spin([i for i in range(5, 21)], initial_value=5, key='columnas'),
                sg.Text('Tiempo total (minutos): ', font=(fuente_texto, tamaño_fuente)), sg.Spin([i for i in range(5, 41)], key='tiempo')]]
    #Prepara los dos frames donde se configurará la cantidad de fichas de la bolsa y sus puntajes
    for objetivo in ['cantidades', 'puntajes']:
        frame_resultante = []
        fila = []
        #Cantidad de elementos a mostrar por fila del frame
        contador_salto = 5
        for i in range(ord('A'), ord('Z')+1):
            fila.extend([sg.Text(f'{chr(i)}: ', font=(fuente_texto, tamaño_letras)), sg.Spin([i for i in range(1, 31)], key=f'{objetivo}_{chr(i)}', size=(2, None))])
            #Dado que la N no suele preceder a la Ñ en la tabla ASCII, si llegué a la primera inserto la segunda a continuación
            if (chr(i) == 'N'):
                fila.extend([sg.Text('Ñ: ', font=(fuente_texto, tamaño_letras)), sg.Spin([i for i in range(1, 31)], key=f'{objetivo}_Ñ')])
                contador_salto = contador_salto - 1
            contador_salto = contador_salto - 1
            if (contador_salto < 1):
                frame_resultante.append(fila)
                fila = []
                contador_salto = 5
        if (len(fila) != 0):
            frame_resultante.append(fila)
        if (objetivo == 'cantidades'):
            layout.append([sg.Frame(layout=frame_resultante, font=('Italic 12'), title='Cantidad de fichas', element_justification='left')])
        else:
            #En el layout, toma la última lista que se insertó (la que contiene el primer frame) y le agrega el frame recién creado.
            #Esto causa que el espacio con los puntajes se vea a la derecha del de la bolsa, en lugar de debajo.
            layout[-1].extend([sg.Frame(layout=frame_resultante, font=('Italic 12'), title='Puntajes de las fichas', element_justification='right')])
    casilleros_especiales = [[sg.Text('Seleccione los casilleros especiales que le gustaría que apareciesen: ')],
                                [sg.Checkbox('+: Suma 5 puntos al valor de la palabra', default=True, key='*sum'), sg.Checkbox('-: Resta 5 puntos al valor de la palabra', default=True, key='*rest')],
                                [sg.Checkbox('*: Duplica el valor de la palabra', default=False, key='*mult') ,sg.Checkbox('%: Divide a la mitad el valor de la palabra', default=False, key='*div')],
                                [sg.Checkbox('0: Anula el valor total de la palabra', default=False, key='*0')]]
    layout.extend(casilleros_especiales)
    layout.append([sg.Button('Guardar y jugar', key='guardar', button_color=('Black', 'White')), sg.Button('Cancelar', key='cancel', button_color=('Black','White'))])
    return layout

def obtener_especiales(ventana):
    '''Retorna una lista con los casilleros especiales que se
    marcaron en las checkbox'''
    especiales = []
    if (ventana['*sum'].Get()):
        especiales.append('*sum')
    if (ventana['*rest'].Get()):
        especiales.append('*rest')
    if (ventana['*mult'].Get()):
        especiales.append('*mult')
    if (ventana['*div'].Get()):
        especiales.append('*div')
    if (ventana['*0'].Get()):
        especiales.append('*0')
    return especiales

def generar_configuracion(ventana, conf):
    '''Crea un diccionario con la información proporcionada por el usuario,
    su estructura es idéntica a la de los niveles predeterminados.
    Además, controla que no se hayan ingresado datos incorrectos'''
    #Al inicio, se asume que no hay ningún error
    conf['error'] = ''
    conf['nivel'] = 'personalizado'

    #Evalúa si los datos en los spin de filas, columnas y tiempo son correctos
    for spin in ['filas', 'columnas', 'tiempo']:
        valor_spin = ventana[f'{spin}'].Get()
        try:
            valor_spin = int(valor_spin)
        except:
            conf['error'] = 'Se asignó un valor no numérico a la cantidad de filas, columnas o al tiempo'
            return conf
        if (valor_spin < 5):
            conf['error'] = 'Se asignó un valor menor a 5 a la cantidad de filas, columnas o al tiempo'
            return conf
        conf[spin] = valor_spin

    #Comprueba que los spin de cantidades y puntajes sean correctos. Si es así,
    #almacena la información en diccionarios
    cant_fichas = {}
    puntaje_ficha = {}
    for frame in ['cantidades', 'puntajes']:
        for i in range(ord('A'), ord('Z')+2):
            letra = chr(i)
            if (i == (ord('Z') + 1)):
                letra = 'Ñ'
            #Obtiene el contenido del spin según el frame en el que se encuentre y la letra actual
            valor_spin = ventana[f'{frame}_{letra}'].Get()
            #Si se ingresó otro caracter que no sea un entero, se guardará el error y dejara de iterar
            try:
                valor_spin = int(valor_spin)
            except:
                conf['error'] = f'Se asignó un valor no numérico a la letra {letra} en el espacio de {frame}'
                return conf
            #Si se ingreso un entero no valido, hará lo mismo que en el paso anterior
            if (valor_spin < 1):
                conf['error'] = f'La letra {letra} posee valor nulo o negativo en el espacio de {frame}'
                return conf
            cant_fichas[f'{letra}'] = valor_spin
            #Si el frame actual es el de puntajes...
            if (frame == 'puntajes'):
                #...y el valor del spin no se encuentra en el diccionario de puntajes, crea la clave y le asigna la primer letra
                if (valor_spin not in puntaje_ficha):
                    puntaje_ficha[valor_spin] = [letra]
                else:
                    #Si no, agrega una nueva letra en ese espacio
                    puntaje_ficha[valor_spin].append(letra)

    #Asigna los diccionarios resultantes (cantidades y puntuación) a la configuración global
    conf['cant_fichas'] = cant_fichas
    conf['puntaje_ficha'] = puntaje_ficha
    #Agrega casilleros especiales al tablero
    especiales_seleccionados = obtener_especiales(ventana)
    conf['especiales'] = configuracion.especial(conf['filas'], conf['columnas'], conf['nivel'], especiales_seleccionados)
    return conf

def cargar_configuracion(usuario):
    directorio = os.path.join('guardados', f'configuracion_{usuario}.pckl')
    with open(directorio, 'rb') as archivo:
        configuracion = pickle.load(archivo)
    return configuracion

def guardar_configuracion(configuracion, usuario):
    #En un futuro, si se implementa la opción de tener multijugadores, se cargará
    #la configuración de cada usuario individualmente
    directorio = os.path.join('guardados', f'configuracion_{usuario}.pckl')
    with open(directorio, 'wb') as archivo:
        pickle.dump(configuracion, archivo)

def interfaz_personalizacion(usuario):
    '''Muestra la interfaz de configuración y controla sus eventos'''
    conf = {}
    mi_tema()
    ventana = sg.Window('Configuración personalizada', layout())
    ventana.Finalize()
    while True:
        event, values = ventana.Read()
        if (event == None):
            break
        if (event == 'cancel'):
            break
        if (event == 'guardar'):
            configuracion = generar_configuracion(ventana, conf)
            #Si no hay ningún error en la configuración, la guarda
            if (len(configuracion['error']) == 0):
                guardar_configuracion(configuracion, usuario)
                break
            else:
                sg.popup(configuracion['error'])
    ventana.close()
    return conf

if __name__ == '__main__':
    interfaz_personalizacion()
