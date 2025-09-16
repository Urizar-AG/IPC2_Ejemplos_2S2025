#MANEJO DE LISTAS NATIVAS DE Python

#1.CREAR UNA LISTA NUEVA

#Lista vacía
numeros = []

#Lista con el constructor
vocales = list()

#2.AÑADIR ELEMENTOS A LA LISTA
numeros.append(1)
numeros.append(2)
numeros.append(3)
numeros.append(4)
numeros.append(5)
numeros.insert(0,9)
print(numeros)

#3.ACCEDER A LOS ELEMENTOS DE LA LISTA

#índice positivo
print(numeros[0])

#índice negativo
print(numeros[-1])

#Slice
print(numeros[2:])
print(numeros[:4])
print(numeros[0:2])
print(numeros[:])

#4.MODIFICAR ELEMENTOS DE LA LISTA
numeros[-1]=0
print(numeros)

#5.MÉTODOS DE LA LISTA

#Ordenar
numeros.sort()
print(numeros)

#Revertir
numeros.reverse()
print(numeros)

#Copiar
vocales = numeros.copy()
print(vocales)

#Vaciar
vocales.clear()
print(vocales)
vocales.append('a')
vocales.append('e')
vocales.append('i')
vocales.append('o')
vocales.append('u')
vocales.append('X')
vocales.append('Y')

#Eliminar elementos
print(vocales)
vocales.remove('X')
letra = vocales.pop(-1)
print(letra)
print(vocales)

#Extender una lista
numeros.extend(vocales)
print(numeros)

#6.RECORRER UNA LISTA
for elemento in numeros:
    print(elemento)
