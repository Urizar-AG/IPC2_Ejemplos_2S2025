class Nodo:
    def __init__(self, data):
        self.__data = data
        self.next = None

    def get_data(self):
        return self.__data
    