from codigo.interfaz import interfaz_inicial
from codigo.logica import juego
from codigo.interfaz.check_imagenes import*
import PySimpleGUI as sg

def main():
    '''Primero ejecuta contról de imagenes; si alguna imagen está dañada
    la modifica por una genérica, así la aplicación no colapsa.
    Luego inicia la interfaza principal y, si se ingresaron datos
    para el jugador, inicia el juego. Respectivamente, si la primera
    retorna un jugador vacío (por ejemplo, si se cierra la ventana sin
    hacer nada), la segunda parte no se ejecuta.'''
    loading()
    while True:
        datos_jugador, cargar = interfaz_inicial.lazo_principal()
        if (datos_jugador.getNombre() != ''):
            error = juego.lazo_principal(datos_jugador, cargar)
            if (error != ''):
                sg.popup(error, keep_on_top=True, background_color='#ece6eb',text_color='black', button_color=('black','#f75404'),font=('Arial',14), no_titlebar=True)
        else:
            break

if __name__ == '__main__':
    main()
