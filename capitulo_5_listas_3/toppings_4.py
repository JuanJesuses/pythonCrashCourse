# Comprobar una lista no vacía

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f'Añadiendo {requested_topping}.')
    print('\nHemos terminado tu pizza!')
else:
    print('¿Estás seguro de que no quieres ingredientes?')