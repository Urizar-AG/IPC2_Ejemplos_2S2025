class Node:
    def __init__(self, data):
        self.__data = data
        self.next = None

    def get_data(self):
        return self.__data
    
    def set_data(self, data):
        self.__data = data
    