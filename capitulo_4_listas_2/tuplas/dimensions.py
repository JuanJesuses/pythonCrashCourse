# Dimensiones de un rectángulo
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# tupla de un sólo elemento. Debe llevar una coma al final
my_tuple = (3,)
print(dimensions)
print(my_tuple)

# Las tuplas son inmutables. La siguiente sentencia genera un Type Error
# dimensions[0] = 250

for dimension in dimensions:
    print(dimension)

print('Dimensiones originales: ')
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print('\nDimesiones modificadas: ')
for dimension in dimensions:
    print(dimension)