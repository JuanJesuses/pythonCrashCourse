# Hacer una lista de los ingredientes que ha pedido el cliente y usar un bucle para informar
# de cada ingrediente añadido a la pizza.

requested_toppings = ['champiñones', 'pimientos verdes', 'extra de queso']

for requested_topping in requested_toppings:
    if requested_topping == 'pimientos verdes':
        print('Lo sentimos, nos hemos quedado sin pimientos verdes')
    else:
        print(f'Añadiendo {requested_topping}.')

print('\nSe terminado de hacer tu pizza!')