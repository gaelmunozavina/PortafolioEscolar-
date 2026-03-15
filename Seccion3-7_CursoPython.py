# Ejemplo del capítulo 3.7 – Aplicaciones avanzadas de listas

# 1. Comprensión de listas
squares = [x**2 for x in range(10)]
print("Cuadrados:", squares)

# 2. Crear una matriz 5x5 usando listas dentro de listas
matrix = [[0 for i in range(5)] for j in range(5)]

print("Matriz inicial:")
for row in matrix:
    print(row)

# 3. Modificar algunos valores en la matriz
matrix[1][2] = 7
matrix[3][4] = 9

print("Matriz modificada:")
for row in matrix:
    print(row)

# 4. Recorrer la matriz para encontrar el número mayor
largest = matrix[0][0]

for row in matrix:
    for value in row:
        if value > largest:
            largest = value

print("El número mayor en la matriz es:", largest)
