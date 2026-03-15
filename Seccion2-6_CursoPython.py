print("SECCIÓN 2.6 - INTERACCIÓN CON EL USUARIO")

print("\n1. La función print() muestra información en la consola.")

print("\n2. La función input() permite que el usuario introduzca datos.")

nombre = input("\nEscribe tu nombre: ")
print("Hola " + nombre + ", mucho gusto.")

print("\n3. El valor que devuelve input() siempre es una cadena (str).")

dato = input("Escribe un número: ")
print("El tipo de dato que ingresaste es:", type(dato))

print("\n4. Para hacer operaciones matemáticas hay que convertir el dato.")

numero = float(input("Ingresa un número para elevarlo al cuadrado: "))
resultado = numero ** 2

print("El número al cuadrado es:", resultado)

print("\n5. Operador + con cadenas (concatenación)")
nombre = input("Dime tu nombre: ")
apellido = input("Dime tu apellido: ")

print("Tu nombre completo es " + nombre + " " + apellido)

print("\n6. Operador * con cadenas (replicación)")
palabra = input("Escribe una palabra: ")
print("Palabra repetida 3 veces:", palabra * 3)

print("\n7. Ejemplo matemático con datos del usuario (hipotenusa)")

a = float(input("Ingresa el primer cateto: "))
b = float(input("Ingresa el segundo cateto: "))

hipotenusa = (a**2 + b**2) ** 0.5

print("La hipotenusa es:", hipotenusa)

print("\nFin del resumen de interacción con el usuario.")
