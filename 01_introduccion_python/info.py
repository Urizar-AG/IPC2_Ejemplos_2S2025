def saludar(nombre, edad):
    print(f'Soy {nombre} y tengo {edad} años')

if __name__ == '__main__':
    # --- Pedir información por consola ---
    print('Ingresa tú nombre')
    nombre = input()

    edad = int(input('Ingresa tú edad \n'))

    saludar(nombre, edad)

print('Este print está fuera del main desde el archivo "info"')
