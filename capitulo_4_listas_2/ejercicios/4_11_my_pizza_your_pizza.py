# Haz una copia de la lista de pizzas y llámala friend_pizzas

my_pizzas = ['margarita', 'cuatro quesos', 'diavola', 'calzone']
friend_pizzas = my_pizzas[:]

# 1. Añade una nueva pizza a la lista original.
my_pizzas.append('fugazza')

# 2. Añade una pizza diferente a la lista friend_pizzas.
friend_pizzas.append('mexican')

# 3. Comprueba que tienes dos listas separadas. Imprime el mensaje ‘Mis pizzas favoritas son: ‘,
# y luego utiliza un bucle for para imprimir la primera lista. Imprime el mensaje
# ‘Las pizzas favoritas de mi amigo son: ‘ y luego utiliza un bucle for para imprimir la segunda lista.
# Asegúrate de que cada nueva pizza se almacena en la lista apropiada.
print(my_pizzas)
print(friend_pizzas)

print('\nMis pizzas favortias son: ')
for pizza in my_pizzas:
    print(pizza)

print('\nLas pizzas favoritas de mi amigo son: ')
for pizza in friend_pizzas:
    print(pizza)