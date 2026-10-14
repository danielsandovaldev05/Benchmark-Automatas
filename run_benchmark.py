import subprocess
import time
import os

# Rutas basadas en tu estructura de carpetas
input_file = "large_input.txt"
c_executable = os.path.join("Flex y Bison", "calc_c.exe")
ply_script = os.path.join("PLY", "calc_ply.py")

# Ruta exacta del Python donde tienes instalado PLY
python_executable = r"C:\Users\ds832\AppData\Local\Python\pythoncore-3.14-64\python.exe"

print("--- INICIANDO BENCHMARK ---")

# 1. Medir Flex/Bison (C)
try:
    start_c = time.time()
    subprocess.run([c_executable, input_file], stdout=subprocess.DEVNULL, check=True)
    end_c = time.time()
    time_c = end_c - start_c
    print(f"Tiempo con Flex/Bison (C): {time_c:.4f} segundos")
except Exception as e:
    print(f"Error al ejecutar C: {e}")
    time_c = None

# 2. Medir PLY (Python) usando el intérprete correcto
try:
    start_ply = time.time()
    subprocess.run([python_executable, ply_script, input_file], stdout=subprocess.DEVNULL, check=True)
    end_ply = time.time()
    time_ply = end_ply - start_ply
    print(f"Tiempo con PLY (Python):   {time_ply:.4f} segundos")
except Exception as e:
    print(f"Error al ejecutar PLY: {e}")
    time_ply = None

# Comparativa final si ambos corrieron con éxito
if time_c and time_ply:
    print("\n[RESULTADOS]")
    print(f"Diferencia: PLY es aproximadamente {time_ply / time_c:.1f}x más lento que C.")