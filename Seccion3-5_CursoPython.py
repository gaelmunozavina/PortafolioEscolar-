# Ordenamiento de listas con el algoritmo burbuja

numbers = []

cantidad = int(input("¿Cuántos números quieres ordenar?: "))

for i in range(cantidad):
    num = int(input("Ingresa un número: "))
    numbers.append(num)

print("Lista original:", numbers)

swapped = True

while swapped:
    swapped = False
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
            swapped = True

print("Lista ordenada:", numbers)
