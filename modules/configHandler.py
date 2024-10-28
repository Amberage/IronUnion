import configparser, os, tempfile

def getConfigPath():
    '''
    return array with paths used in the configuration.

    * array[0] = TEMP_NAME_DIRECTORY
    * array[1] = TELEGRAM_TEMP_DIRECTORY
    * array[2] = CONFIG_FILE
    * array[3] = README_FILE

    @desc:
    - TEMP_NAME_DIRECTORY = Nombre del directorio en temp.
    - TELEGRAM_TEMP_DIRECTORY = Ruta del directorio temp.
    - CONFIG_FILE = Ruta donde se guardará el archivo config.cfg
    - README_FILE = Ruta donde se guardará el archivo Leeme.txt
    '''
    TEMP_NAME_DIRECTORY = '.telegramBot'
    TELEGRAM_TEMP_DIRECTORY = os.path.join(tempfile.gettempdir(), TEMP_NAME_DIRECTORY)
    CONFIG_FILE = TELEGRAM_TEMP_DIRECTORY + '\\config.cfg'
    README_FILE = TELEGRAM_TEMP_DIRECTORY + '\\Leeme.txt'

    return [TEMP_NAME_DIRECTORY, TELEGRAM_TEMP_DIRECTORY, CONFIG_FILE, README_FILE]

def setConfigValues(token_api, token_chat, configFile):
    # Lectura del archivo de configuración.
    config = configparser.ConfigParser()
    config.read(configFile)

    # Escritura de valores.
    config.set('Telegram', 'TELEGRAM_API_KEY', token_api)
    config.set('Telegram', 'TELEGRAM_CHAT_ID', token_chat)

    # Guardar los cambios en el archivo de configuración
    with open(configFile, 'w') as configurationFile:
        config.write(configurationFile)

def getConfigValues(configFile):
    '''
    return array with config.cfg information

    * array[0] = TELEGRAM_API_KEY
    * array[1] = TELEGRAM_CHAT_ID
    '''
    config = configparser.ConfigParser()
    config.read(configFile)

    config_api_key = config.get('Telegram', 'TELEGRAM_API_KEY')
    config_chat_id = config.get('Telegram', 'TELEGRAM_CHAT_ID')
    return [config_api_key, config_chat_id]