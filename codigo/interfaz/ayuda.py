import PySimpleGUI as sg
import os
from codigo.interfaz.tema import mi_tema

def general(dirAyuda):
    sg.theme_text_element_background_color('#4f280a')
    sg.theme_element_background_color('#4f280a')
    col = [[sg.Image(filename=f'{dirAyuda}ba.png'),sg.Text(' Muestra la Ayuda',font=('Arial, 18'),text_color='white')],
           [sg.Image(filename=f'{dirAyuda}bj.png'),sg.Text(' Comenzar a jugar',font=('Arial, 18'),text_color='white')],
           [sg.Image(filename=f'{dirAyuda}bp.png'), sg.Text('Muestra la Tabla de Puntajes', font=('Arial, 18'), text_color='white')],
           [sg.Image(filename=f'{dirAyuda}bnueva.png'), sg.Text('Iniciar una Nueva partida', font=('Arial, 18'), text_color='white')],
           [sg.Image(filename=f'{dirAyuda}bcargar.png'), sg.Text('Carga la ultima partida guardada. Si existe', font=('Arial, 18'), text_color='white')],
           [sg.Image(filename=f'{dirAyuda}bvolver.png'), sg.Text('Vuelve al Menu principal', font=('Arial, 18'), text_color='white')],
           [sg.Image(filename=f'{dirAyuda}nueva.png'), sg.Multiline(default_text=
                                                      'En esta ventana usted podrá configurar \nlos datos para'
                                                      'la nueva partida\n'
                                                      'el apodo debe tener entre 3 y 10 caractere, sin caracteres especiales\n'
                                                      'Debe indicar una dificultad (or defecto se inicia en modo Fácil)\n'
                                                      'al momento de precionar en Jugar se le mostrará un ventana de ocnfirmación\n'
                                                      'en todo momento usted podrá cancelar esta acción\n',
                                                        auto_size_text=True, font=('Arial, 14'), text_color='white', disabled=True, size=(30,10),background_color='#4f280a')],
    ]


    layout = [sg.Column(col,scrollable=True,background_color='#4f280a',vertical_scroll_only=True,size=(700,470))]


    return layout

