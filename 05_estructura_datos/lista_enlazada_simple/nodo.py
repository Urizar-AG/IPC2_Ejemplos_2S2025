class Nodo:
    def __init__(self, id, nombre):
        #data
        self.__id = id
        self.__nombre = nombre
        #Apuntador
        self.next = None

    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def mostrar_informacion(self):
        print(f'Id: {self.__id}, Nombre: {self.__nombre}')
