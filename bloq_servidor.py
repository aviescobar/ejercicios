import socket

# Configurar el servidor
HOST = "0.0.0.0"  # Escuchar en todas las interfaces
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"Servidor en ejecución en {HOST}:{PORT}")
    conn, addr = server.accept()
    print(f"Conexión establecida desde {addr}")
    with conn:
        try:
            while True:
                comando = input("Escribe un comando para el cliente (bloquear/desbloquear/salir): ").strip()
                if comando == "salir":
                    print("Cerrando conexión...")
                    break
                conn.sendall(comando.encode())
                respuesta = conn.recv(1024).decode()
                print(f"Respuesta del cliente: {respuesta}")
        except KeyboardInterrupt:
            print("\nServidor detenido.")
# Commit automático del día 6
# Commit automático del día 6
