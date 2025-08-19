class Nodo:
    def __init__(self, data):
        self.__data = data
        self.prev = None
        self.next = None

    def get_data(self):
        return self.__data
    
    def set_id(self, data):
        self.__data = data

    def mostrar_informacion(self):
        print(f'Frecuencia: {self.__data}')
