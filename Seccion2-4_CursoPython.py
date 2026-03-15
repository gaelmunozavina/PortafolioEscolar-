print("SECCIÓN 2.4 - VARIABLES EN PYTHON")

print("\n1. Una variable es una 'caja' donde se guarda información en un programa.")

print("\n2. Una variable tiene dos partes importantes:")
print("- Un nombre")
print("- Un valor")

print("\n3. Las variables se crean cuando se les asigna un valor usando el signo =")

var = 1
print("Ejemplo: var =", var)

print("\n4. Las variables pueden guardar diferentes tipos de datos:")
numero = 10
decimal = 3.5
texto = "Hola"

print("Número:", numero)
print("Decimal:", decimal)
print("Texto:", texto)

print("\n5. Reglas para nombres de variables:")
print("- Deben empezar con una letra o _")
print("- Pueden tener letras, números y _")
print("- No pueden tener espacios")
print("- No pueden ser palabras reservadas de Python")

print("\n6. Python distingue entre mayúsculas y minúsculas")
var = 5
Var = 10
print("var =", var)
print("Var =", Var)

print("\n7. Se puede cambiar el valor de una variable:")
contador = 1
print("Valor inicial:", contador)

contador = contador + 1
print("Nuevo valor:", contador)

print("\n8. Operadores abreviados:")
x = 5
print("Valor inicial de x:", x)

x += 2
print("x += 2 ->", x)

x *= 3
print("x *= 3 ->", x)

print("\n9. Ejemplo matemático: Teorema de Pitágoras")

a = 3
b = 4
c = (a**2 + b**2) ** 0.5

print("a =", a)
print("b =", b)
print("Hipotenusa =", c)

print("\n10. Ejemplo de suma de variables (manzanas)")

john = 3
mary = 5
adam = 6

total_apples = john + mary + adam

print("Manzanas de John:", john)
print("Manzanas de Mary:", mary)
print("Manzanas de Adam:", adam)
print("Total de manzanas:", total_apples)

