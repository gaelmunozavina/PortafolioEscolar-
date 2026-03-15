Ejemplo de función recursiva: factorial

def factorial(n):
    if n == 1:          # condición de terminación
        return 1
    else:
        return n * factorial(n - 1)

# prueba de la función
num = 4
resultado = factorial(num)

print("El factorial de", num, "es:", resultado)
