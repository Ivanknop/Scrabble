import PySimpleGUI as sg
import os
from codigo.interfaz.tema import mi_tema

def general(dirAyuda):
    sg.theme_text_element_background_color('#4f280a')
    sg.theme_element_background_color('#4f280a')
    col = [[sg.Image(filename=f'{dirAyuda}ayuda 3.png'),sg.Text('Muestra la Ayuda',font=('Arial, 16'),text_color='white')], #botón ayuda
           [sg.Image(filename=f'{dirAyuda}ayuda 5.png'),sg.Text('Comenzar a jugar',font=('Arial, 16'),text_color='white')], #botón comenzar a jugar
           [sg.Image(filename=f'{dirAyuda}ayuda 9.png'), sg.Text('Muestra la Tabla de Puntajes', font=('Arial, 16'), text_color='white')], #botón puntajes
           [sg.Image(filename=f'{dirAyuda}ayuda 6.png'), sg.Text('Iniciar una Nueva partida', font=('Arial, 16'), text_color='white')], #botón nueva partida
           [sg.Image(filename=f'{dirAyuda}ayuda 4.png'), sg.Text('Carga una partida guardada', font=('Arial, 16'), text_color='white')], #botón cargar partida
           [sg.Image(filename=f'{dirAyuda}ayuda 10.png'), sg.Text('Vuelve al Menu principal', font=('Arial, 16'), text_color='white')], #botón volver menú principal
           [sg.Image(filename=f'{dirAyuda}ayuda 22.png'), sg.Multiline(default_text=
                                                      'En esta ventana se configuran los datos para la nueva partida: \n'
                                                      'El apodo debe tener entre 3 y 10 caracteres y no se pueden utilizar caracteres especiales;' 
                                                      'Hay que elegir una dificultad y se puede cambiar el Avatar. \n'
                                                      'Se pueden elegir entre las dificultades Fácil, Medio o Díficil; también se puede personalizar toda la partida. \n' 
                                                      'Al momento de oprimir en Jugar se muestra un ventana de confirmación.\n'
                                                      'En todo momento se puede cancelar esta acción\n',
                                                        auto_size_text=True, font=('Arial, 12'), text_color='white', disabled=True, size=(30,10),background_color='#4f280a')],
    ]
    layout = [sg.Column(col,scrollable=True,background_color='#4f280a',vertical_scroll_only=True,size=(700,470))]
    return layout

