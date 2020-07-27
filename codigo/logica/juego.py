from codigo.logica.tablero import *
from codigo.logica.configuracion import *
from codigo.logica.preferencias import Preferencias
from codigo.logica.atril import Atril
from codigo.logica.bolsa_fichas import *
from codigo.interfaz.dibujar import Dibujar
import codigo.logica.check_palabra as cp
from codigo.logica.guardar_partida import Juego_Guardado
from codigo.logica.jugador import Jugador
from codigo.interfaz.interfaz_palabras import *
from codigo.interfaz.final import*
from codigo.interfaz.ayuda import ayuda
from codigo.interfaz.ayuda import popReglas
from codigo.interfaz import configuracion_personalizada
from codigo.logica import administrar_usuarios
import os.path
import time
import random

def determinar_dificultad(jugador):
    '''Retorna un diccionario que contiene toda la información necesaria
    para configurar la partida (puntajes de las fichas, cantidad de filas
    y columnas, coordenadas de casilleros especiales, etc.)'''
    dificultad = jugador.getDificultad()
    if (dificultad == 'facil'):
        configuracion = nivel_facil()
    elif (dificultad == 'medio'):
        configuracion = nivel_medio()
    elif (dificultad == 'dificil'):
        configuracion = nivel_dificil()
    else:
        configuracion = configuracion_personalizada.cargar_configuracion(jugador.getNombre())
    return configuracion

