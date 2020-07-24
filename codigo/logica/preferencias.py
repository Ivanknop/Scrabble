class Preferencias():
    def __init__ (self, cant_filas=5, cant_columnas=5, especiales={}, nivel='', categorias=[]):
        self.__filas = cant_filas
        self.__columnas = cant_columnas
        self.__especiales = especiales
        self.__nivel = nivel
        self.__categorias_personalizadas = categorias

    def getFilas(self):
        return self.__filas

    def getColumnas(self):
        return self.__columnas

    def getEspeciales(self):
        return self.__especiales

    def getNivel(self):
        return self.__nivel
    
    def getCategoriasPersonalizadas(self):
        return self.__categorias_personalizadas
    
    def setCategoriasPersonalizadas(self, categorias):
        self.__categorias_personalizadas = categorias

    def setNivel(self, nivel):
        self.__nivel = nivel

    def setFilas(self, filas):
        self.__filas = filas

    def setColumnas(self, columnas):
        self.__columnas = columnas

    def setEspeciales(self, especiales):
        self.__especiales = especiales
