import socket
import pyautogui
from PIL import Image
import io
import time

# Configuramos el cliente
server_ip = "172.168.2.25"  # Cambia a la IP del servidor
server_port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

try:
    while True:
        # Capturar pantalla
        screenshot = pyautogui.screenshot()

        # Convertir la imagen a bytes
        img_bytes = io.BytesIO()
        screenshot.save(img_bytes, format="JPEG")
        img_data = img_bytes.getvalue()

        # Enviar el tamaño de la imagen
        data_size = len(img_data)
        client_socket.sendall(data_size.to_bytes(8, 'big'))

        # Enviar la imagen en bytes
        client_socket.sendall(img_data)

        # Esperar unos segundos antes de la siguiente captura
        time.sleep(2)  # Captura cada 2 segundos
except Exception as e:
    print(f"Ocurrió un error: {e}")
finally:
    client_socket.close()
    print("Conexión cerrada.")
