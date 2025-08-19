import os
from nodo import Nodo

class ListaCircular:
    def __init__(self):
        self.head = None

    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)
        if self.head is None:
            self.head = nuevo
            nuevo.next = self.head
        else:
            nuevo.next = self.head
            tmp = self.head
            while tmp.next != self.head:
                tmp = tmp.next
            tmp.next = nuevo
            self.head = nuevo

    def insertar_final(self, dato):
        nuevo = Nodo(dato)
        if self.head is None:
            self.head = nuevo
            nuevo.next = self.head
        else:
            tmp = self.head
            while tmp.next != self.head:
                tmp = tmp.next
            tmp.next = nuevo
            nuevo.next = self.head
    
    def buscar(self, value):
        tmp = self.head
        while tmp:
            if tmp.get_data() == value:
                return tmp
            tmp = tmp.next

            if tmp == self.head:
                break
        return None
    
    def eliminar(self, value):
        if self.head is None:
            return False
        elif self.head.get_data() == value:
            tmp = self.head
            self.head = tmp.next
            tmp.next = None
            return True
        else:
            prev = self.head
            tmp = self.head.next #Nodo a borrar
            while tmp:
                if tmp.get_data() == value:
                    prev.next = tmp.next
                    tmp.next = None
                    return True
                prev = tmp 
                tmp = tmp.next
            return False
        
    def mostrar_lista(self):
        tmp = self.head
        while tmp:
            print(tmp.get_data())
            tmp = tmp.next
            if tmp == self.head:
                break

    def graficar_lista(self, nombre_archivo):
        with open(f'{nombre_archivo}.dot', 'w') as file:
            file.write('digraph G {\n')
            file.write('\trankdir=LR;\n')
            file.write('\tlabel="Listado de estudiantes"\n')
            file.write('\tlabelloc = t;\n')
            file.write('\tnode [shape = box];\n')
            
            cnt = 0
            tmp = self.head
            while tmp:
                file.write(f'\tnode{cnt} [label="Carnet: {tmp.get_data()}"];\n')
                if tmp != self.head:
                    file.write(f'\tnode{cnt-1} -> node{cnt};\n')
                tmp = tmp.next
                if tmp == self.head:
                    break
                cnt += 1
            file.write(f'\tnode{cnt} -> node{0} [constraint=false];\n')
            file.write('}')
        os.system("dot -Tsvg "+ nombre_archivo +".dot -o "+ nombre_archivo +".svg")
