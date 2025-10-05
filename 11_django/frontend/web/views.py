from django.shortcuts import render, redirect

# Create your views here.
import requests

API_URL = 'http://localhost:3000/productos' #BACKEND en Flask

def index(request):
    try:
        response = requests.get(API_URL)
        response.raise_for_status() #Si no es status 200 lanza excepción
        productos = response.json().get('productos')
    except Exception as e:
        print(e)
        productos = []
    finally:
        return render(request, 'index.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        categoria = request.POST.get('categoria')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
        vencimiento = request.POST.get('vencimiento')
    
        try:
            response = requests.post(API_URL,
                headers = {'Content-Type': 'application/json'},
                json = {
                    'nombre': nombre, 
                    'categoria': categoria, 
                    'descripcion':descripcion, 
                    'precio': int(precio), 
                    'stock': int(stock),
                    'vencimiento': vencimiento
                }
            )
            response.raise_for_status()
        except Exception as e:
            print(e)

    return redirect('index')


def actualizar_producto(request, id):
    #La petición realizada a 'actualizar_producto' es de tipo POST (Cuando se actualiza la información)
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        categoria = request.POST.get('categoria')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
        fecha = request.POST.get('vencimiento')

        try:
            response = requests.put(
                f'{API_URL}/{id}',
                headers={'Content-Type': 'application/json'},
                json = {
                    'nombre': nombre, 
                    'categoria': categoria, 
                    'descripcion':descripcion, 
                    'precio': int(precio), 
                    'stock': int(stock),
                    'vencimiento': fecha
                }
            )
            response.raise_for_status()
        except Exception as e:
            print(e)

        return redirect('index')

    #La petición realizada a 'actualizar_producto' es de tipo GET (Al cargar la página, para mostrar el formulario lleno)
    try:
        response = requests.get(f'{API_URL}/{id}')
        response.raise_for_status()
        producto = response.json()
    except Exception as e:
        return redirect('index')

    #Renderiza la página de actualizar la información del producto
    return render(request, 'actualizar.html', {'producto': producto})

def eliminar_producto(request, id):
    try:
        response = requests.delete(f'{API_URL}/{id}')
        response.raise_for_status()
    except Exception as e:
        print(e)

    return redirect('index')
