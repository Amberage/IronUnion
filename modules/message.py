import requests
from . import configHandler as config

# Enviar mensaje
def sendMessage(mensaje = "Error: Se esperaba un mensaje, revise el comando usado para enviar mensajes.\n\n *.exe -m <mensaje>"):
    configPaths = config.getConfigPath()
    CONFIG_FILE = configPaths[2]

    configValues = config.getConfigValues(CONFIG_FILE)
    config_api_key = configValues[0]
    config_chat_id = configValues[1]

    url = f"https://api.telegram.org/bot{config_api_key}/sendMessage"
    payload = {
        'chat_id': config_chat_id,
        'text': mensaje
    }
    
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("Mensaje enviado con éxito.")
        else:
            print(url, payload, CONFIG_FILE, configValues)
            print(f"Error al enviar el mensaje. Código de estado: {response.status_code}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
