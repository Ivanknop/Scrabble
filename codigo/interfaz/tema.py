import PySimpleGUI as sg

def mi_tema():
    '''
    Configuración genérica del diseño de las interfaces que facilita el diseño. 
    Después se adapta a la especificidad de cada pestaña.
    '''
    sg.LOOK_AND_FEEL_TABLE['scrabble'] = {'BACKGROUND': '#4f280a', ##133d51',
                                            'TEXT': '#fff4c9',
                                            'INPUT': '#c7e78b',
                                            'TEXT_INPUT': '#000000',
                                            'SCROLL': '#c7e78b',
                                            'BUTTON': ('black', '#4f280a'),
                                            'PROGRESS': ('#01826B', '#D0D0D0'),
                                            'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                            }
    sg.theme('scrabble')




def aviso(mensaje = 'Este es un mensaje estandar',botones = ['entendido']):

    '''Esta funcion se encarga de generar un PopUp personalizao
    recibe ods parametros
    :mensaje : es la informacion que se imprimira en la ventana
    :botones: una lista con las etiqueteas para los botones en formato string su KEY esta formada por un '_' y el nombre pasado por parametro

    la funcion retorna el evento (boton cliceado) '''
    layout = [[sg.Text(mensaje,font=('Arial', 12),text_color='black',background_color='white')],]

    botonLIs = []
    for b in botones:
        botonLIs.extend([sg.Button(button_text=b, border_width=1, button_color=('black', '#f75404'), key=f'_{b}')])

    layout.append(botonLIs)
    popup = sg.Window('AVISO',layout, background_color='white', no_titlebar=True, keep_on_top=True,grab_anywhere=True).Finalize()


    while True:
        evento, valor = popup.read()
        if evento:
            break

    popup.Close()
    return evento



if __name__ == '__main__':
   evento =  aviso('Hola mundo' , ['Salir', 'OK', 'Jugar'])
   print(evento)