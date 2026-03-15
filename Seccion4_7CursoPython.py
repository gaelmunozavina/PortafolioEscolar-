
while True:
    try:
        # Pedimos un número entero al usuario
        value = int(input("Ingresa un número entero: "))
        
        # Calculamos su recíproco (1/value)
        print("El recíproco de", value, "es", 1/value)
        
        # Si todo salió bien, salimos del bucle
        break

    # Manejo de excepción si el valor ingresado no es un número
    except ValueError:
        print("Advertencia: el valor ingresado no es un número válido. Intenta de nuevo...")

    # Manejo de excepción si el usuario ingresa cero
    except ZeroDivisionError:
        print("La división entre cero no está permitida. Intenta de nuevo...")

    # Cualquier otra excepción inesperada
    except Exception as e:
        print("Algo salió mal:", e)