def juego(dirAyuda):
    col = [
        [sg.Image(filename=f'{dirAyuda}tablero2.png'), sg.Multiline('Esta es la vista general del Tablero.\n A continuaci{on podr{a encontrar informaci{on detallada de c{omo se juega', font=('Arial, 18'), text_color='white', disabled=True, size=(25,10),background_color='#4f280a')],
        [sg.Image(filename=f'{dirAyuda}areasuperior.png')], [sg.Multiline('En el area superior se encunetra el indicador de Tiempo (1),\nel boton de Pausa y el de Ayuda\n'
                                                                     '\n1) TEMPORIZADOR: en tiempo JUGADo (indicado con números en el area negra)\n es el tiempo transcurrido según la configuración elegida.\n'
                                                                     'La barra de color naranja indica el tiempo RESTANTE. Esta se encoe a medida que pasa el tiempo.\n'
                                                                     '2) si usted cliquea el boton de pausa, la partida quda detenida y e muestra un menu con opciones que verá más abajo.\n'
                                                                     '\n3)luego e encunetra el simbolo de \"?\" el cual le muestra esta ayuda.\n ', font=('Arial, 18'), text_color='white' ,autoscroll=True, disabled=True, size=(40,8),background_color='#4f280a')],
        [sg.Image(filename=f'{dirAyuda}botonConfiguracion.png'),
         sg.Multiline('Sobre los Avatars de los jugadores, usted encontrara\n un boton que al precionarlo le '
                 'muestra la configuracion elegida para eta partida', font=('Arial, 18'), text_color='white',autoscroll=True, disabled=True, size=(30,6),background_color='#4f280a')],
        [sg.Image(filename=f'{dirAyuda}indicadorJugador.png'),
         sg.Multiline('A la derecha del tablero se encunetra el Avatar de cada jugador\n'
                 'debajo se encunetra el apodo elegido y los puntos acumulados en la partida. \n '
                 'Si su apodo esta de color verde, el juego indica  que es siu turno', font=('Arial, 18'), text_color='white',autoscroll=True, disabled=True, size=(30,8),background_color='#4f280a')],
        [sg.Image(filename=f'{dirAyuda}atril.png'),
         sg.Multiline('Debajo de los  avatares se encunetra el atril con sus fichas \n'
                  ' junto al boton de VALIDAR (simbolo check) y CAMBIAR FICHAS (bolsa)'
                 '\n  Cuando usted seleccione una ficha esta se pondra transparente como e indica en la imagen\n'
                  'en el area superior del atril podra visualizar la palabra.\n'
                  'Note que al seleccionar una ficha usted no puede preisonar la bola para cambiar las fichas.\n'
                 'Note que si deja el mouse sobre una ficha esta muestra una etiqueta con su puntaje.\n'
                 'Recuerde que el mismo tambien puede verse en el boton de Preferencias inidcado anteriormente.', font=('Arial, 18'), text_color='white',autoscroll=True, disabled=True, size=(20,8),background_color='#4f280a')],
        [sg.Image(filename=f'{dirAyuda}atrilValidado.png')],
         [sg.Multiline('Una vez que usted ya formo su palabra \n'
                  'debe dar click en el boton de validar y si todo es correcto'
                  'ScrabbleAR le indicará que seleccione donde insertar la palabra\n'
                  'en la pestaña de REGLAS podr{a consultar las reglas generales de ScrabbleAR'
                  'com ose ve en la imagen', font=('Arial, 18'), text_color='white',autoscroll=True, disabled=True, size=(40,8),background_color='#4f280a')],
        [sg.Image(filename=f'{dirAyuda}seleccionarlugar.png'), sg.Multiline('Cuando haga click en un casillero del tablero\n'
                                                                       'se muestra el indicador de orientacion. Una vez elegida\n'
                                                                       'la orientacion la palabra quedara insertada en el tablero.',
                                                            font=('Arial, 18'), text_color='white',autoscroll=True, disabled=True, size=(30,8),background_color='#4f280a')],
        [sg.Image(filename=f'{dirAyuda}palabracompu.png'), sg.Image(filename=f'{dirAyuda}palabraJugador.png'), ],
        [sg.Multiline('En el tablero las palbras con fondo Rojo son las insertadas por el oponente\n'
                 'Y las de fondo verde son sus palabras',

                                                            font=('Arial, 18'), text_color='white',autoscroll=True, disabled=True, size=(40,5),background_color='#4f280a')],
        [sg.Image(filename=f'{dirAyuda}bolsaFinalizar.png'), sg.Multiline('Si usted ve que el icono de la Bolsa de Fichas\n'
                                                                     'cambio y ahota dice FINALIZAR, puede que pasen dos cosas:\n'
                                                                     '- No hay mas fichas en la bolsa\n - No puedes cambiar mas fichas (maximo tres cambios) ',
                                                            font=('Arial, 18'), text_color='white',autoscroll=True, disabled=True, size=(20,10),background_color='#4f280a')],
        [sg.Image(filename=f'{dirAyuda}pausa.png'), sg.Image(filename=f'{dirAyuda}pantallaFinal.png'),sg.Image(filename=f'{dirAyuda}historialPalabras.png'),],
         [sg.Multiline('Aqui puede ver el menu de Pausa.\n'
                  'este le permite Retornar a la partida, Guardar la partida y Abandonar la partida\n'
                  'Luego puede ver la ventana de final de partida.\n'
                  'Esta muestra los puntos de cada jugador y el/la ganador/ora\n'
                  ' En este ventana si usted presiona el boton de Listado de palabras \n'
                  'podra ver las palabras que inserto cada jugador y los puntos que hizo con cada una'
                  ,font=('Arial, 18'), text_color='white',autoscroll=True, disabled=True, size=(40,8),background_color='#4f280a')],
        ]

    layout = [sg.Column(col,scrollable=True,background_color='#4f280a', vertical_scroll_only=True,size=(700,470))]

    return layout

