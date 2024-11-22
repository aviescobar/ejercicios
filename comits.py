import subprocess
from datetime import datetime, timedelta
import os

# Configuración
repo_dir = "/home/rafael/Documents/Python_Exercises2"  # Cambia por la ruta de tu repositorio local
start_date = datetime(2024, 11, 12)  # Fecha de inicio
days = 8  # Número de archivos/días
branch = "master"  # Rama en la que estás trabajando

# Cambia a la carpeta del repositorio
os.chdir(repo_dir)

# Generar y subir commits
for i in range(days):
    # Nombre del archivo correspondiente a cada día
    file_name = f"ejercicio_{i+1}.py"
    
    # Verifica si el archivo existe antes de intentar hacer commit
    if os.path.exists(file_name):
        # Añadir el archivo al stage
        subprocess.run(["git", "add", file_name])

        # Calcular la fecha del commit
        commit_date = (start_date + timedelta(days=i)).strftime("%Y-%m-%dT12:00:00")

        # Hacer el commit con la fecha deseada
        commit_command = f'GIT_AUTHOR_DATE="{commit_date}" GIT_COMMITTER_DATE="{commit_date}" git commit -m "Añadir {file_name} en {commit_date}"'
        subprocess.run(commit_command, shell=True)
    else:
        print(f"Archivo {file_name} no encontrado, saltando...")

# Subir todos los commits en un solo comando
subprocess.run(["git", "push", "origin", branch])