import xml_elementtree as xmlet 
import xml_minidom as xmldom

def menu():
    print("+------------------------------------+")
    print("|             MENÚ PRINCIPAL         |")
    print("+------------------------------------+")
    print("|1. Limpiar sistema                  |")
    print("|2. Cargar archivo con ElementTree   |")
    print("|3. Cargar archivo con Minidom       |")
    print("|4. Mostrar campos agricolas         |")
    print("|5. Escribir archivo con ElementTree |")
    print("|6. Escribir archivo con Minidom     |")
    print("|7. Salir                            |")
    print("+------------------------------------+")

    opcion = int(input('Ingresa una opción: '))
    return opcion

if __name__ == "__main__":

    campos_agricolas = []

    while True:
        opc = menu()
        if opc == 1:
            campos_agricolas = []
        elif opc == 2: 
            ruta = input('Ingresa la ruta origen del archivo: ') 
            nombre_archivo = input('Ingresa el nombre del archivo: ')
            xmlet.leer_archivo(ruta + nombre_archivo, campos_agricolas)
            print('')
        elif opc == 3:
            ruta = input('Ingresa la ruta origen del archivo: ') 
            nombre_archivo = input('Ingresa el nombre del archivo: ')
            xmldom.leer_inventario(ruta + nombre_archivo, campos_agricolas)
            print('')
        elif opc == 4:
            for campo in campos_agricolas:
                print('====================================')
                print(campo.get_nombre())
                print('====================================')
                for estacion in campo.estaciones:
                    print(estacion.get_nombre())   
                print('')
        elif opc == 5:
            ruta = input('Ingresa la ruta destino del archivo: ') 
            nombre_archivo = input('Ingresa el nombre del archivo: ')
            xmlet.escribir_archivo(ruta + nombre_archivo, campos_agricolas)
            print('')
        elif opc == 6:
            ruta = input('Ingresa la ruta destino del archivo: ') 
            nombre_archivo = input('Ingresa el nombre del archivo: ')
            xmldom.escribir_inventario(ruta + nombre_archivo, campos_agricolas)
            print('')
        elif opc == 7:
            print('Programa finalizado')
            break
        else:
            print('Opción no válida\n')
