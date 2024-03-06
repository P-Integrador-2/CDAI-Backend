from json import loads

import requests
from flask import Flask, request, jsonify
from person_reko import contar_personas

app = Flask(__name__)

# Endpoint para recibir las tres imágenes y devolver el promedio de las respuestas
@app.route('/', methods=['POST'])
def procesar_imagenes():
    try:
        data = loads(request.data.decode().replace("'", '"'))


        imagen1_bytes, imagen2_bytes, imagen3_bytes = data["image1"], data["image2"], data["image3"]
        
        respuestas = [contar_personas(imagen1_bytes), contar_personas(imagen2_bytes), contar_personas(imagen3_bytes)]
    
        promedio_respuestas = sum(respuestas) / 3.0

        return jsonify({'promedio_respuestas': promedio_respuestas}), 200
    except Exception as e:
        return jsonify({str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
