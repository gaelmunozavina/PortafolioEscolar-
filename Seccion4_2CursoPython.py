# Ejemplo del capítulo 4.2 – Funciones con parámetros

def suma(a, b, c=0):
    print(a, "+", b, "+", c, "=", a + b + c)

print("Ejemplo con argumentos posicionales")
suma(2, 3, 4)

print("Ejemplo con argumentos de palabra clave")
suma(a=5, b=6, c=7)

print("Ejemplo mezclando tipos")
suma(8, b=2, c=1)

print("Ejemplo usando valor por defecto")
suma(10, 5)
