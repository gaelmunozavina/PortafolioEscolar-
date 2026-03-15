beatles = []

print("Paso 1:", beatles)

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

print("Paso 2:", beatles)

for i in range(2):
    beatles.append(input("Nuevo miembro: "))

print("Paso 3:", beatles)

del beatles[3]
del beatles[3]

print("Paso 4:", beatles)

beatles.insert(0, "Ringo Starr")

print("Paso 5:", beatles)

print("Los Fav", len(beatles))
