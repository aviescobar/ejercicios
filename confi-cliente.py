import socket

# Configuración del servidor
IP_SERVIDOR = '0.0.0.0'  # Escuchar en todas las interfaces
PUERTO_SERVIDOR = 8081

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((IP_SERVIDOR, PUERTO_SERVIDOR))
servidor.listen(1)

print("Esperando conexión del cliente para enviar señal de apagado...")
cliente_socket, cliente_direccion = servidor.accept()
print(f"Conectado con {cliente_direccion}")

# Enviar señal de apagado sin preguntar
mensaje = "APAGAR"
cliente_socket.sendall(mensaje.encode())
print("Señal de apagado enviada al cliente.")

cliente_socket.close()
servidor.close()# Commit automático del día 10
# Commit automático del día 10
# Commit automático del día 10
