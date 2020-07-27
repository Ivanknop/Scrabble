import PySimpleGUI as sg
from codigo.logica.puntuaciones_maximas import*
from codigo.interfaz.interfaz_puntaje import*
from codigo.interfaz.tema import *
from codigo.interfaz.interfaz_palabras import*
from codigo.logica.jugador import*

def ver_ganador (jug,pc,ven):
    '''
    Primero actualiza la pantalla con los puntajes de ambos jugadores. Después define el vencedor.
    '''
    ven['pje_jug'].update(value=jug)
    ven['pje_pc'].update(value=pc)
    if int(jug) > int(pc):
        ven['ganador'].update(value='FELICIDADES, ¡¡GANASTE!!')
    elif int(jug) < int(pc):
        ven['ganador'].update(value='QUÉ LÁSTIMA.. PERDISTE')
    else:
        ven['ganador'].update(value='EMPATE SOBRE EL FINAL')

def terminar(nombre, punt_jug,punt_pc,pal_jug,pal_pc,nivel):
    '''
    Construye una interfaz para determinar qué jugador salió vencedor. Permite acceder a las palabras que cada uno utilizó y
    a las puntuaciones máximas
    '''
    contenido = [
        [sg.Text('TU PUNTAJE FINAL',size=(40,1),font=('Impact',14),justification='center',text_color=('#D09F61'),key='_jug')],
        [sg.Text(key='pje_jug',size=(50,1),justification='center',font=('Arial',50),background_color='Black',text_color='white')],
        [sg.Text('PUNTAJE DE LA PC',size=(40,1),font=('Impact',14),justification='center',text_color=('#D09F61'),key='_pc')],
        [sg.Text(key='pje_pc',size=(50,1),justification='center',font=('Arial',50),background_color='Black',text_color='white')],
        [sg.Text(key='ganador',size=(50,1),justification='center',font=('Arial',20),background_color='Black',text_color='white')],
        [sg.Text('',size=(5,1)),
        sg.Button('Salir', font=('Arial', 10), size=(10, 2),button_color=('black', '#f75404'), key='salir'),
        sg.Button('Listado de palabras', font=('Arial', 10), size=(10, 2),button_color=('black', '#f75404'), key='list_pal'),
        sg.Button('Puntuaciones Máximas', font=('Arial', 10), size=(10, 2),button_color=('black', '#f75404'), key='puntajes')]

        ]
    mi_tema()
    ven = sg.Window ('Ganador',layout=contenido,size= (400,400), no_titlebar=False,keep_on_top=True)
    ven.finalize()
    
    nuevo_pje = True
    while True:         
        #Abre la ventana donde se ve quién ganó
        ver_ganador (punt_jug,punt_pc,ven)
        puntaje = Puntuacion_Maxima()
        if nuevo_pje: #Controla no agregar más de una vez un puntaje a las puntuaciones máximas
            puntaje.agregar(Jugador(nombre,punt_jug,nivel))
            nuevo_pje = False
        event, values = ven.read()
        if event in (None,'salir'):
            break
        if event == 'list_pal':
            #Abre la ventana de las palabras utilizadas
            listado_palabras(pal_jug,pal_pc)
        if event == 'puntajes':
            #Abre la ventana de puntuaciones máximas
            puntajes()             
    ven.close()
    
if __name__ == '__main__':
    terminar()
