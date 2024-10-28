# Metin2 Telegram Bot

Este programa busca simplificar la instalación de un bot para Telegram de uso multipropósito.

Las funcionalidades que ofrece el bot actualmente son:
* Enviar mensajes a un único chat de Telegram.
* Enviar una captura de pantalla a un único chat de Telegram.

## Instalación de librerias y empaquetado

Para instalar el proeycto en su versión de desarrollo basta con hacer un:

```yaml
pip install -r requirements.txt
```

Para empaquetar en un único ejecutable es necesario previamente haber instalado pyinstaller _(se hace con el paso anterior)_ y empaquetarlo con pyinstaller junto a las carpetas `modules` y `assets`.
## Funcionalidades

Para configurar el bot basta con ejecutarlo, por otra parte, para usar las funcionalidades se debe usar una linea de comandos:

| Función | Bandera | Argumento |
|----------|----------|----------|
| Entrar en modo configuración. |  | Ejecutar el .exe |
| Mandar mensaje | -m | \<mensaje\> |
| Captura de pantalla | -s | No se espera argumento. |

Ejemplos:
* main.exe -m "Hola mundo!"
* main.exe -s

## Notas adicionales
* Falta implementar control de errores.
* Mostrar ventanas con errores, acutlamente hay casos donde se entra en estado de error sin mostrar en una interfaz el error.