class Invernadero:
    def __init__(self, id, nombre, filas, columnas):
        #data
        self.__id = id
        self.__nombre = nombre
        self.__filas = filas
        self.__columnas = columnas
        self.next = None

    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_filas(self):
        return self.__filas
    
    def set_filas(self, filas):
        self.__id = filas

    def get_columnas(self):
        return self.__columnas
    
    def set_columnas(self, columnas):
        self.__id = columnas
