import graphviz
from nodo import Node

class Stack:
    def __init__(self):
        self.__top = None
        self.__size = 0

    #Agregrar un nodo al final de la pila
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.__top
        self.__top = new_node
        self.__size += 1 

    #Eliminar el primer nodo de la pila
    def pop(self):
        if self.__top is None:
            print('No hay elementos en la pila')
            return None
        else:
            value = self.__top.get_data()

            tmp = self.__top
            self.__top = tmp.next
            tmp.next = None
            self.__size -= 1 

            return value
        
    def peek(self):
        return self.__top

    def is_empty(self):
        return self.__top is None
    
    def stack_size(self):
        return self.__size

    #Recorrer la pila
    def print_stack(self):
        tmp = self.__top
        while tmp:
            print(tmp.get_data())
            tmp = tmp.next
    
    def draw_stack(self, path):
        dot = graphviz.Digraph(format='svg', name='Pila')
        dot.attr(label='Pila', labelloc='t')
        dot.attr(rankdir='TB')
        dot.attr('node', shape='record')
        dot.attr('edge', arrowtail='dot', dir='both')

        aux = 1
        tmp = self.__top
        dot.node(str(aux), f'{{{tmp.get_data()}|}}')
        aux += 1
        tmp = tmp.next

        while tmp:
            dot.node(str(aux), f'{{{tmp.get_data()}|}}')
            dot.edge(str(aux - 1), str(aux))
            tmp = tmp.next
            aux += 1
        dot.render(path, view=True)
