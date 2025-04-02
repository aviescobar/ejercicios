import socket
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def enviar_archivo(cliente_socket):
    Tk().withdraw()  # Oculta la ventana principal
    archivo_path = askopenfilename()  # Permite seleccionar un archivo
    
    if archivo_path:
        cliente_socket.send("archivo".encode())
        
        nombre_archivo = os.path.basename(archivo_path)
        tamano_archivo = os.path.getsize(archivo_path)
        
        cliente_socket.send(nombre_archivo.encode())
        cliente_socket.send(str(tamano_archivo).encode())
        
        with open(archivo_path, "rb") as f:
            while (datos := f.read(1024)):
                cliente_socket.send(datos)
        print(f"Archivo enviado: {nombre_archivo}")

def enviar_texto(cliente_socket):
    mensaje = input("Escribe tu mensaje: ")
    cliente_socket.send("texto".encode())
    cliente_socket.send(mensaje.encode())
    print("Mensaje enviado:", mensaje)

def cliente():
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_socket.connect(("172.168.3.92", 9999))
    
    while True:
        opcion = input("¿Enviar archivo o texto? (archivo/texto): ")
        if opcion == "archivo":
            enviar_archivo(cliente_socket)
        elif opcion == "texto":
            enviar_texto(cliente_socket)

cliente()# Commit automático del día 12
# Commit automático del día 12
# Commit automático del día 12