def juego(dirAyuda):
    col = [     #Ayuda 14 = tablero, ayuda 0 = timer
        [sg.Image(filename=f'{dirAyuda}ayuda 14.png'), sg.Multiline('Vista general del Tablero. A continuación se encuentra detallada la información sobre cómo jugar', font=('Arial, 16'), text_color='white', disabled=True, size=(25,10),background_color='#4f280a')],
        [sg.Image(filename=f'{dirAyuda}ayuda 0.png')], [sg.Multiline('En el area superior se encuentra el indicador de Tiempo y los botones de Pausa Ayuda.\n'
                                                                     '\n1) TEMPORIZADOR: en tiempo jugado (indicado con números en el area negra) se ve el tiempo transcurrido. '
                                                                     'La barra de color naranja indica el tiempo RESTANTE, que se reduce a medida que pasa el tiempo.\n'
                                                                     '2) Si se oprime el boton de pausa, la partida queda detenida y se despliega un menú de opciones (abajo explicadas).\n'
                                                                     '3)El simbolo de \"?\" abre esta misma ayuda.\n ', font=('Arial, 12'), text_color='white' ,autoscroll=True, disabled=True, size=(40,8),background_color='#4f280a')],
        [sg.Image(filename=f'{dirAyuda}ayuda 8.png'), #Botón para ver configuración de nivel
         sg.Multiline('Sobre los avatares de los jugadores, se encuentra un botón que al presionarlo '
                 'muestra la configuración elegida para la partida', font=('Arial, 12'), text_color='white',autoscroll=True, disabled=True, size=(30,6),background_color='#4f280a')],
        [sg.Image(filename=f'{dirAyuda}ayuda 19.png'), #indicadorJugador
         sg.Multiline('A la derecha del tablero se encuentra el Avatar de cada jugador; '
                 'debajo se encuentra el apodo elegido y los puntos acumulados en la partida. \n '
                 'El apodo remarcado con color verde indica de quién es el turno', font=('Arial, 12'), text_color='white',autoscroll=True, disabled=True, size=(30,8),background_color='#4f280a')],
        [sg.Image(filename=f'{dirAyuda}ayuda 1.png'), #atril
         sg.Multiline('Debajo de los  avatares se encuentra el atril con sus fichas '
                  ' junto al boton de VALIDAR (símbolo check) y CAMBIAR FICHAS (bolsa).'
                 '\n  Cuando se selecciona una ficha esta se pondra transparente como se indica en la imagen. \n'
                  'En el area superior del atril se comenzará a visualizar la palabra en formación.\n'
                  'Nota: al seleccionar una ficha no se puede presionar la bolsa para cambiar las fichas.\n'
                 'Nota 2: si deja el mouse sobre una ficha esta muestra una etiqueta con el puntaje de la misma.\n'
                 'En el botón de preferencias pueden verse todos los puntajes para esa partida.', font=('Arial, 12'), text_color='white',autoscroll=True, disabled=True, size=(20,8),background_color='#4f280a')],
        [sg.Image(filename=f'{dirAyuda}ayuda 2.png')], #atril validado
         [sg.Multiline('Una vez que se formó la palabra, se debe dar click en el boton de validar. Si esta es válida, '
                  'ScrabbleAR le indicará que seleccione dónde insertarla.\n'
                  'En la pestaña de REGLAS podr{a consultar las reglas generales de ScrabbleAR'
                  'como se ve en la imagen', font=('Arial, 12'), text_color='white',autoscroll=True, disabled=True, size=(40,8),background_color='#4f280a')],
        [sg.Image(filename=f'{dirAyuda}ayuda 33.png'), sg.Multiline('Cuando se hace click en un casillero del tablero con una palabra ya validada,\n'
                                                                       'se muestra el indicador de orientacion. Una vez elegida,la palabra quedara insertada en el tablero.',
                                                            font=('Arial, 12'), text_color='white',autoscroll=True, disabled=True, size=(30,8),background_color='#4f280a')],
        [sg.Image(filename=f'{dirAyuda}ayuda 27.png'), sg.Image(filename=f'{dirAyuda}ayuda 28.png'), ], #palabra pc y palabra jugador
        [sg.Multiline('En el tablero las palabras con fondo ROJO son las insertadas por el oponente '
                 'y las de fondo VENDE son las suyas',font=('Arial, 12'), text_color='white',autoscroll=True, disabled=True, size=(40,5),background_color='#4f280a')],
        [sg.Image(filename=f'{dirAyuda}ayuda 7.png'), sg.Multiline('Si en la Bolsa de Fichasa parece "FINALIZAR", puede que pasen dos cosas:\n'
                                                                     '- No hay mas fichas en la bolsa\n - No puedes cambiar mas fichas (maximo tres cambios) ',
                                                            font=('Arial, 12'), text_color='white',autoscroll=True, disabled=True, size=(20,10),background_color='#4f280a')],
        [sg.Image(filename=f'{dirAyuda}ayuda 30.png'), sg.Image(filename=f'{dirAyuda}ayuda 29.png'),sg.Image(filename=f'{dirAyuda}ayuda 18.png'),], #pausa, pantalla final, historial palabras
         [sg.Multiline('Aqui puede verse el menu de Pausa.\n'
                  'Se puede retornar a la partida, guardarla o abandonar. \n' 
                  'En caso de abandonar o finalizar o si se terminó el tiempo,se verá la ventana de final de partida. '
                  'Aquí se muestran los puntos de cada jugador y quién ganó.'
                  ' En esta ventana si usted presiona el boton de Listado de palabras '
                  'podrán verse las palabras que insertó cada jugador y los puntos que hizo con cada una'
                  ,font=('Arial, 12'), text_color='white',autoscroll=True, disabled=True, size=(40,8),background_color='#4f280a')],
        ]
    layout = [sg.Column(col,scrollable=True,background_color='#4f280a', vertical_scroll_only=True,size=(700,470))]
    return layout

