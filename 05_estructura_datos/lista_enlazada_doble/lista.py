import os
from nodo import Nodo

class ListaDoble:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertar_inicio(self, data):
        nuevo = Nodo(data)
        if self.head is None:
            self.head = self.tail = nuevo
        else:
            nuevo.next = self.head
            self.head.prev = nuevo
            self.head = nuevo

    def insertar_final(self, data):
        nuevo = Nodo(data)
        if self.head is None:
            self.head = self.tail = nuevo
        else:
            nuevo.prev = self.tail
            self.tail.next = nuevo
            self.tail = nuevo

    def buscar(self, value):
        tmp = self.head
        while tmp:
            if tmp.get_data() == value:
                return tmp
            tmp = tmp.next
        return None
    
    def buscar_reverso(self, value):
        tmp = self.tail
        while tmp:
            if tmp.get_data() == value:
                return tmp
            tmp = tmp.prev
        return None
    
    def eliminar(self, value):
        if self.head is None:
            return False
        
        tmp = self.head
        while tmp:
            if tmp.get_data() == value:
                if tmp == self.head:
                    self.head = tmp.next
                    tmp.next = None
                    self.head.prev = None
                    return True
                elif tmp == self.tail:
                    self.tail = tmp.prev
                    tmp.prev = None
                    self.tail.prev = None
                    return True
                else:
                    tmp.prev.next = tmp.next
                    tmp.next.prev = tmp.prev
                    tmp.next = None
                    tmp.prev = None
                    return True
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
            file.write('\tlabel="Listado de frecuencias"\n')
            file.write('\tlabelloc = t\n')
            file.write('\tnode [shape = box];\n')
            
            cnt = 0
            tmp = self.head
            file.write(f'\tnode{cnt} [label="Frecuencia: {tmp.get_data()}"];\n')
            cnt += 1
            tmp = tmp.next
            while tmp:
                file.write(f'\tnode{cnt} [label="Frecuencia: {tmp.get_data()}"];\n')
                file.write(f'\tnode{cnt-1} -> node{cnt};\n')
                file.write(f'\tnode{cnt} -> node{cnt-1};\n')
                tmp = tmp.next
                cnt += 1
            
            file.write('}')

        os.system("dot -Tsvg "+ nombre_archivo +".dot -o "+ nombre_archivo +".svg")
        #Si se quiere en pdf
        #os.system("dot -Tpdf "+ archivo +".dot -o "+ archivo +".pdf")

    #Representar la lista enlazada como una tabla
    def graficar_matriz(self, nombre_archivo, filas, columnas):
        with open(f'{nombre_archivo}.dot', 'w') as file:
            file.write('digraph G {\n')
            file.write('\tlabel="Listado frecuencias"\n')
            file.write('\tlabelloc=t;\n')
            file.write('\tnode [shape=plaintext]\n')

            #Creación del nodo
            file.write('\tnode0 [label=<\n') 
            file.write('\t\t<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="10">\n')

            #Fila encabezado para los números de columna
            file.write('\t\t\t<TR>\n')
            file.write('\t\t\t\t<TD BORDER="0"></TD>\n')
            for j in range(1, columnas+1):
                file.write(f'\t\t\t\t<TD BORDER="0">{j}</TD>\n') #Número de columna
            file.write('\t\t\t</TR>\n')

            #Agregando los valores por filas
            tmp = self.head
            for i in range(1, filas+1):
                file.write('\t\t\t<TR>\n')
                file.write(f'\t\t\t\t<TD BORDER="0"  CELLPADDING="15">{i}</TD>\n') #Número de fila
                #Contenido de la celda
                for j in range(columnas):
                    file.write(f'\t\t\t\t<TD>{tmp.get_data()}</TD>\n') #Contenido de la celda
                    tmp = tmp.next
                file.write('\t\t\t</TR>\n')

            file.write('\t\t</TABLE>>];\n')
            file.write('}')

        os.system("dot -Tsvg "+ nombre_archivo +".dot -o "+ nombre_archivo +".svg")
