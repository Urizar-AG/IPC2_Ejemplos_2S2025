#MANEJO DE FICHEROS

#1.LEER UN ARCHIVO
with open('entrada.txt', 'r', encoding='UTF-8') as archivo:
    #Leer todo el contenido
    # contenido = archivo.read()
    # print(contenido)

    #Obtener el contenido por lineas
    # contenido = archivo.readlines()
    # print(contenido)

    #Leer línea por línea
    cnt = 1
    for linea in archivo:
        print(f'Línea {cnt}: {linea}')
        cnt += 1

#2.ESCRIBIR UN ARCHIVO
with open('salida.txt', 'w', encoding='UTF-8') as archivo:
    contenido = 'Hola estudiantes,'
    archivo.write(contenido)

#3.LEER Y ESCRIBIR UN ARCHIVO
with open('salida.txt', 'r+', encoding='UTF-8') as archivo:
    contenido = archivo.read()
    print('Contenido actual:', contenido)

    contenido_nuevo = '\nSí sale IPC2!!! No la tiren :)'
    archivo.write(contenido + contenido_nuevo)
