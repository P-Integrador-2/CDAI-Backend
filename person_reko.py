import boto3


def contar_personas(imagen_path, perfil_aws='RekognitionFullAccess_user'):
    rekognition_client = boto3.Session(profile_name=perfil_aws).client('rekognition')

    with open(imagen_path, 'rb') as imagen_archivo:
        imagen_binaria = imagen_archivo.read()

    try:
        response = rekognition_client.detect_faces(
            Image={'Bytes': imagen_binaria},
            Attributes=['ALL']
        )

        numero_personas = len(response['FaceDetails'])
        return numero_personas

    except Exception as e:
        print(f"Error al analizar la imagen: {e}")
        return 0


ruta_imagen = 'p1.jpg'
cantidad_personas = contar_personas(ruta_imagen)
# print(cantidad_personas)
