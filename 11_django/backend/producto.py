class Producto:
    def __init__(self, id, nombre, categoria, descripcion, precio, stock, vencimiento):
        self.__id = id
        self.__nombre = nombre
        self.__categoria = categoria
        self.__descripcion = descripcion
        self.__precio = precio
        self.__stock = stock
        self.__vencimiento = vencimiento

    def get_id(self):
        return self.__id
    
    def get_info(self):
        return {
            'id': self.__id,
            'nombre': self.__nombre,
            'categoria': self.__categoria,
            'descripcion': self.__descripcion,
            'precio': self.__precio,
            'stock': self.__stock,
            'vencimiento': self.__vencimiento
        }
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_categoria(self, categoria):
        self.__categoria = categoria

    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion

    def set_precio(self, precio):
        self.__precio = precio

    def set_stock(self, stock):
        self.__stock = stock

    def set_vencimiento(self, vencimiento):
        self.__vencimiento = vencimiento
