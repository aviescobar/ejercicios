import os
import atexit

def configurar_ping(permitir):
    """
    Configura las reglas del firewall para permitir o denegar pings.
    """
    try:
        if permitir:
            # Eliminar regla que bloquea ICMP (si existe)
            os.system("iptables -D INPUT -p icmp --icmp-type echo-request -j DROP 2>/dev/null")
            print("Ping permitido hacia el servidor.")
        else:
            # Agregar regla para bloquear ICMP
            os.system("iptables -A INPUT -p icmp --icmp-type echo-request -j DROP")
            print("Ping denegado hacia el servidor.")
    except Exception as e:
        print(f"Error al modificar reglas de ping: {e}")

def restaurar_estado_predeterminado():
    """
    Restaura el estado predeterminado para permitir pings al servidor.
    """
    print("\nRestaurando estado predeterminado (permitir pings)...")
    configurar_ping(True)

def mostrar_menu():
    """
    Muestra un menú para que el administrador del servidor permita o deniegue pings.
    """
    while True:
        print("\nControl de Ping del Servidor:")
        print("1. Permitir ping")
        print("2. Denegar ping")
        print("3. Salir")
        opcion = input("Elige una opción (1/2/3): ").strip()

        if opcion == "1":
            configurar_ping(True)
        elif opcion == "2":
            configurar_ping(False)
        elif opcion == "3":
            print("Saliendo del control de ping.")
            break
        else:
            print("Opción no válida. Por favor, elige 1, 2 o 3.")

if __name__ == "__main__":
    print("Iniciando control de pings del servidor...")

    # Asegurarse de restaurar el estado al salir
    atexit.register(restaurar_estado_predeterminado)

    mostrar_menu()
# Commit automático del día 18
# Commit automático del día 18
# Commit automático del día 18
# Commit automático del día 18
# Commit automático del día 18
