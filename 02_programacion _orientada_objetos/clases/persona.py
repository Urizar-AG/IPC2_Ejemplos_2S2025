from abc import ABC, abstractmethod

class Persona(ABC):
    
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad
    
    def set_edad(self, edad):
        self.__edad = edad

    @abstractmethod
    def saludar(self):
        pass

    def describir(self):
        pass
