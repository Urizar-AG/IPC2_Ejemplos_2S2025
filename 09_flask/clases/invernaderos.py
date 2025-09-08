from .invernadero import Invernadero

class Invernaderos:
    def __init__(self):
        self.head = None

    def agregar_invernadero(self, id, nombre, filas, columnas):
        nuevo = Invernadero(id, nombre, filas, columnas)
        if self.head is None:
            self.head = nuevo
        else:
            tmp = self.head 
            while tmp.next is not None:
                tmp = tmp.next
            tmp.next = nuevo

    def buscar_invernadero(self, id):
        tmp = self.head
        while tmp:
            if tmp.get_id() == id:
                return tmp
            tmp = tmp.next
        return None

    def eliminar_invernadero(self, id):
        if self.head is None:
            return False
        elif self.head.get_id() == id:
            tmp = self.head
            self.head = tmp.next
            tmp.next = None
            return True
        else:
            prev = self.head
            tmp = self.head.next
            while tmp:
                if tmp.get_id() == id:
                    prev.next = tmp.next
                    tmp.next = None
                    return True
                prev = tmp 
                tmp = tmp.next
            return False

    def esta_vacia(self):
        return self.head is None
    
    #Hace la lista iterable
    def __iter__(self):
        tmp = self.head
        while tmp:
            yield tmp
            tmp = tmp.next
