import random
import PySimpleGUI as sg
from codigo.interfaz.tema import mi_tema

def infoConfiguracion(conf):
    '''Crea una ventana que muestra la configuración
    de la partida que se está jugando.'''
    layout = [
                [sg.Text('Nivel: '), sg.Text(f'{conf["nivel"].capitalize()}')],
                [sg.Text('Filas: '), sg.Text(f'{conf["filas"]}')],
                [sg.Text('Columnas: '), sg.Text(f'{conf["columnas"]}')],
                [sg.Text('Tiempo: '), sg.Text(f'{conf["tiempo"]} minutos')],
                [sg.Text('Cantidad de letras: ')]
                ]
    contador_salto = 6
    letras = []
    for clave, valor in sorted(conf['cant_fichas'].items()):
        letras.append(sg.Text(f'{clave}: {valor}'))
        contador_salto = contador_salto - 1
        if (contador_salto == 0):
            contador_salto = 6
            layout.append(letras)
            letras = []
    #Si quedaron letras por insertar antes de que se completara una fila, las agrega
    if (len(letras) != 0):
        layout.append(letras)
    layout.append([sg.Text('Puntajes de las fichas: ')])
    letras = []
    for clave in sorted(conf['puntaje_ficha'].keys()):
        letras.append(sg.Text(f'{clave}: '))
        for fichas in conf['puntaje_ficha'][clave]:
            letras.append(sg.Text(fichas))
        layout.append(letras)
        letras=[]
    layout.extend([[sg.Text('Casilleros especiales: ')], [sg.Text('+: Obtienes 5 puntos adicionales')], [sg.Text('-: Pierdes 5 puntos del total conseguido')], [sg.Text('x2: Duplica el valor de la palabra')], [sg.Text('%2: Divide a la mitad el total de la palabra')], [sg.Text('0: Anula el valor de la palabra')]])
    layout.append([sg.Button('Volver',button_color=('black', '#f75404'),key='volverConf')])

    mi_tema()
    ventana = sg.Window('configuracion',layout=layout,size=(300,670),no_titlebar=True,grab_anywhere=True, keep_on_top=False).Finalize()

    while True:
        event, value = ventana.read()
        if event == 'volverConf'  :
            break
        elif event == None:
            break
    ventana.close()

def especial(filas, columnas, nivel, esp_personalizados=[]):
    '''Genera casilleros especiales según el nivel,
    teniendo en cuenta la cantidad de columnas, filas y la dificultad.
    Además, controla que exista cierta cantidad de casilleros especiales'''
    especiales = {}
    if nivel == 'facil':
        esp = ['*rest', '*sum']
        minEsp= 10
    elif nivel == 'medio':
        esp = ['*rest', '*sum', '*mult', '*div' ]
        minEsp = 7
    elif nivel == 'dificil':
        esp = ['*rest', '*sum', '*mult', '*0', '*div']
        minEsp = 7
    else:
        esp = esp_personalizados
        if (len(esp) == 0):
            return especiales
    for fila in range(filas):
        for columna in range(columnas):
            probabilidad = random.randint(0, 100)
            if probabilidad < 25:
                #Crea el casillero especial
                coordenada = str(fila) + ', ' + str(columna)
                random.shuffle(esp)
                especiales[coordenada] = esp[0]
    return especiales

