import socket

# Crear un socket
servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Definir la dirección y el puerto
direccion = ('172.168.3.223', 12345)  # Puedes cambiar 'localhost' por la IP del servidor si es necesario
servidor_socket.bind(direccion)

# Escuchar conexiones entrantes
servidor_socket.listen(1)
print("Esperando conexiones...")

while True:
    # Aceptar una conexión
    cliente_socket, addr = servidor_socket.accept()
    print(f"Conexión establecida con {addr}")

    while True:
        # Recibir datos del cliente
        datos = cliente_socket.recv(1024)
        if not datos:
            break  # Salir si no hay más datos

        print(f"Recibido del cliente: {datos.decode()}")

        # Enviar una respuesta al cliente
        respuesta = "Datos recibidos"
        cliente_socket.send(respuesta.encode())

    # Cerrar la conexión con el cliente
    cliente_socket.close()
    print(f"Conexión cerrada con {addr}")

# No olvides cerrar el socket del servidor (este código no se alcanzará en este ejemplo)
servidor_socket.close()# Commit automático del día 22
# Commit automático del día 22
# Commit automático del día 22
# Commit automático del día 22
