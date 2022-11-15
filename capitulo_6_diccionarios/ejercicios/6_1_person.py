# Usa un diccionario para almacenar información acerca de una persona que conozcas. Almacena su primer nombre,
# apellido, edad  la ciudad en la que vive. Podrías tener claves como first_name, last_name, age y city.
# Imprime cada parte de la información almacenada en el diccionario.

person = {
    'first_name' : 'juan cristóbal',
    'last_name' : 'lópez',
    'age' : 26,
    'city' : 'huércal city',
}

print(person)

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

# Lo mismo con get()
print(person.get('first_name'))
print(person.get('last_name'))
print(person.get('age'))
print(person.get('city'))
print(person.get('talla', 'Todavía no necesitas saber la talla.'))