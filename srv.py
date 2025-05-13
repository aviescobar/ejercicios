# servidor.py
import socket
from PIL import Image
import io

# Configuramos el servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 12345))  # Usar dirección IP del servidor y un puerto adecuado
server_socket.listen(1)
print("Esperando conexión del cliente...")

conn, addr = server_socket.accept()
print(f"Conectado con: {addr}")

try:
    while True:
        # Recibir el tamaño de los datos
        data_size = conn.recv(8)
        if not data_size:
            break
        data_size = int.from_bytes(data_size, 'big')
        
        # Recibir la imagen en bytes
        data = b''
        while len(data) < data_size:
            packet = conn.recv(4096)
            if not packet:
                break
            data += packet
        
        # Cargar y mostrar la imagen recibida
        image = Image.open(io.BytesIO(data))
        image.show()  # Muestra la imagen (bloquea el proceso, en producción sería mejor guardarla en archivo)
        
finally:
    conn.close()
    server_socket.close()
    print("Conexión cerrada.")# Commit automático del día 23