def iconCas(dirAyuda):
    col = [
        [sg.Image(filename=f'{dirAyuda}orientacionG.png'), sg.Text('Casillero seleccionado para insertar palabra', font=('Arial, 18'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}orientacionDrerechaG.png'), sg.Text('insertar horizontalmente', font=('Arial, 18'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}orientacionAbajoG.png'),
         sg.Text('insertar verticalmente', font=('Arial, 18'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}sumaG.png'),
         sg.Text('Incrementa 5 puntos el valor total de la palabra', font=('Arial, 18'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}menosG.png'),
         sg.Text('Resta 5 puntos al valor total de la palabra', font=('Arial, 18'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}multGi.png'),
         sg.Text('Duplica el valor de la palabra', font=('Arial, 18'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}divG.png'),
         sg.Text('Divide a la mitad el valor de la palabra', font=('Arial, 18'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}ceroG.png'),
         sg.Text('Anula el valor de la palabra', font=('Arial, 18'), text_color='white')],

        ]

    layout = [sg.Column(col,scrollable=True,background_color='#4f280a', vertical_scroll_only=True,size=(700,470))]

    return layout

def otros(dirAyuda):
    col = [
        [sg.Image(filename=f'{dirAyuda}ba.png'), sg.Text(' Muestra la Ayuda', font=('Arial, 18'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}bj.png'), sg.Text(' Comenzar a jugar', font=('Arial, 18'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}bp.png'),
         sg.Text('Muestra la Tabla de Puntajes', font=('Arial, 18'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}bnueva.png'),
         sg.Text('Iniciar una Nueva partida', font=('Arial, 18'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}bcargar.png'),
         sg.Text('Carga la ultima partida guardada. Si existe', font=('Arial, 18'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}bvolver.png'),
         sg.Text('Vuelve al Menu principal', font=('Arial, 18'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}nueva.png'), sg.Text('',
                                                            font=('Arial, 18'), text_color='white')],
        ]

    layout = [sg.Column(col,scrollable=True,background_color='#4f280a', vertical_scroll_only=True,size=(700,470))]

    return layout

def reglas():
    imgReglas = os.path.join('media', 'ayuda', 'reglas.png')

    col = [[sg.Image(filename=imgReglas)],
           [sg.Multiline('¡¿Cómo te va?! Vamos a jugar al ScrabbleAR. Veamos bien cómo se juega...'
                         'Sí,   es   el   famoso   juego   de   mesa   donde   probarás   tu   conocimiento   acerca   de   las '
                         '  palabras\'realmente\' '
                         'existentes. Frente a tí tendrás al computador. ¿Serás capaz de derrotarlo?Lo primero que debes saber '
                         'es que las distintas dificultades afectan la inteligencia del ordenador.¿Inteligencia?   Dejémoslo   así '
                         '  por   el   momento.   Puedes   elegir   entre   FÁCIL,   MEDIO,  o   DIFÍCIL.Además   de   tener   un  '
                         ' adversario   más   complejo   de   enfrentar,   cambian   algunas   disposiciones   deljuego. Si quieres'
                         ' más detalles puedes ir a la sección específica en estas mismas reglas.Una vez elegida la dificultad se '
                         'abrirá el Tablero de juego y comenzará la verdadera prueba. Eneste juego tu tienes tres cosas para '
                         'hacer:•Escoger entre las fichas de tu atril la combinación que forme la mejor palabra posible (cadaletra posee '
                         'una puntuación propia, así que toda palabra tiene un puntaje) y, luego de eso,colocarla   en   la   mejor  '
                         ' posición   del   tablero.   Un   detalle,   antes   de   colocar   tu   palabra   en   eltablero deberás'
                         ' validar la palabra. No queremos tramposos.•Cambiar tus fichas por nuevas. ¡Ojo! Sólo dispones de 3 (tres) '
                         'cambios por partida.•Rendirte.... Bueno, esto mejor no.Presta mucha atención al tablero de juego. Encontrarás '
                         'casilleros especiales donde se sumaránpuntos o quizás multipliques el valor de la palabra... Pero '
                         'también hay otros que restan, dividen ohasta multiplican el valor total por CERO. Escoge con mucho '
                         'cuidado dónde colocarás tu palabra.Por suerte para tí esto también afecta al ordenador.Las   palabras  '
                         ' pueden   insertarse   en   vertical   u   horizonal.   En   este   juego   no   podrás   hacerlo   '
                         'endiagonal. Tampoco está permitido que se crucen las palabras entre sí. Calcula muy bien los '
                         'espaciosdisponibles.¿Cuándo termina la partida? Cuando no hay más fichas en algún atril y '
                         'tampoco en la bolsa defichas, cuando no hay espacios en el Tablero o cuando alguno de los dos '
                         'jugadores han agotado suscambios de fichas disponibles y aún así no tienen dónde jugar una nueva'
                         ' combinación de letras. Alfinalizar se comparan las puntuaciones y... ¡Tenemos un ganador!',
                         font=('Arial',18),text_color='white',size=(53,50),autoscroll=True, disabled=True,background_color='#4f280a')],

    ]
    layout = [sg.Column(col,scrollable=True,background_color='#4f280a',element_justification='center', vertical_scroll_only=True,size=(720,470))]
    return layout

def popReglas():
    layout = [reglas(),
              [sg.Button('Comenzar!',size=(20,5),key='comenzar')],]
    ventana = sg.Window('Reglas', layout=layout,element_justification='center', no_titlebar=True,grab_anywhere=True, keep_on_top=True).Finalize()

    while True:

        event, values = ventana.read()
        if event in ( None,'comenzar'):
            break
    ventana.close()


def niveles(dirAyuda):
    col = [[sg.Frame(
            layout=[[sg.Multiline(' Tamaño tablero: 20*20.     \n  '
                             'Puntaje de Fichas:  \n'
                             '\t Vocales y L, N, S, T, R = 5 pts; C, D, G = 2 pts; M, B, P = 8 pts; \n '
                             'F, H, V, Y = 4 pts; J = 6 pts; K, Ñ, Q, W, X = 9 pts; Z= 10 pts \n  '
                             '\tCantidad de fichas:   99  \n  '
                             '\t Duración de la   partida: 25 minutos    \n  '
                             '\t Tipo de casilleros  especiales: Suma y Resta   \n   '
                             '\tCantidad de Cambios   computador: 1\n'
                             '\tTipos de palabras  permitidas: sustantivos, adjetivos y verbos      \n'
                             '\t la PC: Busca la primer  palabra posible y \nla inserta en el primer lugar disponible en el   tablero.\n',
                             font=('Arial, 18'), text_color='black',autoscroll=True, disabled=True, size=(45,8),background_color='#afad71')]],

            title='Nivel Facil', title_color='white' , relief=sg.RELIEF_SUNKEN, font=('Impact 24'),
            element_justification='left',  key='contenedor_facil'),],
        [sg.Frame(
            layout=[[sg.Multiline(' Tamaño tablero 15*15. Idem anterior   \n '
                             '  Puntaje de Fichas:  Vocales y L, N, S, T, R = 1 pts; C, D, G = 2 pts; M, B,\n P = 3 pts; F, H, V, Y = 4 pts; J = 6 pts; K, Ñ, Q, W, X = 8 pts; Z= 10 pts       \n'
                             ' Cantidad de fichas: 95     \n    '
                             ' Duración de la partida: 20 minutos     \n    '
                             ' Tipo de casilleros especiales: Suma, resta, multiplica x 2, divide x2.      \n   '
                             ' Cantidad de Cambios computador: 1         \n'
                             ' Tipos de palabras   permitidas: sustantivos, adjetivos y verbos  \n       '
                             'PC: Evalúa la   primer palabra que puede formar y analiza en el tablero cuál es la mejor posición.\n',
                             font=('Arial, 18'), text_color='black',autoscroll=True, disabled=True, size=(45,8),background_color='#afad71')]],
            title='Nivel Medio', title_color='white' , relief=sg.RELIEF_SUNKEN, font=('Impact 24'),
            element_justification='center', key='contenedor_medio'), ],
        [sg.Frame(
            layout=[[sg.Multiline('Tamaño tablero: 10*10Idem anterior\n'
                             'Puntaje de Fichas: Vocales y L, N, S, T, R = 1 pts; C, D, G = 1 pts; \n'
                             'M, B, P = 3 pts; F, H, V, Y = 4 pts; J = 6 pts; K, Ñ, Q, W, X = 8 pts; Z= 10 pts\n'
                             'Cantidad de fichas: 95\n'
                             'Duración de la partida: 15 minutos\n'
                             'Tipo de casilleros especiales: Suma, resta, multiplica x 2, divide x2, multiplica palabra x 0\n'
                             'Cantidad de Cambios computador: 1\n'
                             'Tipos de palabras permitidas: adjetivos y verbos\n'
                             'PC: Prueba todas las palabras posibles y cuáles puede \ninsertar en las mejores posiciones a fin de encontrar la mejor combinación palabra-espacio.\n',
                             font=('Arial, 18'), text_color='black',autoscroll=True, disabled=True, size=(45,8),background_color='#afad71')]],
            title='Dificil', title_color='white' , relief=sg.RELIEF_SUNKEN, font=('Impact 24'),
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
                          sg.Tab('Reglas', tabReglas, background_color='#4f280a', ),
                          sg.Tab('Niveles', tabNiveles, background_color='#4f280a', ),
                          sg.Tab('Más', tabOtros,background_color='#4f280a',)]],
                           font=('Arial', 14),
                          key='pestanas', title_color='red',
                          selected_title_color='white', tab_location='top',theme=mi_tema())],
              [sg.Button('Cerrar',button_color=('black','#f75404'), font=('Arial', 16),size=(20,10),key='cerrar')]]

    mi_tema()
    ventana = sg.Window('Ayuda', layout=layout,element_justification='center',grab_anywhere=True,no_titlebar=True,
                        size=(780,580)).Finalize()
    while True:

        eventos, valor = ventana.read()
        if eventos in (None, 'cerrar'):
            break
    ventana.close()






if __name__ == '__main__':
    ayuda()
    popReglas()
