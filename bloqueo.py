import paramiko
import tkinter as tk
from tkinter import messagebox

def ejecutar_comando_ssh(host, usuario, contraseña, comando):
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=host, username=usuario, password=contraseña)
        stdin, stdout, stderr = ssh_client.exec_command(comando)
        stdin.write(contraseña + '\n')
        stdin.flush()
        salida = stdout.read().decode("utf-8")
        error = stderr.read().decode("utf-8")
        ssh_client.close()
        return salida, error
    except Exception as e:
        return None, str(e)

def bloquear_entrada():
    host = host_entry.get()
    usuario = usuario_entry.get()
    contraseña = contraseña_entry.get()
    
    # Comando para instalar xtrlock y bloquear la pantalla
    comando_instalar = "echo {} | sudo -S apt-get install -y xtrlock".format(contraseña)
    comando_bloquear = "xtrlock"
    
    # Instalar xtrlock si no está instalado
    _, error_instalacion = ejecutar_comando_ssh(host, usuario, contraseña, comando_instalar)
    if error_instalacion:
        messagebox.showerror("Error", f"No se pudo instalar xtrlock: {error_instalacion}")
        return

    # Bloquear la pantalla con xtrlock
    _, error_bloqueo = ejecutar_comando_ssh(host, usuario, contraseña, comando_bloquear)
    
    if not error_bloqueo:
        messagebox.showinfo("Éxito", "Mouse y teclado bloqueados correctamente.")
    else:
        messagebox.showerror("Error", f"No se pudo bloquear el mouse o teclado: {error_bloqueo}")

def habilitar_boton(event=None):
    if host_entry.get() and usuario_entry.get() and contraseña_entry.get():
        btn_bloquear.config(state=tk.NORMAL)
    else:
        btn_bloquear.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Bloquear Mouse y Teclado Remoto")
root.geometry("380x380")
root.resizable(False, False)

# Obtener dimensiones de la pantalla
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calcular la posición para centrar la ventana
x = (screen_width // 2) - (380 // 2)
y = (screen_height // 2) - (380 // 2)

root.geometry(f"380x380+{x}+{y}")

tk.Label(root, text="Bloquear mouse y teclado de un usuario/cliente").pack(pady=10)

tk.Label(root, text="IP de la computadora:").pack(anchor="w", padx=20)
host_entry = tk.Entry(root)
host_entry.pack(fill="x", padx=20)
host_entry.bind("<KeyRelease>", habilitar_boton)

tk.Label(root, text="Nombre de usuario de la computadora:").pack(anchor="w", padx=20)
usuario_entry = tk.Entry(root)
usuario_entry.pack(fill="x", padx=20)
usuario_entry.bind("<KeyRelease>", habilitar_boton)

tk.Label(root, text="Contraseña de la computadora:").pack(anchor="w", padx=20)
contraseña_entry = tk.Entry(root, show="*")
contraseña_entry.pack(fill="x", padx=20)
contraseña_entry.bind("<KeyRelease>", habilitar_boton)

btn_bloquear = tk.Button(root, text="Bloquear", command=bloquear_entrada, state=tk.DISABLED)
btn_bloquear.pack(pady=20)

root.mainloop()