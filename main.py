from json import loads

from flask import Flask, request, jsonify
from flask_cors import CORS
from person_reko import contar_personas
from PIL import Image
import io

app = Flask(__name__)
CORS(app)


# Endpoint para recibir las tres imágenes y devolver el promedio de las respuestas
@app.route('/', methods=['POST', "post", 'OPTIONS'])
def procesar_imagenes():
    try:
        respuestas = []
        for i in range(1, 4):
            blob = request.files.get(f'imagen{i}')
            imagen_bytes = blob.read()
            respuestas.append(contar_personas(imagen_bytes))

        # print(imagenes_bytes)
        # respuestas = [contar_personas(imagen_bytes) for imagen_bytes in imagenes_bytes.values()]
        # promedio_respuestas = sum(respuestas) / 3.0

        return jsonify({'promedio_respuestas': 100}), 200
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
