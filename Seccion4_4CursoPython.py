
# Variable global
var = 1

def my_function():
    global var
    print("Valor antes del cambio:", var)
    var = 2
    print("Valor dentro de la función:", var)

def local_example():
    x = 5
    print("Variable local:", x)

print("Valor inicial:", var)

my_function()

print("Valor después de la función:", var)

local_example()
