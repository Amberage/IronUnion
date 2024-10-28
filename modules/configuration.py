import shutil, tempfile, os, telebot, flet as ft, webbrowser, threading
from . import accessKeys as key

'''
Descripción de las constantes:
╔═════════════════════════╦═══════════════════════════════════════════════╗
║        Constante        ║                  Descripción                  ║
╠═════════════════════════╬═══════════════════════════════════════════════╣
║ TELEGRAM_TEMP_DIRECTORY ║ Ruta del directorio temp de windows.          ║
║ TEMP_NAME_DIRECTORY     ║ Nombre de la carpeta que se guardará en temp. ║
║ CONFIG_FILE             ║ Ruta del archivo config.cfg en windows.       ║
║ README_FILE             ║ Ruta del achivo Leeme.txt en windows.         ║
╚═════════════════════════╩═══════════════════════════════════════════════╝

Descripción de las variables:
╔════════════════╦═══════════════════════════════════════════════════════════════════╗
║    Variable    ║                            Descripción                            ║
╠════════════════╬═══════════════════════════════════════════════════════════════════╣
║ readmeSource   ║ Archivo original del readme que se copia del .exe a temp.         ║
║ configSource   ║ Archivo original de configuración que se copia del .exe a temp.   ║
║ config_api_key ║ Almacena el valor del API KEY obtenido de config.cfg desde temp.  ║
║ config_chat_id ║ Almacena el valor del CHAT ID obtenido del config.cfg desde temp. ║
╚════════════════╩═══════════════════════════════════════════════════════════════════╝

Nota: rootPath es un argumento que es recibido desde el main, es la ruta de ejecución del .exe
'''

TEMP_NAME_DIRECTORY = '.TelegramBot'
TELEGRAM_TEMP_DIRECTORY = os.path.join(tempfile.gettempdir(), TEMP_NAME_DIRECTORY)
CONFIG_FILE = TELEGRAM_TEMP_DIRECTORY + '\\config.cfg'
README_FILE = TELEGRAM_TEMP_DIRECTORY + '\\Leeme.txt'

#!
def verifyDirectory(rootPath):
    readmeSource = rootPath + '\\assets\\readme'
    configSource = rootPath + '\\assets\\config.cfg'

    # Crear directorio TelegramBot en la carpeta temporal de Windows
    os.makedirs(TELEGRAM_TEMP_DIRECTORY, exist_ok=True)  # Crea el directorio, no lanza error si ya existe

    if not os.path.exists(README_FILE):
        #Si no existe el readme, entonces lo crea.
        shutil.copy(readmeSource, README_FILE)

    # Revisar si el fichero config.cfg existe en el directorio temporal
    if not os.path.exists(CONFIG_FILE):
        # Si no existe, copiar desde la ruta de origen
        shutil.copy(configSource, CONFIG_FILE)
        print('-> ¡Configuración inicial creada con éxito!\n')
    else:
        print('-> ¡Se ha encontrado una configuración existente.\n-> Iniciando una nueva configuración...\n')
    
#!
def testConnection():
    configValues = key.getConfigValues()
    
    config_api_key = configValues[0]
    config_chat_id = configValues[1]

    try:
        bot = telebot.TeleBot(config_api_key)
        @bot.message_handler(func=lambda message: True)
        def handle_message(message):
            bot.reply_to(message, f"Hola {message.from_user.first_name} 👋, la configuración ha sido exitosa!! 🎉\n\nSolo falta verificar que '{config_chat_id}' sea el CHAT ID que te proporciono @userinfobot.\n\nSi los datos son correctos la configuración ha finalizado y puedes cerrar el programa de configuración, de lo contrario cierra y vuelve a iniciar la configuración. 🫠\n\n⚠️ Importante ⚠️: El API Token de este bot debe ser confidencial, nunca lo compartas pues este bot podría ser intervenido por terceros. 👀")

        threading.Thread(target=bot.polling, daemon=True).start()
        return True  # Indica que la conexión es exitosa
    except:
        print("Error de conexión, revisar el token del API")
        return False

#!
def configureGUI(page: ft.Page):
    #. -> Configuración APP
    page.title = "Metin2 Telegram Reporter | By: remk0r3"
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.window_width = 550
    page.window_height = 320
    page.window_resizable = False
    page.padding = 25
    page.scroll = ft.ScrollMode.HIDDEN

    #. -> Elementos
    #? Textos
    txt_Confirmation = ft.Text(value = "Datos almacenados correctamente.", text_align = 'center')

    #? Textfields:
    txtField_apiToken = ft.TextField(label = "Token API HTTP", hint_text = "Ingrese su token 'API HTTP' de su bot en Telegram.")
    txtField_chatId = ft.TextField(label = "Chat ID", hint_text = "Ingrese su Chat ID de Telegram.")
    
    #? Ventanas Modales:
    modal_help = ft.AlertDialog(title=ft.Column([
        ft.TextButton("¿Cómo obtener el token del API HTTP?", style=ft.ButtonStyle(color=ft.colors.BLUE), on_click=lambda e: webbrowser.open("https://www.youtube.com/watch?v=VLXElCqqcsg")),
        ft.TextButton("¿Cómo obtener el Chat ID?", style=ft.ButtonStyle(color=ft.colors.BLUE), on_click=lambda e: webbrowser.open("https://www.youtube.com/watch?v=Fzr88Iz75Uo"))
        ]))
    
    modal_connError = ft.AlertDialog(title=ft.Text("Error: El token del 'API HTTP' no pudo conectarse con el bot, compruebe que el token sea correcto e intente nuevamente."))

    #. -> Obtener valores de la configuración
    configValues = key.getConfigValues()

    txtField_apiToken.value = configValues[0]
    txtField_chatId.value = configValues[1]

    #. -> Funciones

    #? Validar los campos input
    def validateFields(e):
        if not txtField_apiToken.value:
            txtField_apiToken.error_text = "Por favor, ingrese el token del 'API HTTP' de su bot."

        elif not txtField_chatId.value:
            txtField_chatId.error_text = "Por favor, ingrese el Chat ID de su cuenta de Telegram."

        elif not txtField_chatId.value.isdigit(): 
            txtField_chatId.error_text = "Por favor, ingrese un Chat ID válido, solo números."
            
        else:
            #? Se vuelven a obtener los valores del textField y se guardan en el config.cfg
            token_api = txtField_apiToken.value
            token_chat = txtField_chatId.value
            key.setConfigValues(token_api, token_chat)

            #? Se valida la conexión al API
            isValid = testConnection()
            if isValid == False:
                page.open(modal_connError)
                txtField_apiToken.value = ''
                key.setConfigValues('', token_chat)
            else:
                # Mostrar mensaje de confirmación
                page.clean()
                page.add(txt_Confirmation)
                # Iniciar bot.polling
                # startBotPolling()
                
    

            

        page.update()
    

    page.add(txtField_apiToken, txtField_chatId, ft.ElevatedButton("Say hello!", on_click=validateFields), ft.ElevatedButton("Ayuda", on_click=lambda e: page.open(modal_help)))


def configure(rootPath):
    #? 1. Crear el directorio en temp, si ya existe preservarlo, si no existe crearlo con configuraciones default.
    verifyDirectory(rootPath)
    
    #? 2. Capturar API Key y Chat ID
    #setConfigValues()
    
    #? 3. Testear conexión
    #testConnection()

    ft.app(configureGUI)


