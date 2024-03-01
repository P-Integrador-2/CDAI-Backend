from json import loads

import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Función para enviar una imagen a la otra a AWS Rekognition y obtener la respuesta
def enviar_a_aws(imagen_bytes):
    url_api = ''
    respuesta = requests.post(url_api, data=imagen_bytes)
    return respuesta.json()


# Endpoint para recibir las tres imágenes y devolver el promedio de las respuestas
@app.route('/', methods=['POST'])
def procesar_imagenes():
    try:
        data = loads(request.data.decode().replace("'", '"'))
        print(data["image1"], type(data))
        """
        imagen1_bytes, imagen2_bytes, imagen3_bytes = data["image1"], data["image2"], data["image3"]
        
        respuestas = [enviar_a_aws(imagen1_bytes), enviar_a_aws(imagen2_bytes), enviar_a_aws(imagen3_bytes)]
    
        promedio_respuestas = sum(respuestas) / 3.0

        return jsonify({'promedio_respuestas': promedio_respuestas}), 200
"""
        return jsonify({'promedio_respuestas': 100}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
