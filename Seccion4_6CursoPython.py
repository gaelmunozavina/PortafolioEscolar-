
# Ejemplo de Tuplas y Diccionarios

# Tupla (inmutable)
numeros = (10, 20, 30, 40)

print("Elementos de la tupla:")
for n in numeros:
    print(n)

# Diccionario (clave : valor)
estudiantes = {
    "Ana": 9,
    "Luis": 8,
    "Carlos": 7
}

print("\nCalificaciones de estudiantes:")

for nombre, calificacion in estudiantes.items():
    print(nombre, "->", calificacion)

# Agregar un nuevo elemento al diccionario
estudiantes["Maria"] = 10

print("\nDiccionario actualizado:")
print(estudiantes)