def iconCas(dirAyuda):
    col = [
        [sg.Image(filename=f'{dirAyuda}ayuda 25.png'), sg.Text('Casillero seleccionado para insertar palabra', font=('Arial, 16'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}ayuda 24.png'), sg.Text('Insertar horizontalmente', font=('Arial, 16'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}ayuda 23.png'), #estos tres son la orientación
         sg.Text('Insertar verticalmente', font=('Arial, 18'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}ayuda 34.png'), #suma
         sg.Text('Incrementa 5 puntos el valor total de la palabra', font=('Arial, 16'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}ayuda 20.png'), #resta
         sg.Text('Resta 5 puntos al valor total de la palabra', font=('Arial, 16'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}ayuda 21.png'), #multiplica x 2
         sg.Text('Duplica el valor de la palabra', font=('Arial, 16'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}ayuda 15.png'), #divide
         sg.Text('Divide a la mitad el valor de la palabra', font=('Arial, 16'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}ayuda 11.png'), #multiplica x 0
         sg.Text('Anula el valor de la palabra', font=('Arial, 16'), text_color='white')],
        ]
    layout = [sg.Column(col,scrollable=True,background_color='#4f280a', vertical_scroll_only=True,size=(700,470))]
    return layout

def otros(dirAyuda):
    col = [
        [sg.Image(filename=f'{dirAyuda}ayuda 3.png'), sg.Text(' Muestra la Ayuda', font=('Arial, 18'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}ayuda 5.png'), sg.Text(' Comenzar a jugar', font=('Arial, 18'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}ayuda 9.png'),
         sg.Text('Muestra la Tabla de Puntajes', font=('Arial, 18'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}ayuda 6.png'),
         sg.Text('Iniciar una Nueva partida', font=('Arial, 18'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}ayuda 4.png'),
         sg.Text('Carga la ultima partida guardada. Si existe', font=('Arial, 18'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}ayuda 10.png'),
         sg.Text('Vuelve al Menu principal', font=('Arial, 18'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}ayuda 22.png'), sg.Text('',
                                                            font=('Arial, 18'), text_color='white')],
        ]
    layout = [sg.Column(col,scrollable=True,background_color='#4f280a', vertical_scroll_only=True,size=(700,470))]
    return layout

def reglas():
    imgReglas = os.path.join('media', 'ayuda', 'ayuda 39.png') #reglas
    col = [[sg.Image(filename=imgReglas)],
           [sg.Multiline('¡¿Cómo te va?! Vamos a jugar al ScrabbleAR. Veamos bien cómo se juega...'
                         'Sí, es el famoso juego de mesa donde probarás tu conocimiento acerca de las palabras realmente '
                         'existentes. Frente a tí tendrás al computador. ¿Serás capaz de derrotarlo? Lo primero que debes saber '
                         'es que las distintas dificultades afectan la inteligencia del ordenador. ¿Inteligencia? Dejémoslo así'
                         '  por el momento. Puedes elegir entre FÁCIL, MEDIO, o DIFÍCIL o PERSONALIZAR íntegramente la partida .Además   de   tener   un  '
                         ' adversario más complejo de enfrentar, cambian algunas disposiciones del juego. Si quieres'
                         ' más detalles puedes ir a la sección específica en estas mismas reglas. \n'
                         'Una vez elegida la dificultad se abrirá el Tablero de juego y comenzará la verdadera prueba. En este juego tienes tres cosas para '
                         'hacer:\n •Escoger entre las fichas de tu atril la combinación que forme la mejor palabra posible (cada letra posee '
                         'una puntuación propia, así que toda palabra tiene un puntaje) y, luego de eso, colocarla en la mejor  '
                         ' posición del tablero. Un detalle, antes de colocar tu palabra en el tablero deberás'
                         ' validarla. No queremos tramposos.\n •Cambiar tus fichas por nuevas. ¡Ojo! Sólo dispones de 3 (tres) '
                         'cambios por partida.•Rendirte... Bueno, esto mejor no.Presta mucha atención al tablero de juego. Encontrarás '
                         'casilleros especiales donde se sumaránpuntos o quizás multipliques el valor de la palabra... Pero '
                         'también hay otros que restan, dividen ohasta multiplican el valor total por CERO. Escoge con mucho '
                         'cuidado dónde colocarás tu palabra.Por suerte para tí esto también afecta al ordenador.Las   palabras  '
                         ' pueden insertarse en vertical u horizonal. En este juego no podrás hacerlo '
                         'en diagonal. Tampoco está permitido que se crucen las palabras entre sí. Calcula muy bien los '
                         'espacios disponibles.¿Cuándo termina la partida? Cuando no hay más fichas en algún atril y '
                         'tampoco en la bolsa de fichas, cuando no hay espacios en el Tablero o cuando alguno de los dos '
                         'jugadores han agotado sus cambios de fichas disponibles y aún así no tienen dónde jugar una nueva'
                         ' combinación de letras. Al finalizar se comparan las puntuaciones y... ¡Tenemos un ganador!',
                         font=('Arial',12),text_color='white',size=(53,40),autoscroll=True,
                         pad=((10,10),10),disabled=True,background_color='#4f280a')],

    ]
    layout = [sg.Column(col,scrollable=True,background_color='#4f280a',element_justification='center', justification='center', vertical_scroll_only=True,size=(720,470))]
    return layout

def popReglas():
    layout = [reglas(),
              [sg.Button('Comenzar!',size=(20,5),key='comenzar')],]
    ventana = sg.Window('Reglas', layout=layout,element_justification='center',
                        no_titlebar=True,grab_anywhere=True, keep_on_top=True,background_color='#afad71',border_depth=50).Finalize()
    while True:
        event, values = ventana.read()
        if event in ( None,'comenzar'):
            break
    ventana.close()

def niveles(dirAyuda):
    col = [[sg.Frame(
            layout=[[sg.Multiline(' Tamaño tablero: 20*20.\n'
                             '>Puntaje de Fichas:\n'
                             '\tVocales y consonantes L, N, S, T, R = 5 pts\n' 
                             '\tC, D, G = 2 pts \n'
                             '\tM, B, P = 8 pts \n '
                             '\tF, H, V, Y = 4 pts \n'
                             '\tJ = 6 pts\n'
                             '\tK, Ñ, Q, W, X = 9 pts\n' 
                             '\tZ= 10 pts \n\n'
                             '>Cantidad de fichas:  99\n\n'
                             '>Duración de la partida: 25 minutos\n\n'
                             '>Tipo de casilleros especiales: Suma y Resta\n\n'
                             '>Cantidad de Cambios computador: 1\n\n'
                             '>Tipos de palabras permitidas: sustantivos, adjetivos y verbos\n\n'
                             '>Dificultad de la PC: Busca la primer palabra posible y la inserta en el primer lugar disponible en el tablero.\n',
                             font=('Arial, 12'), text_color='black',autoscroll=True, disabled=True, size=(45,8),background_color='#afad71')]],
            title='Nivel Facil', title_color='white' , relief=sg.RELIEF_SUNKEN, font=('Impact 24'),
            element_justification='left',  key='contenedor_facil'),],
        [sg.Frame(
            layout=[[sg.Multiline('Tamaño tablero 15*15. \n'
                             '>Puntaje de Fichas: \n'
                             '\tVocales y L, N, S, T, R = 1 pts\n'
                             '\tC, D, G = 2 pts\n'
                             '\tM, B, P = 3 pts\n'
                             '\tF, H, V, Y = 4 pts\n'
                             '\tJ = 6 pts\n'
                             '\tK, Ñ, Q, W, X = 8 pts\n'
                             '\tZ= 10 pts\n\n'
                             '>Cantidad de fichas: 95\n\n'
                             '>Duración de la partida: 20 minutos\n\n'
                             '>Tipo de casilleros especiales: Suma, resta, Multiplica x 2, Divide x2.\n\n'
                             '>Cantidad de Cambios computador: 1\n\n'
                             '>Tipos de palabras permitidas: sustantivos, adjetivos y verbos\n\n'
                             '>Dificultad de la PC: Evalúa la primer palabra que puede formar y analiza en el tablero cuál es la mejor posición.\n',
                             font=('Arial, 12'), text_color='black',autoscroll=True, disabled=True, size=(45,8),background_color='#afad71')]],
            title='Nivel Medio', title_color='white' , relief=sg.RELIEF_SUNKEN, font=('Impact 24'),
            element_justification='center', key='contenedor_medio'), ],
        [sg.Frame(
            layout=[[sg.Multiline('Tamaño tablero: 10*10\n'
                             '>Puntaje de Fichas: \n'
                             '\tVocales y L, N, S, T, R = 1 pts\n'
                             '\tC, D, G = 1 pts \n'
                             '\tM, B, P = 3 pts\n'
                             '\tF, H, V, Y = 4 pts\n'
                             '\tJ = 6 pts\n'
                             '\tK, Ñ, Q, W, X = 8 pts\n'
                             '\tZ= 10 pts\n\n'
                             '>Cantidad de fichas: 95\n\n'
                             '>Duración de la partida: 15 minutos\n\n'
                             '>Tipo de casilleros especiales: Suma, Resta, Multiplica x 2, Divide x2, Anula valor de la palabra\n\n'
                             '>Cantidad de Cambios computador: 1\n\n'
                             '>Tipos de palabras permitidas: adjetivos y verbos\n\n'
                             '>Dificultad de la PC: Prueba todas las palabras posibles y cuáles puede insertar en las mejores posiciones a fin de encontrar la mejor combinación palabra-espacio.\n',
                             font=('Arial, 12'), text_color='black',autoscroll=True, disabled=True, size=(45,8),background_color='#afad71')]],
            title='Nivel Dificil', title_color='white' , relief=sg.RELIEF_SUNKEN, font=('Impact 24'),
            element_justification='center' , key='contenedor_dificil'), ],
        ]
    layout = [sg.Column(col,scrollable=True,background_color='#4f280a', vertical_scroll_only=True,size=(700,470))]
    return layout



def ayuda() :
    '''esta función  es la encargada de motrar la interfaz
    que brinda ayuda a los/as Jugadores/as. Da información de cómo se juega
    detalle información de ventanas y popUps que utiliza  la aplicación '''

    dirAyuda = os.path.join('media','ayuda','')

    tabGeneral = [general(dirAyuda)]
    tabJuego = [juego(dirAyuda)]
    tabReglas = [reglas()]
    tabNiveles = [niveles(dirAyuda)]
    tabIconCas = [iconCas(dirAyuda)]

    tabOtros = [otros(dirAyuda)]    # Agregar solapa o boton que te de un poco de info del proyecto, un link a Git y que diga que en el informe ocmpleto hay mas info



    layout = [[sg.TabGroup([[sg.Tab('General', tabGeneral,background_color='#4f280a',  key='pGeneral'),
                          sg.Tab('Instrucciones de Juego', tabJuego ,background_color='#4f280a',),
                          sg.Tab('Iconos y Casilleros', tabIconCas,background_color='#4f280a',),
                          sg.Tab('Reglas', tabReglas, background_color='#4f280a', element_justification='center'),
                          sg.Tab('Niveles', tabNiveles, background_color='#4f280a',element_justification='center' ),
                          sg.Tab('Más', tabOtros,background_color='#4f280a',)]],
                           font=('Arial', 14),
                          key='pestanas', title_color='red',
                          selected_title_color='white', tab_location='top',theme=mi_tema())],
              [sg.Button('Cerrar',button_color=('black','#f75404'), font=('Arial', 16),size=(20,10),key='cerrar')]]

    mi_tema()
    ventana = sg.Window('Ayuda', layout=layout,element_justification='center',grab_anywhere=True,no_titlebar=True,
                      keep_on_top=True,border_depth=5,background_color='#afad71',  size=(780,580)).Finalize()
    while True:

        eventos, valor = ventana.read()
        if eventos in (None, 'cerrar'):
            break
    ventana.close()






if __name__ == '__main__':
    ayuda()
    popReglas()
