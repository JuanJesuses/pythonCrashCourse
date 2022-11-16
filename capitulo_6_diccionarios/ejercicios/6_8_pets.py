# Haz varios diccionarios donde cada uno represente a una mascota diferente. En cada uno incluye el tipo de animal
# y el nombre del propietario. Almacena esos diccionarios en una lista llamada pets.
# A continuación, mientras recorres la lista imprime.

pet_1 = {
    'tipo' : 'perrete',
    'prop' : 'michael',
}

pet_2 = {
    'tipo' : 'gatete',
    'prop' : 'rachel',
}

pet_3 = {
    'tipo' : 'cobaya',
    'prop' : 'sanders',
}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f"Esto es un {pet['tipo']} y su dueño es {pet['prop'].title()}.")