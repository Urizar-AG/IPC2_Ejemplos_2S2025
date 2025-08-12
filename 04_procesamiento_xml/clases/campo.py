class CampoAgricola:
    def __init__(self, id, nombre):
        self.__id = id
        self.__nombre = nombre
        self.estaciones = []

    def get_id(self):
        return self.__id
    
    def get_nombre(self):
        return self.__nombre

    def agregar_estacion(self, estacion):
        self.estaciones.append(estacion)
