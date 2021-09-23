#! usr/bin/env python3

nombre = int(input("Nombre : "))

#ex: 12345 = 1*10⁴ + 2*10³ + 3*10² + 4*10¹ + 5*10⁰

if (nombre < 0 or nombre == 0):
    print("Entrez une valeur supérieure à 0 (Entiers positifs)")
    nombre = int(input("\nNombre : "))

final = 0

while(nombre > 0):
    a = nombre % 10
    final = final*10 + a
    nombre = nombre // 10

print(final)
