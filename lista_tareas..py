class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

    def completar(self):
        self.completada = True

    def __str__(self):
        estado = "Completada" if self.completada else "Pendiente"
        return f"{self.descripcion} - {estado}"

def lista_tareas():
    tareas = []

    while True:
        print("\n1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Completar tarea")
        print("4. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            descripcion = input("Ingrese la descripción de la tarea: ")
            tareas.append(Tarea(descripcion))
        elif opcion == "2":
            for i, tarea in enumerate(tareas, start=1):
                print(f"{i}. {tarea}")
        elif opcion == "3":
            if tareas:
                for i, tarea in enumerate(tareas, start=1):
                    print(f"{i}. {tarea}")
                opcion = int(input("Ingrese el número de la tarea a completar: "))
                if opcion > 0 and opcion <= len(tareas):
                    tareas[opcion - 1].completar()
                else:
                    print("Error: Opción no válida")
            else:
                print("No hay tareas")
        elif opcion == "4":
            break
        else:
            print("Error: Opción no válida")

lista_tareas()# Commit automático del día 14
# Commit automático del día 14
# Commit automático del día 14
# Commit automático del día 14
