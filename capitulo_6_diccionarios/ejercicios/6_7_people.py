# Comienza con el programa que escribiste en el ejercicio 6-1. Haz dos nuevos diccionarios representando
# a diferentes personas y almacena los tres diccionarios en una lista llamada people.
# Recorre tu lista de personas. A medida que recorras la lista, imprime.

person_1 = {
    'first_name' : 'richard',
    'last_name' : 'stallman',
    'age' : 69,
    'city' : 'new york',
}

person_2 = {
    'first_name' : 'guido',
    'last_name' : 'van rossum',
    'age' : 66,
    'city' : 'amsterdam',
}

person_3 = {
    'first_name' : 'linus',
    'last_name' : 'torvalds',
    'age' : 53,
    'city' : 'portland',
}

people = [person_1, person_2, person_3]

for person in people:
    print(f"\nNombre: {person['first_name'].title()}")
    print(f"Apellidos: {person['last_name'].title()}")
    print(f"Edad: {person['age']}")
    print(f"Localidad: {person['city'].title()}")

