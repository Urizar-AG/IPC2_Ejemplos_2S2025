from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_cors import CORS
import xml.etree.ElementTree as ET 
from clases.invernaderos import Invernaderos

app = Flask(__name__)
CORS(app)

invernaderos = Invernaderos()

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/invernaderos', methods=['GET'])
def mostrar_invernaderos():
    return render_template('invernaderos.html', lista_invernaderos=invernaderos)

@app.route('/cargar_archivo', methods=['POST'])
def cargar_archivo():
    file = request.files.get('file')
    if file:
        xml = file.read().decode('UTF-8')
        root = ET.fromstring(xml)
        cnt = 1
        for invernadero in root.find('listaInvernaderos').findall('invernadero'):
            invernaderos.agregar_invernadero(
                cnt, 
                invernadero.get('nombre'),
                int(invernadero.find('numeroHileras').text),
                int(invernadero.find('plantasXhilera').text)
            )
            cnt += 1
    return redirect(url_for('mostrar_invernaderos'))


####################################################################################################################

#http://host:port/api/invernadero/ver?id=#
@app.route('/api/invernaderos/ver')
def ver_invernadero():
    id_invernadero = int(request.args.get('id'))
    
    for invernadero in invernaderos:
        if invernadero.get_id() == id_invernadero:
            return jsonify({
                'id': invernadero.get_id(),
                'nombre': invernadero.get_nombre(),
                'filas': invernadero.get_filas(),
                'columnas': invernadero.get_columnas()
            }), 200

    return jsonify({'error': f'No existe un invernadero con ID={id_invernadero}'}), 400

@app.route('/api/invernaderos', methods=['GET', 'POST'])
def gestionar_invernaderos():
    if request.method == 'GET':
        listado_invernaderos = []
        for invernadero in invernaderos:
            listado_invernaderos.append({
                'id': invernadero.get_id(),
                'nombre': invernadero.get_nombre(),
                'filas': invernadero.get_filas(),
                'columnas': invernadero.get_columnas()
            })
        return jsonify({'invernaderos': listado_invernaderos}), 200

    data = request.get_json()
    invernaderos.agregar_invernadero(
        int(data['id']),
        data['nombre'],
        int(data['filas']),
        int(data['columnas'])
    )
    return jsonify({'msg': 'Invernadero registrado correctamente'}), 200

#<int:param>
#<float:param>
#<str:param> 
@app.route('/api/invernaderos/<int:id>', methods=['PUT'])
def actualizar_invernaderos(id):
    data = request.get_json()
    for invernadero in invernaderos:
        if invernadero.get_id() == id:
            invernadero.set_nombre(data.get('nombre'))
            invernadero.set_filas(int(data.get('filas')))
            invernadero.set_columnas(int(data.get('columnas')))

            return jsonify({'msg': 'Invernadero actualizado correctamente'}), 200
        
@app.route('/api/invernaderos/eliminar', methods=['DELETE'])
def eliminar_invernadero():
    id_invernadero = int(request.args.get('id'))
    
    eliminado = invernaderos.eliminar_invernadero(id_invernadero)
    if eliminado:
        return jsonify({'msg': 'Invernadero eliminado correctamente'}), 200
    return jsonify({'error': 'No existe un invernadero con ID{}'.format(id_invernadero)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,  debug=True)