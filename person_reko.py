import boto3

region = "us-east-1"


def contar_personas(imagen_binaria, perfil_aws='RekognitionFullAccess_user'):
    rekognition_client = boto3.Session(profile_name=perfil_aws, region_name=region).client('rekognition')

    try:
        response = rekognition_client.detect_faces(
            Image={'Bytes': imagen_binaria},
            Attributes=['ALL']
        )

        numero_personas = len(response['FaceDetails'])
        return numero_personas

    except Exception as e:
        return f"Error al analizar la imagen: {e}"

# ruta_imagen = 'p1.jpg'
# cantidad_personas = contar_personas(ruta_imagen)
# print(cantidad_personas)