def nivel_facil():
    conf = {
        'nivel':'facil',
        'filas':15,
        'columnas':15,
        'especiales':{},

        'tiempo': 25, #minutos
        'cant_fichas': {'A':11, 'E':11, 'O':8, 'S':7, 'I':6,'U': 6, 'N': 5, 'L': 4, 'R': 4, 'T': 4,'C': 4, 'D': 4, 'G': 2, 'M': 3, 'B': 3,'P': 2, 'F': 2, 'H': 2, 'V': 2, 'Y': 1,'J': 2, 'K': 1, 'Ñ': 1, 'Q': 1, 'W': 1, 'X': 1, 'Z': 1 },

         #  dic el indice indica le puntaje y lo valores son las letras que itenen ese puntaje
        # tienen mayor puntaje que otros niveles
         'puntaje_ficha' : {
        5: ['A', 'E', 'O', 'S', 'I', 'U', 'N', 'L', 'R', 'T'],
        2: ['C', 'D', 'G'],
        8: ['M', 'B', 'P'],
        4: ['F', 'H', 'V', 'Y'],
        6: ['J'],
        9: ['K', 'Ñ', 'Q', 'W', 'X'],
        10: ['Z']
    }
    }
    conf['especiales'] = especial(conf['filas'], conf['columnas'],conf['nivel'])
    return conf


def nivel_medio():
    # tiene menor cantidad de vocales
    # tiene menos punto las letras
    #el tablero sera un poco mas chico
    #y menor tiempo de juego
    conf = {
        'nivel': 'medio',
        'filas':15,
        'columnas':15,
        'especiales': {},
        'tiempo': 20, #minutos
        # el indice es la letra y e lvalor la cantidad de fichas de esa letra

        'cant_fichas' : {
        'A':9, 'E':9, 'O' :8, 'S' :7, 'I' :6,
        'U':6, 'N':5, 'L':4, 'R':4, 'T':4,
        'C':4, 'D':4, 'G' :2, 'M' :3, 'B' :3,
        'P' :2, 'F' :2, 'H' :2, 'V':2, 'Y' :1,
        'J':2, 'K' :1, 'Ñ' :1, 'Q' :1, 'W' :1, 'X' :1, 'Z' :1
    },

         #  dic el indice indica le puntaje y lo valores son las letras que itenen ese puntaje
         'puntaje_ficha' : {
        1: ['A', 'E', 'O', 'S', 'I', 'U', 'N', 'L', 'R', 'T'],
        2: ['C', 'D', 'G'],
        3: ['M', 'B', 'P'],
        4: ['F', 'H', 'V', 'Y'],
        6: ['J'],
        8: ['K', 'Ñ', 'Q', 'W', 'X'],
        10: ['Z']
    }
    }
    conf['especiales'] = especial(conf['filas'], conf['columnas'],conf['nivel'])
    return conf


def nivel_dificil():
    # tiene menor cantidad de vocales
    # misma puntuacion que en el nivel medio
    # el tablero sera igual al nivel medio
    # y menor tiempo de juego
    # tendra mas casilleros que restan puntos
    conf = {
        'nivel': 'dificil',
        'filas': 10,
        'columnas': 10,
        'especiales': {},  # ver de armarl ode forma random
        'tiempo': 15,  # minutos
        # el indice es la letra y e lvalor la cantidad de fichas de esa letra

        'cant_fichas': {
            'A':9, 'E':9, 'O' :8, 'S' :7, 'I' :6,
        'U':6, 'N':5, 'L':4, 'R':4, 'T':4,
        'C':4, 'D':4, 'G' :2, 'M' :3, 'B' :3,
        'P' :2, 'F' :2, 'H' :2, 'V':2, 'Y' :1,
        'J':2, 'K' :1, 'Ñ' :1, 'Q' :1, 'W' :1, 'X' :1, 'Z' :1
        },

        #  dic el indice indica le puntaje y lo valores son las letras que itenen ese puntaje
        'puntaje_ficha': {
            1: ['A', 'E', 'O', 'S', 'I', 'U', 'N', 'L', 'R', 'T', 'C', 'D', 'G'],
            3: ['M', 'B', 'P'],
            4: ['F', 'H', 'V', 'Y'],
            6: ['J'],
            8: ['K', 'Ñ', 'Q', 'W', 'X'],
            10: ['Z']
        }
    }
    conf['especiales'] = especial(conf['filas'], conf['columnas'],conf['nivel'])
    return conf
