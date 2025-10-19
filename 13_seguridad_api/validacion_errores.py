import requests
from jsonschema import validate, ValidationError

schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string", "minLength": 5},
        "email": {"type": "string", "format": "email"},
        "age": {"type": "integer", "minimum": 18}
    },
    "required": ["id", "name", "email"]
}

def api_segura(url, metodo, datos=None):
    try:
        if metodo == 'GET':
            res = requests.get(url, timeout=5)
        elif metodo == 'POST':
            res = requests.post(url, json=datos, timeout=5)

        res.raise_for_status()
        data = res.json()

        try:
            validate(data, schema=schema)
            print('Datos recibidos con éxito\n',data)
        except ValidationError as ve:
            print('Error: Esquema JSON incorrecto\n', ve.message)

    except requests.exceptions.Timeout:
        print('Error: La solicitud ha superado el tiempo de espera.')
    except requests.exceptions.ConnectionError:
        print('Error: No se pudo conectar al servidor')
    except requests.exceptions.RequestException:
        print('Error: Error en la solicitud')

if __name__ == '__main__':
    api_segura('https://jsonplaceholder.typicode.com/users/1', 'GET')

    datos = {
        "id": 10,
        "name": "Bob",
        "email": "correo@gmail.com",
        "age": 18
    }
    api_segura('https://jsonplaceholder.typicode.com/users', 'POST', datos)
