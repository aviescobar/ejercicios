import random


def adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0


    while True:
        intento = int(input("Adivina un número entre 1 y 100: "))
        intentos += 1

        if intento < numero_secreto:
            print("El número es mayor.")
        elif intento > numero_secreto:
            print("El número es menor.")
        else:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break

adivina_el_numero()
# Commit automático del día 3
# Commit automático del día 3
# Commit automático del día 3
# Commit automático del día 3
# Commit automático del día 3
# Commit automático del día 3
