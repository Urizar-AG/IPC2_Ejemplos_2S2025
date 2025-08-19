from lista import ListaDoble


if __name__ == '__main__':
    frecuencias = ListaDoble()
    frecuencias.insertar_final(300)
    frecuencias.mostrar_lista()
    print('----------------------------------')

    frecuencias.insertar_inicio(200)
    frecuencias.mostrar_lista()
    print('----------------------------------')

    frecuencias.insertar_final(0)
    frecuencias.mostrar_lista()
    print('----------------------------------')

    frecuencias.insertar_final(0)
    frecuencias.insertar_final(0)
    frecuencias.insertar_final(6000)
    frecuencias.insertar_final(500)
    frecuencias.insertar_final(8000)
    frecuencias.insertar_final(0)
    frecuencias.insertar_final(1500)
    frecuencias.insertar_final(0)
    frecuencias.insertar_final(1500)
    frecuencias.insertar_final(0)
    frecuencias.insertar_final(0)
    frecuencias.insertar_final(2000)

    frecuencias.graficar_lista('./lista_frecuencias')
    frecuencias.graficar_matriz('matriz_frecuencias', 5, 3)