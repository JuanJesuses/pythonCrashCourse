''' Piensa al menos cinco lugares en el mundo que te gustaría visitar: '''

# Almacena la localización en una lista. Asegúrate de que la lista no está en orden alfabético.
listOfPlaces = ['New York', 'Helsinki', 'Oimiakón', 'Los Ángeles', 'Moscow']

# Imprime la lista en su orden original. No te preocupes por imprimir la lista ordenadamente,
# simplemente imprímelo como una lista de Python sin procesar.
print(listOfPlaces)

# Utiliza sorted() para imprimir tu lista en orden alfabético sin modificar la lista actual.
print(sorted(listOfPlaces))

# Muestra que tu lista permanece en su orden original imprimiéndola.
print(listOfPlaces)

# Utiliza sorted para imprimir tu lista en orden alfabético inverso sin cambiar la ordenación de la lista original.
sorted(listOfPlaces)
print(listOfPlaces.reverse())
print(listOfPlaces)

# Muestra que tu lista todavía se encuentra en el orden original imprimiéndola.
print(listOfPlaces)

# Utiliza reverse() para cambiar el orden de tu lista. Imprímela para mostrar que el orden ha cambiado.
listOfPlaces.reverse()
print(listOfPlaces)

# Utiliza reverse() para cambiar de nuevo el orden de la lista. Imprime la lista para mostrar
# que ha vuelto a su orden original.
listOfPlaces.reverse()
print(listOfPlaces)

# Utiliza sort() para cambiar la lista que está almacenada en orden alfabético.
# Imprime la lista para mostrar que el orden ha cambiado.
listOfPlaces.sort()
print(listOfPlaces)

# Utiliza sort() para cambiar la lista y almacenarla en orden alfabético inverso.
# Imprime la lista para mostrar que el orden ha cambiado.
listOfPlaces.sort()
listOfPlaces.reverse()
print(listOfPlaces)
