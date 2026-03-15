print("SECCIÓN 3.1 - Comparaciones y decisiones")

# 1. Operador de igualdad ==
print("\n1. Operador ==")

print("2 == 2 :", 2 == 2)
print("2 == 2.0 :", 2 == 2.0)
print("1 == 2 :", 1 == 2)

# 2. Diferencia entre = y ==
print("\n2. Diferencia entre = y ==")

a = 5     # asignación
print("a =", a)

print("¿a es igual a 5?", a == 5)

# 3. Operador diferente !=
print("\n3. Operador !=")

var = 0
print("var != 0 :", var != 0)

var = 1
print("var != 0 :", var != 0)

# 4. Operadores de comparación
print("\n4. Otros operadores de comparación")

print("10 > 5 :", 10 > 5)
print("10 >= 10 :", 10 >= 10)
print("5 < 3 :", 5 < 3)
print("5 <= 5 :", 5 <= 5)

# 5. Guardar resultado de comparación en una variable
print("\n5. Guardar el resultado en una variable")

lions = 5
lionesses = 3

answer = lions >= lionesses
print("¿Hay más o igual leones que leonas?:", answer)

# 6. Ejemplo del LAB
print("\n6. Ejercicio del LAB")

n = int(input("Ingresa un número: "))
print(n >= 100)
