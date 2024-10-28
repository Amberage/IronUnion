import os, tempfile, configparser

TEMP_NAME_DIRECTORY = '.TelegramBot'
TELEGRAM_TEMP_DIRECTORY = os.path.join(tempfile.gettempdir(), TEMP_NAME_DIRECTORY)
CONFIG_FILE = TELEGRAM_TEMP_DIRECTORY + '\\config.cfg'

def setConfigValues(token_api, token_chat):
    # Lectura del archivo de configuración.
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)

    # Escritura de valores.
    config.set('Telegram', 'TELEGRAM_API_KEY', token_api)
    config.set('Telegram', 'TELEGRAM_CHAT_ID', token_chat)

    # Guardar los cambios en el archivo de configuración
    with open(CONFIG_FILE, 'w') as configurationFile:
        config.write(configurationFile)

def getConfigValues():
    '''
    return array with config.cfg information

    * array[0] = TELEGRAM_API_KEY
    * array[1] = TELEGRAM_CHAT_ID
    '''
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)

    config_api_key = config.get('Telegram', 'TELEGRAM_API_KEY')
    config_chat_id = config.get('Telegram', 'TELEGRAM_CHAT_ID')
    return [config_api_key, config_chat_id]