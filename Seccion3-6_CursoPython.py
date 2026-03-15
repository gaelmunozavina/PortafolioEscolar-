# Programa de ejemplo del capítulo 3.6 – Operaciones con listas

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

print("Lista original:", my_list)

# 1. Copiar la lista usando rebanada
copy_list = my_list[:]
print("Copia de la lista:", copy_list)

# 2. Crear lista sin elementos repetidos
unique_list = []

for number in my_list:
    if number not in unique_list:
        unique_list.append(number)

print("Lista sin repetidos:", unique_list)

# 3. Usar rebanadas
print("Primeros 3 elementos:", unique_list[:3])
print("Desde el índice 2 hasta el final:", unique_list[2:])

# 4. Verificar si un número está en la lista
if 6 in unique_list:
    print("El número 6 está en la lista")

# 5. Eliminar una parte de la lista
del unique_list[0:1]

print("Lista después de eliminar una rebanada:", unique_list)
