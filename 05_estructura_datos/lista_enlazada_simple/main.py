from lista import ListaSimple

if __name__ == '__main__':
    campos = ListaSimple()

    print('---------- Insertando al final ----------')
    campos.insertar_final('01', 'Campo Agricola 01')
    campos.insertar_final('02', 'Campo Agricola 02')
    campos.mostrar_lista()
    print('')


    print('---------- Insertando al inicio ----------')
    campos.insertar_inicio('00', 'Campo Agricola 00')
    campos.mostrar_lista()
    print('')


    print('---------- Buscar nodo ----------')
    campo = campos.buscar('01')
    campo.mostrar_informacion()
    print('')


    campo2 = campos.buscar('03') #Este id no existe
    if campo2:
        campo2.mostrar_informacion()


    print('---------- Eliminar nodo ----------')
    campos.eliminar('00')
    campos.mostrar_lista()
    print('')


    print('---------- Graficar lista ----------')
    campos.graficar_lista('lista_campos_agricolas')
    