def lazo_principal(jugador, cargar_partida=True):
    '''Lazo que controla el flujo normal de la partida. Determina qué
    sucede ante cada evento que ocurre en el juego.
    :param jugador: Objeto que contiene los datos del jugador, lo
    utiliza al crear una nueva partida o cargar una anterior.
    :param cargar_partida: Booleano. Si es True, intentará cargar un archivo
    de partida.'''

    #Al inicio del módulo, se asume que no ocurrirá ningún error
    error = ''
    #Crea un string con el directorio donde se almacena la partida. El formato
    #de la ruta depende del sistema operativo en ejecución
    ruta_guardado = os.path.join('guardados', f'partida_{jugador.getNombre()}')
    #Crea el objeto que gestionará el guardado y cargado de la partida
    archivo_partida = Juego_Guardado(ruta_guardado)
    #Si se clickeó en "Cargar" en la interfaz principal...
    if (cargar_partida):
        #Carga una partida. Es True si se cargó con éxito, False en caso contrario
        if (archivo_partida.cargar_guardado()):
            #Al cargar una partida, la dificultad debe establecerse a partir del archivo
            jugador.setDificultad(archivo_partida.getDificultad())
            configuracion = determinar_dificultad(jugador)
            #Si ocurrió algún error durante la carga de la configuración, lo retorna
            if ('error' in configuracion) and (configuracion['error'] != ''):
                return configuracion['error']
            #Si se está jugando en modo personalizado, se guardan algunas características seleccionadas
            if (configuracion['nivel'] == 'personalizado'):
                preferencias = Preferencias(configuracion['filas'],configuracion['columnas'],configuracion['especiales'], configuracion['nivel'], configuracion['tipos_palabras'], configuracion['IA'])
            else:
                #Si no, se conserva sólo la información predeterminada
                preferencias = Preferencias(configuracion['filas'],configuracion['columnas'],configuracion['especiales'], configuracion['nivel'])
            #Prepara la información extraída del archivo
            jugador.setAvatar(archivo_partida.getAvatar())
            jugador.setNombre(archivo_partida.getJugadorUser())
            puntaje = archivo_partida.getPuntaje()
            jugador.setPuntaje(puntaje)
            unTablero = archivo_partida.getTablero()
            atril_jugador = archivo_partida.getAtril()
            atril_pc = archivo_partida.getAtrilPC()
            bolsa_fichas = archivo_partida.getBolsaFichas()
            preferencias = archivo_partida.getPreferencias()
            cant_cambiar = archivo_partida.getCantCambiar()
            puntaje_pc = archivo_partida.getPuntajePC()
            palabras_jugador = archivo_partida.getPalabrasJugador()
            palabras_pc = archivo_partida.getPalabrasPC()
            #La partida sólo se puede guardar en el turno del jugador. Al cargarla,
            #continuará siendo su turno
            turno_jugador = True
            #Construye la interfaz
            interfaz = Dibujar(unTablero, preferencias, atril_jugador, jugador)
            #Si se habían agotado las oportunidades para cambiar las fichas...
            if (cant_cambiar == 0):
                #... el botón permite finalizar el juego
                interfaz.habilitarFinalizacion()
            #Solicita el tiempo que faltaba para finalizar la partida, lo convierte a
            #segundos y lo envía al timer
            interfaz.setTimer(archivo_partida.getTiempoRestante() / 60)
            interfaz.actualizarPuntajePC(puntaje_pc)
            partida_existente = True
    else:
        #Como es una nueva partida, la dificultad fue seteada para el jugador en el menú principal
        configuracion = determinar_dificultad(jugador)
        puntaje = jugador.getPuntaje()
        if (configuracion['nivel'] == 'personalizado'):
            preferencias = Preferencias(configuracion['filas'],configuracion['columnas'],configuracion['especiales'], configuracion['nivel'], configuracion['tipos_palabras'], configuracion['IA'])
        else:
            preferencias = Preferencias(configuracion['filas'],configuracion['columnas'],configuracion['especiales'], configuracion['nivel'])
        unTablero = Tablero(preferencias)
        #Si no se clickeó "Cargar" en la interfaz inicial, crea una bolsa y nuevos atriles
        bolsa_fichas = crear_bolsa(configuracion['cant_fichas'],configuracion['puntaje_ficha'])
        atril_jugador = Atril(bolsa_fichas, 7)
        atril_pc = Atril(bolsa_fichas, 7)
        #El primer turno se decide al azar
        turno_jugador = random.choice([True, False])
        #Asigna la cantidad de veces que se pueden cambiar las fichas
        cant_cambiar = 3
        puntaje = 0
        puntaje_pc = 0
        interfaz = Dibujar(unTablero, preferencias, atril_jugador, jugador)
        #Muestra la pantalla con las reglas si es la primera vez que está jugando
        popReglas()
        #El tiempo de la partida se determina según el nivel de dificultad
        tiempo_partida = configuracion['tiempo']
        interfaz.setTimer(tiempo_partida)
        #Prepara los listados donde se guardarán las palabras utilizadas
        palabras_jugador=[]
        palabras_pc=[]
        partida_existente = False

    #Lazo principal del juego
    interfaz.turnoJugador(turno_jugador)
    jugar = True
    while jugar:

        #Turno del jugador
        if (turno_jugador):
            event, value = interfaz.leer()

            #Si se acabo el tiempo o se cerró la ventana, se termina el jueg
            if (event ==  None):
                break

            if (interfaz.terminoTimer()):
                terminar(jugador.getNombre(),puntaje,puntaje_pc,palabras_jugador,palabras_pc,jugador.getDificultad())
                break

            #-----EVENTO: Clickear en una ficha del atril-----
            if ('ficha' in event):
                #Se obtiene el índice de la ficha seleccionada a partir de la "key"
                #del botón y se agrega a una lista
                fichas_seleccionadas = []
                fichas_seleccionadas.append(int(event.split(" ")[1]))

                #En el siguiente string se irá formando la palabra
                palabra = ''
                #Le pide al atril la ficha que se corresponde con el botón que se clickeó
                palabra += list(atril_jugador.get_ficha(int(event.split(" ")[1])).keys())[0]

                #Muestra la palabra que se va formando e inhabilita la ficha clickeada y
                #el botón de cambiar. Luego, habilita el botón para deshacer
                interfaz.actualizarTexto(palabra)
                interfaz.inhabilitarElemento(event)
                interfaz.inhabilitarElemento('cambiar')
                interfaz.habilitarElemento('deshacer')
                #-----EVENTO: Clickear en otra ficha o en el botón "Validar"-----
                click_validar = False
                while (not click_validar):
                    event, value = interfaz.leer()

                    #Circunstancias que cierran el lazo}
                    if (event ==  None):
                        jugar = False
                        break


                    if (interfaz.terminoTimer()):
                        terminar(jugador.getNombre(),puntaje,puntaje_pc,palabras_jugador,palabras_pc,jugador.getDificultad())
                        jugar = False
                        break
                    if (event == 'validar'):
                        interfaz.inhabilitarElemento('deshacer')
                        click_validar = True

                    if ('ficha' in event):
                        #Cada vez que se clickea en una ficha, agrega el índice (la key) a
                        #"fichas_seleccionadas", inhabilita el botón correspondiente y
                        #añade la letra a la palabra
                        fichas_seleccionadas.append(int(event.split(" ")[1]))
                        interfaz.inhabilitarElemento(event)

                        palabra += list(atril_jugador.get_ficha(int(event.split()[1])).keys())[0]
                        #Muestra la palabra que se está formando en la interfaz
                        interfaz.actualizarTexto(palabra)

                    if (event == 'deshacer'):
                        #Quita la última letra de la palabra que se está formando                 
                        ficha_descartada = fichas_seleccionadas.pop()
                        #Habilita nuevamente la ficha
                        interfaz.habilitarElemento(f'ficha {ficha_descartada}')
                        #Actualiza la palabra
                        palabra = palabra[:-1]
                        interfaz.actualizarTexto(palabra)
                        #Si la palabra ya no tiene más letras, rompe el lazo y muestra el texto estándar.
                        if len(palabra) == 0:
                            interfaz.textoEstandar()
                            interfaz.inhabilitarElemento('deshacer')
                            #Como "click_validar" no se modifica, ignorará el resto de los eventos de validación.
                            break

                    #El timer debe actualizarse obligatoriamente dentro de cada evento
                    interfaz.actualizarTimer()
                    
                #Si clickeó validar (no se terminó el tiempo, se cerró la ventana ni se borró toda la palabra)...
                if (click_validar):
                    #Valida la palabra y, si existe, permite que se decida la posición en el tablero
                    if(cp.check_jugador(palabra, preferencias)):
                        interfaz.actualizarTexto('SELECCIONE DÓNDE INSERTAR', tamaño=12, color='green', fondo='white')

                        #-----EVENTO: Clickear en el tablero para elegir la posición-----
                        elegir_posicion = True
                        cambio_posicion = False
                        while elegir_posicion:
                            #La primera vez, se esperará que decida donde insertarla
                            if not (cambio_posicion):
                                event, value = interfaz.leer()
                            if (event == None):
                                jugar = False
                                break
                            if (interfaz.terminoTimer()):
                                terminar(jugador.getNombre(),puntaje,puntaje_pc,palabras_jugador,palabras_pc,jugador.getDificultad())
                                jugar = False
                                break

                            if 'tablero' in event:
                                #Muestra los botones de selección de orientación
                                interfaz.seleccionarOrientacion(event.split()[1], preferencias)

                                #Guarda la coordenada de ese botón según sus keys
                                fila = event.split(" ")[1].split(',')[0]
                                columna = event.split(" ")[1].split(',')[1]

                                #Calcula las coordenadas que estan debajo y a la derecha
                                #de la que escogió. Se utilizarán para decidir el sentido
                                coord_derecha = fila + ',' + str(int(columna) + 1)
                                coord_inferior = str(int(fila) + 1) + ',' + columna

                                #-----EVENTO: Decidir sentido-----
                                while True:
                                    event, value = interfaz.leer()
                                    if (event == None):
                                        jugar = False
                                        break
                                    if (interfaz.terminoTimer()):
                                        terminar(jugador.getNombre(),puntaje,puntaje_pc,palabras_jugador,palabras_pc,jugador.getDificultad())
                                        jugar = False
                                        break

                                    #Si seleccionó la coordenada que está a la derecha (insertar horizontal)
                                    #o la que está debajo (insertar vertical)...
                                    if (event == f'tablero {coord_derecha}') or (event == f'tablero {coord_inferior}'):

                                        #Las fichas se guardarán en esta lista
                                        lista_insercion = []
                                        for f in fichas_seleccionadas:
                                            #Usa la lista de índices para pedirle al atril las fichas necesarias
                                            lista_insercion.append(atril_jugador.get_ficha(f))

                                        #Le pide al tablero que intente agregarlas
                                        puntaje_palabra = unTablero.insertarPalabra(lista_insercion, (int(fila),int(columna)), 'h' if event == f'tablero {coord_derecha}' else 'v')

                                        #Si el tablero devuelve puntaje negativo, significa que no hubo espacio
                                        if puntaje_palabra == -1:
                                            interfaz.actualizarTexto('NO HAY ESPACIO', color='red', fondo='white', tamaño=12)
                                        else:
                                            #Las fichas se eliminan del atril en orden descendente, para evitar excepciones
                                            fichas_seleccionadas.sort(reverse=True)
                                            for f in fichas_seleccionadas:
                                                atril_jugador.usar_ficha(f)

                                            #Se completan los espacios vacios en el atril
                                            atril_jugador.llenar_atril(bolsa_fichas)

                                            #Se incremente el puntaje del jugador y actualizan en la interfaz
                                            puntaje += puntaje_palabra
                                            interfaz.actualizarPuntaje(puntaje)
                                            interfaz.textoEstandar()

                                            #Se guarda la palabra elegida por el jugador en la lista "palabras_jugador"
                                            palabras_jugador.append({palabra: puntaje_palabra})

                                            turno_jugador = False

                                        interfaz.actualizarAtril(atril_jugador)
                                        interfaz.actualizarTablero(unTablero)

                                        elegir_posicion = False
                                        break

                                    #Si se clickeó más allá de los botones de sentido, designa ese lugar como la nueva
                                    #ubicación para la palabra
                                    elif ('tablero' in event):
                                        cambio_posicion = True
                                        interfaz.reestablecerOrientacion(fila+','+columna, unTablero, preferencias)
                                        break
                                    interfaz.actualizarTimer()
                            interfaz.actualizarTimer()

                    #Si el módulo que resuelve la validez de la palabra devolvió False..
                    else:
                        interfaz.actualizarTexto('PALABRA NO VÁLIDA ¡PRUEBA DE NUEVO!', tamaño=10, color='red', fondo='white')
                        interfaz.actualizarAtril(atril_jugador)

                #Antes de continuar esperando eventos y habilitar los botones,
                #se comprueba que no se haya cerrado la ventana
                if (event != None):
                    interfaz.habilitarElemento('cambiar')

            #-----EVENTO: Botón para cambiar fichas-----
            if (event == 'cambiar'):
                if (cant_cambiar > 0):
                    cant_cambiar = cant_cambiar - 1
                    atril_jugador.cambiar_fichas(bolsa_fichas)
                    interfaz.actualizarAtril(atril_jugador)
                    #Si se alcanzó la cantidad máxima de cambios permitida, "cambiar"
                    #se convierte en "Finalizar juego"
                    if (cant_cambiar == 0):
                        interfaz.habilitarFinalizacion()
                    #Si el nivel no es fácil, termina el turno del jugador
                    if preferencias.getNivel() != 'facil':
                        turno_jugador = False
                else:
                    #Si se clickea "Finalizar juego", se termina la ronda
                    terminar(jugador.getNombre(),puntaje,puntaje_pc,palabras_jugador,palabras_pc,jugador.getDificultad())
                    jugar = False

            #-----EVENTO: Pausar juego-----
            if (event == 'pausar'):
                 #Se prepara para paralizar el timer
                instante = time.time()
                while True:
                    event = interfaz.ventanaPausa()
                    if (event == 'retomar') or (event == None):
                        break
                    if (event == 'abandonar'):
                        #Si abandonó la partida, muestra la lista completa de palabras usadas antes de salir
                        terminar(jugador.getNombre(),puntaje,puntaje_pc,palabras_jugador,palabras_pc,jugador.getDificultad())
                        jugar = False
                        break

                    #-----EVENTO: Guardar partida-----
                    if (event == 'guardar'):
                        eleccion = interfaz.popUpOkCancel('¿Estas seguro que deseas guardar la partida?')
                        if (eleccion == 'OK'):
                            jugador.setPuntaje(puntaje)
                            #Carga la lista de partidas guardadas
                            usuarios = administrar_usuarios.cargar_usuarios()
                            #Si el jugador no está en el listado, lo agrega y sobreescribe el archivo
                            if (jugador.getNombre() not in usuarios):
                                usuarios.append(jugador.getNombre())
                                administrar_usuarios.guardar_usuarios(usuarios)
                            #Como se va a guardar el tiempo restante real, se debe anular el tiempo perdido hasta este momento
                            instante = interfaz.paralizarTimer(instante)
                            archivo_partida = Juego_Guardado(ruta_guardado, unTablero, jugador.getNombre(), atril_jugador, atril_pc, bolsa_fichas, jugador.getPuntaje(), puntaje_pc, interfaz.getTiempoRestante(), preferencias, cant_cambiar, jugador.getAvatar(), palabras_jugador, palabras_pc, jugador.getDificultad())
                            archivo_partida.crear_guardado()
                            partida_existente = True
                            eleccion = interfaz.popUpOkCancel('¡Partida guardada con éxito!\n¿Volver al menú principal?')
                            if (eleccion == 'OK'):
                                jugar = False
                                break
                            
                #Cálcula el tiempo perdido durante el uso del menú de pausa
                interfaz.paralizarTimer(instante)

            #-----EVENTO: Información sobre la partida-----
            if (event == 'infoPartida'):
                instante =  time.time()
                infoConfiguracion(configuracion)
                interfaz.paralizarTimer(instante)
            if (event == 'ayuda'):
                instante = time.time()
                ayuda()
                interfaz.paralizarTimer(instante)
            interfaz.actualizarTimer()

        #Turno de la PC
        else:
            interfaz.turnoJugador(False)
            interfaz.leer()
            if (interfaz.terminoTimer()):
                terminar(jugador.getNombre(),puntaje,puntaje_pc,palabras_jugador,palabras_pc,jugador.getDificultad())
                break

            #Busca una palabra y un lugar en el tablero
            mejor_opcion, pal_pc = cp.check_compu(atril_pc, unTablero, preferencias)

            #Si encontró al menos una opcíón, la inserta y actualiza la información
            if len(mejor_opcion) != 0:
                #Guarda la palabra elegida por la IA en la lista "palabras_pc"
                palabras_pc.append({pal_pc: mejor_opcion['interes']})
                #Marca las fichas utilizadas como pertenecientes a la IA y las elimina de su atril
                for ficha in mejor_opcion['fichas']:
                    #Recordar que mejor_opcion['fichas'] podría contener diccionarios/fichas repetidas (en términos
                    #del lenguaje, con la misma referencia), por lo que al modificar una cambiaría su gemela. Por este
                    #motivo, no es conveniente alterar su contenido hasta acabado el proceso de búsqueda de indices en el atril.
                    indice = atril_pc.ver_atril().index(ficha)
                    atril_pc.usar_ficha(indice)
                for ficha in mejor_opcion['fichas']:
                    ficha['propietario'] = 'PC'
                #Realiza la inserción
                puntaje_pc += unTablero.insertarPalabra(mejor_opcion['fichas'], mejor_opcion['coordenada'], mejor_opcion['sentido'])
                atril_pc.llenar_atril(bolsa_fichas)
                interfaz.actualizarTablero(unTablero)
                interfaz.actualizarPuntajePC(puntaje_pc)
                interfaz.actualizarTexto(random.choice(['PC: ¡A ver cómo contrarrestas eso!', 'PC: ¿Te quedaste sin ideas?', 'PC: Podés hacerlo mejor...',
                                                            'PC: ¡Tu turno!', 'PC: He tenido retos más difíciles.', 'PC: El tiempo se acaba, amiguito.', 'PC: Jamás me han derrotado.',
                                                            'PC: Hoy estas con poca imaginación.', 'PC: Quizás deberías volver al buscaminas.', 'PC: Mis núcleos son más rápidos que tu cerebro.',
                                                            'PC: 100101110, que en binario es "perdedor."', 'PC: El código fuente no está de tu lado :(', 'PC: ¿Mala? ¿Yo?',
                                                            f'PC: Tu turno, {jugador.getNombre()}', 'PC: *bosteza*']), tamaño=12, color='#EBDEB6', fondo=random.choice(['#D10E49', '#12870D', '#80870D']), pc=True)
                #Si la bolsa de fichas se vació, advierte al jugador
                if len(bolsa_fichas) == 0:
                    interfaz.textoEstandar(pc=True)
                    interfaz.actualizarTexto('PC: La bolsa de fichas se vació', tamaño=14, color='#EBDEB6', fondo='#A9084F')
                    cant_cambiar = 0
                    interfaz.habilitarFinalizacion()
            interfaz.turnoJugador(True)
            turno_jugador = True

    #Si al terminar el programa no se guardó la partida y se está jugando en modo personalizado,
    #se borra el archivo con la configuración
    if (jugador.getDificultad() == 'personalizado') and (not partida_existente):
        configuracion_personalizada.eliminar_configuracion(jugador.getNombre())

    interfaz.cerrar()
    #Retorna un string que indica si ocurrió algún error durante la ejecución del módulo 
    return error