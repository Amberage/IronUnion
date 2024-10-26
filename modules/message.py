import requests

# Enviar mensaje
def sendMessage(api_key, chat_id, mensaje):
    url = f"https://api.telegram.org/bot{api_key}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': mensaje
    }
    
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("Mensaje enviado con éxito.")
        else:
            print(f"Error al enviar el mensaje. Código de estado: {response.status_code}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
