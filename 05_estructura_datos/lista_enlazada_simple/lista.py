import os
from nodo import Nodo

class ListaSimple:
    def __init__(self):
        self.head = None

    def insertar_inicio(self, id, nombre):
        nuevo = Nodo(id, nombre)
        if self.head is None:
            self.head = nuevo
        else:
            nuevo.next = self.head
            self.head = nuevo

    def insertar_final(self, id, nombre):
        nuevo = Nodo(id, nombre)
        if self.head is None:
            self.head = nuevo
        else:
            tmp = self.head 
            while tmp.next is not None:
                tmp = tmp.next
            tmp.next = nuevo

    def buscar(self, id):
        tmp = self.head
        while tmp:
            if tmp.get_id() == id:
                return tmp
            tmp = tmp.next
        return None

    def eliminar(self, id):
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

    def mostrar_lista(self):
        tmp = self.head
        while tmp:
            tmp.mostrar_informacion()
            tmp = tmp.next

    def graficar_lista(self, nombre_archivo):
        with open(f'{nombre_archivo}.dot', 'w') as file:
            file.write('digraph G {\n')
            file.write('\trankdir=LR;\n')
            file.write('\tlabel="Listado de campos"\n')
            file.write('\tlabelloc = t')
            file.write('\tnode [shape = record];\n')
            
            cnt = 0
            tmp = self.head
            file.write(f'\tnode{cnt} [label="{{Id: {tmp.get_id()}|Nombre: {tmp.get_nombre()}}}"];\n')
            tmp = tmp.next
            cnt += 1
            while tmp:
                file.write(f'\tnode{cnt} [label="{{Id: {tmp.get_id()}|Nombre: {tmp.get_nombre()}}}"];\n')
                file.write(f'\tnode{cnt-1} -> node{cnt};\n') #Enlaza el nodo anterior con el nodo actual
                tmp = tmp.next
                cnt += 1
            file.write('}')
        os.system("dot -Tsvg "+ nombre_archivo +".dot -o "+ nombre_archivo +".svg")
        #Si se quiere en pdf
        #os.system("dot -Tpdf "+ archivo +".dot -o "+ archivo +".pdf")
