from flask import Flask, request, jsonify
from flask_cors import CORS
from producto import Producto

app = Flask(__name__)
CORS(app)

productos = []

#Registrar un producto nuevo
@app.route('/productos', methods=['POST'])
def registrar_producto():
    data = request.get_json()
    precio = int(data.get('precio'))
    stock = int(data.get('stock'))
    if len(productos) > 0:
        #ID correlativo
        productos.append(Producto(
            productos[-1].get_id()+1, 
            data['nombre'], 
            data['categoria'], 
            data['descripcion'],
            precio, 
            stock,
            data['vencimiento']
        ))
    else:
        productos.append(Producto(
            1, 
            data['nombre'], 
            data['categoria'], 
            data['descripcion'],
            precio, 
            stock,
            data['vencimiento']
        ))
    
    return jsonify({'message': 'Producto registrado exitosamente'}), 200


#Obtener todos los productos
@app.route('/productos', methods=['GET'])
def obtener_productos():
    return jsonify({'productos': [producto.get_info() for producto in productos]}), 200


#Obtener un producto individual
@app.route('/productos/<int:id>', methods=['GET'])
def obtener_producto(id):
    for producto in productos:
        if producto.get_id() == id:
            return jsonify(producto.get_info()), 200
    return jsonify({'error': f'No existe un producto con ID: {id}'}), 400


#Actualizar un producto
@app.route('/productos/<int:id>', methods=['PUT'])
def actualizar_producto(id):
    data = request.get_json()

    for producto in productos:
        if producto.get_id() == id:
            producto.set_nombre(data.get('nombre'))
            producto.set_categoria(data.get('categoria'))
            producto.set_descripcion(data.get('descripcion'))
            producto.set_precio(data.get('precio'))
            producto.set_stock(data.get('stock'))
            producto.set_vencimiento(data.get('vencimiento'))
            return jsonify({'msg': 'Producto actualizado correctamente'}), 200
    return jsonify({'error': f'No existe un producto con ID: {id}'}), 400


#Eliminar un producto
@app.route('/productos/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
    posicion = 0
    #Itera hasta encontrar el producto a eliminar
    for producto in productos:
        if producto.get_id() == id:
            del productos[posicion]
            return jsonify({'msg': 'Producto eliminado correctamente'}), 200
        posicion += 1
    
    return jsonify({'error': f'No existe un producto con ID: {id}'}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000,  debug=True)
