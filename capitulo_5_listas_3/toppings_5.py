# Listas múltiples

available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f'Añadiendo {requested_topping} a tu pizza.')
    else:
        print(f'Lo sentimos, no tenemos {requested_topping}.')
print('\nTu pizza está terminada!')