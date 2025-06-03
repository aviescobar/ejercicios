import socket

def receive_file():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 8080))
    server.listen(1)
    print("Esperando conexión entrante...")

    conn, addr = server.accept()
    print(f"Conexión establecida desde: {addr}")

    with open('captura_recibida.txt', 'wb') as file:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            file.write(data)

    print("Archivo recibido correctamente.")
    conn.close()
    server.close()

receive_file()
# Commit automático del día 21
# Commit automático del día 21
# Commit automático del día 21
# Commit automático del día 21
