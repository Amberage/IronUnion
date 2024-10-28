
import sys, os
from modules import configManager as config
from modules import message as msg
from modules import screenshot

#* Constantes de desarrollo
DEVELPOMENT_STATE = False

#* Determinación de que rutas elegir en caso de ser necesario.
if DEVELPOMENT_STATE == True:
    rootPath = os.path.join(os.path.dirname(__file__))
else:
    rootPath = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))


#. Inicio del bot
ARGUMENTS_LENGTH = len(sys.argv)
VALID_ARGUMENTS = ['-c', '-m', '-s']
ARGUMENTS = sys.argv

if __name__ == "__main__":
    if ARGUMENTS_LENGTH <= 1:
        print("Metin2 Telegram Bot - By: rem0kr3\n")
        config.configure(rootPath)

    else:
        match ARGUMENTS[1]:
            case '-c':
                print("Iniciando configuración.")
                config.configure(rootPath)

            case '-m':
                if ARGUMENTS_LENGTH == 3:
                    print("Enviando mensaje...")
                    msg.sendMessage(ARGUMENTS[2])
                else:
                    print("Error, se esperaba un argumento.")
                    msg.sendMessage()
                #

            case '-s':
                print("Enviando captura de pantalla.")
                screenshot.sendEvidence()

            case _:
                print("Iniciando configuración.")
                config.configure(rootPath)
