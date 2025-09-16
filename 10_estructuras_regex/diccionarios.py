### MANEJO DE DICCIONARIOS ###

#1.CREAR UN DICCIONARIO

#Diccionario vacío
estudiantes = {}

#Diccionario con el constructor
diccionario = dict()

#2.AÑADIR ELEMENTOS CLAVE-VALOR
estudiantes[1] = 'Estudiante Uno'
estudiantes[2] = 'Estudiante Dos'
estudiantes[3] = 'Estudiante Tres'
estudiantes.update({4: 'Estudiante Cuatro'})
print(estudiantes)

#3.ACCEDER A LOS DATOS DEL DICCIONARIO
print(estudiantes[2])
print(estudiantes.get(1))
print('Las llaves son: ', estudiantes.keys())
print('Los valores son: ', estudiantes.values())
print('Los items son: ', estudiantes.items())

#4.ELIMINAR ELEMENTOS CLAVE-VALOR

#Basado en una clave
estudiantes.pop(1)
print(estudiantes)

#Eliminar el último elemento
print(estudiantes.popitem())

#5.RECORRER UN DICCIONARIO

#Iterar sobre las claves
for estudiante in estudiantes:
    print(estudiante)

#Iterar sobre los valores
for estudiante in estudiantes.values():
    print(estudiante)

#Iterar sobre los items
for clave, valor in estudiantes.items():
    print('Clave:', clave,'|', 'Valor:', valor)
