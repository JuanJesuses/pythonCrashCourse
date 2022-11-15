''' Muestra por pantalla el cuadrado de los numeros del 1 al 10.

squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)

print(squares) '''

# versión reducida del código anterior
squares = []

for value in range(1, 11):
    squares.append(value**2)
print(squares)

digitos = []

for i in range(1, 11):
    digitos.append(i)

print(min(digitos))
print(max(digitos))
print(sum(digitos))

# List comprhension
squares2 = [value**2 for value in range(1, 11)]
print(f'List comprehension {squares2}')

elemento = [(i+i) for i in range(23)]
print(f'Esta expresión está hecha con List comprehension y queda así: {elemento}')

letras = 'camaradería'
elemento2 = [('@' + i) for i in letras]
print(f'Esto también es list copmrehension y queda así: \n{elemento2}.')