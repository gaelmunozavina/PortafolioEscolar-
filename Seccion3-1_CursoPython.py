# Resumen de la sección 3.2 - Bucles en Python

print("SECCIÓN 3.2 - BUCLES EN PYTHON")

# 1. Bucle while
print("\n1. Ejemplo de bucle while")

contador = 1
while contador <= 5:
    print("Iteración:", contador)
    contador += 1

print("Fin del bucle while")

# 2. Bucle infinito (ejemplo controlado)
print("\n2. Ejemplo de bucle infinito controlado con break")

while True:
    numero = int(input("Ingresa un número (0 para salir): "))
    if numero == 0:
        print("Saliendo del bucle...")
        break

# 3. Bucle for con range()
print("\n3. Bucle for con range()")

for i in range(5):
    print("Valor de i:", i)

# 4. range con inicio y fin
print("\n4. range con inicio y fin")

for i in range(2, 8):
    print("Valor:", i)

# 5. range con incremento
print("\n5. range con incremento")

for i in range(2, 10, 2):
    print("Número:", i)

# 6. break
print("\n6. Ejemplo de break")

for i in range(1, 6):
    if i == 3:
        break
    print("Dentro del bucle:", i)

print("Fuera del bucle")

# 7. continue
print("\n7. Ejemplo de continue")

for i in range(1, 6):
    if i == 3:
        continue
    print("Número:", i)

print("Fin del ejemplo continue")

# 8. Ejemplo práctico: contar pares e impares
print("\n8. Contar números pares e impares")

pares = 0
impares = 0

numero = int(input("Ingresa un número (0 para terminar): "))

while numero != 0:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    numero = int(input("Ingresa otro número (0 para terminar): "))

print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)

print("\nFin del resumen de bucles.")
