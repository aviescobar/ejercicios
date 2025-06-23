import socket

# Definir la IP y el puerto del servidor
HOST = '0.0.0.0'  # Escuchar en todas las interfaces
PORT = 5000     # Puerto del servidor

# Lista de IPs denegadas
DENIED_IPS = ['172.168.0.21', '172.168.2.146']  # Añadir las IPs que se quieren denegar

# Configuración del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
print(f"Servidor escuchando en {HOST}:{PORT}")

while True:
    # Aceptar conexión del cliente
    client_socket, client_address = server_socket.accept()
    client_ip, client_port = client_address
    print(f"Conexión de: {client_ip}:{client_port}")

    # Verificar si la IP está en la lista de denegados
    if client_ip in DENIED_IPS:
        print(f"Conexión denegada para: {client_ip}")
        client_socket.close()  # Cerrar el socket del cliente
    else:
        print(f"Conexión permitida para: {client_ip}")
        # Aquí puedes iniciar la comunicación con el cliente
        # Por ejemplo, enviarle un mensaje de bienvenida
        client_socket.sendall(b"Bienvenido al servidor!")

        # Aquí puedes agregar más lógica de comunicación

        # Cerrar la conexión después de completar la comunicación
        client_socket.close()# Commit automático del día 17
# Commit automático del día 17
# Commit automático del día 17
# Commit automático del día 17
# Commit automático del día 17
