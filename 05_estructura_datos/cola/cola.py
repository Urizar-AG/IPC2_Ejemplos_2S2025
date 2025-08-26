import graphviz
from nodo import Node

class Queue:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    #Agregar un elemento en la cola, se agrega el nodo siempre al final de la lista
    def enqueue(self, value):
        new_node = Node(value)
        
        if self.__head is None: 
            self.__head = self.__tail = new_node
        else:
            self.__tail.next = new_node
            self.__tail = new_node
        
        self.__size += 1

    #Eliminar un elemento de la cola, se elimina siempre el primer nodo de la lista
    def dequeue(self):
        if self.__head is None:
            print('No hay elementos en la cola')
            return None
        else:
            tmp = self.__head
            self.__head = tmp.next
            tmp.next = None

            self.__size -= 1 
            
    def peek(self):
        return self.__head

    def is_empty(self):
        return self.__head is None
    
    def queue_size(self):
        return self.__size
    
    #Recorrer
    def print_queue(self):
        tmp = self.__head
        while tmp:
            print(tmp.get_data())
            tmp = tmp.next
    
    #Graficar
    def draw_queue(self, path):
        dot = graphviz.Digraph(format='svg', name='Cola')
        dot.attr(label='Cola', labelloc='t')
        dot.attr(rankdir='LR')
        dot.attr('node', shape='record')
        dot.attr('edge', arrowtail='dot', dir='both')

        aux = 1
        tmp = self.__head
        dot.node(str(aux), f'{{{tmp.get_data()}|}}')
        aux += 1
        tmp = tmp.next

        while tmp:
            dot.node(str(aux), f'{{{tmp.get_data()}|}}')
            dot.edge(str(aux - 1), str(aux))
            tmp = tmp.next
            aux += 1
        dot.render(path, view=True)
        