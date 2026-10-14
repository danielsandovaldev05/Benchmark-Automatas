# Generar archivo de prueba
with open("large_input.txt", "w") as f:
    for i in range(50000):
        f.write(f"({i} + 10) * 2 / 5\n")
print("Archivo 'large_input.txt' creado con éxito.")