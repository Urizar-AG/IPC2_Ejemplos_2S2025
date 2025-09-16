import re

#1.BUSCAR UNA PALABRA ESPECÍFICA

#Primera coincidencia
patron = r'hola'
texto = 'hola estudiantes, hola mundo'
if resultado := re.search(patron, texto):
    print(resultado.group())
else:
    print('No se encontaron coincidencias')

#Todas la coincidencias
patron = r'Python'
texto = 'Python es un lenguaje interpretado, Python fue lanzado en 1991, python es el lenguaje utilizado en IPC2.'
coincidencias = re.findall(patron, texto, re.IGNORECASE)
print('Coincidencias encontradas:', coincidencias)


#2.EMPIEZA O TERMINA CON UNA PALABRA ESPECÍFICA

#Empieza con la palabra
patron = r'^hola'
texto = 'hola estudiantes, hola mundo'
if re.search(patron, texto):
    print('La cadena empieza con "hola"')
else:
    print('La cadena no empieza con "hola"')

#Termina con la palabra
patron = r'mundo$'
if re.search(patron, texto):
    print('La cadena termina con "mundo"')
else:
    print('La cadena no termina con "mundo"')


#3.REEMPLAZAR COINCIDENCIAS
patron = r'mundo'
texto = 'Hola mundo, mundo, mundo!'
print('Cadena antes de la sustitución:', texto)
texto_nuevo = re.sub(patron, 'Python', texto)
print('Cadena después de la sustitución:', texto_nuevo)


### CASOS CON EXPRESIONES REGULARES ###

#Extraer fechas
texto = 'Guatemala, 16/09/2025, Ciudad de Guatemala'
fecha = re.search(r'\d{2}/\d{2}/\d{4}', texto)
print(f'Coincidencia: {fecha}; Fecha:{fecha.group()}')

#Correo electrónico
patron = r'\w+@(\w+)\.(\w+)'
correo = 'correo@example.com'
resultado = re.search(patron, correo)
if resultado:
    nombre = resultado.group(1)
    dominio = resultado.group(2)
    print(f'Nombre: {nombre}; Dominio: {dominio}')
else:
    print('No es un correo válido')

#Números
# [+-]?\d+(\.\d+)?
patron = r'([+-]?\d+(?:\.\d+)?)'
texto = '+10, -10, +10.50, -10.50, 10, aaa'
coincidencias = re.findall(patron, texto)
print('Coincidencias encontradas:', coincidencias)
