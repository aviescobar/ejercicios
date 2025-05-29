import socket

# Configuración del servidor
HOST = '0.0.0.0'  # Dirección IP del servidor
PORT = 8080         # Puerto en el que el servidor escuchará

# Lista de páginas prohibidas
PAGINAS_PROHIBIDAS = ["/prohibido.html", "/privado.html"]

def servidor():
    # Crear el socket del servidor
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.bind((HOST, PORT))
    servidor_socket.listen(5)
    print(f"Servidor escuchando en {HOST}:{PORT}")

    while True:
        cliente_socket, direccion = servidor_socket.accept()
        print(f"Conexión recibida de {direccion}")

        # Recibir la solicitud del cliente
        solicitud = cliente_socket.recv(1024).decode()
        print(f"Solicitud:\n{solicitud}")

        # Extraer la página solicitada
        primera_linea = solicitud.splitlines()[0]
        pagina_solicitada = primera_linea.split(" ")[1]

        # Comprobar si la página está prohibida
        if pagina_solicitada in PAGINAS_PROHIBIDAS:
            respuesta = (
                "HTTP/1.1 403 Forbidden\r\n"
                "Content-Type: text/html\r\n\r\n"
                "<html><body><h1>403 Acceso Denegado</h1></body></html>"
            )
        else:
            respuesta = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/html\r\n\r\n"
                "<html><body><h1>Bienvenido!</h1></body></html>"
            )

        # Enviar la respuesta al cliente
        cliente_socket.sendall(respuesta.encode())
        cliente_socket.close()

if __name__ == "__main__":
    try:  ## mañana 
        servidor()
    except KeyboardInterrupt:
        print("\nServidor detenido.")
# Commit automático del día 16
# Commit automático del día 16
# Commit automático del día 16
# Commit automático del día 16
