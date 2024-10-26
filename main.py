
import sys, os
from modules import help as hp
from modules import configuration as config

#* Constantes de desarrollo
DEVELPOMENT_STATE = False
""" TELEGRAM_API_KEY = "7205288012:AAHWaaEidxCU-fV2kaCtlyvJzUkFsJ3LL1M"
TELEGRAM_CHAT_ID = "1300633499"
 """

#* Determinación de que rutas elegir en caso de ser necesario.
if DEVELPOMENT_STATE == True:
    rootPath = os.path.join(os.path.dirname(__file__))
else:
    rootPath = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))


#. Inicio del bot
ARGUMENTS_LENGTH = len(sys.argv)
VALID_ARGUMENTS = ['-h', '-c', '-m', '-s', '-e']
ARGUMENTS = sys.argv

if __name__ == "__main__":
    if ARGUMENTS_LENGTH <= 1:
        print("Metin2 Telegram Bot - By: rem0kr3\n")
        hp.showHelp()

    else:
        match ARGUMENTS[1]:
            case '-h':
                print("Metin2 Telegram Bot - By: rem0kr3\n")
                hp.showHelp()

            case '-c':
                print("Iniciando configuración.")
                config.configure(rootPath)

            case '-m':
                print("Enviando mensaje.")

            case '-s':
                print("Enviando captura de pantalla.")

            case _:
                print("Error, argumento invalido.")
