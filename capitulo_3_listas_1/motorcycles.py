motorcycles = ['honda', 'suzuki', 'yamaha']
print(motorcycles)

"""
motorcycles[0] = 'Ducati'
print(motorcycles)"""

# Añadiendo elementos
motorcycles.append('ducati')
print(motorcycles)

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('yuzuki')

print(motorcycles)

motorcycles.insert(2, 'husqvarna')
print(motorcycles)

del motorcycles[5]

print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

print(f'El valor eliminado ha sido la moto {popped_motorcycle}.')

first_owned = motorcycles.pop(0)
print(f'The first motorcycle i owned was a {first_owned.title()}.')

print(motorcycles)
motorcycles.remove('yamaha')
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f'La {too_expensive.title()} es demasiado cara para mí.')