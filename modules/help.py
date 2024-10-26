TEXT_HELP ='''+-------------------------------+---------+------------------------------------+
|            Función            | Bandera |             Argumento              |
+-------------------------------+---------+------------------------------------+
| Ayuda                         | -h      | No se espera argumento ni bandera. |
| Entrar en modo configuración. | -c      | No se espera argumento.            |
| Mandar mensaje                | -m      | <mensaje>                          |
| Captura de pantalla           | -s      | No se espera argumento.            |
+-------------------------------+---------+------------------------------------+'''

def showHelp():
    print(TEXT_HELP)