# Almacena cinco comidas de un restaurante en una tupla
menus = ('entrantes', 'arroz y fideos', 'tepanyaki', 'uramaki', 'nigri sushi')

# 1. Utiliza un bucle para imprimir cada comida que ofrece el restaurante.
for menu in menus:
    print(menu)

# Apartado 1 con list comprehension
menu2 = [menu for menu in menus]
print(menu2)

menu3 = [print(menu) for menu in menus]
menu3

# 2. Intenta modificar uno de los elementos, y asegúrate de que Python rechace el cambio.
#menus[3] = 'dorayaki'

# 3. El restaurante cambia su menú, reemplaza dos elementos con comida diferente.
# Añade una línea que reescriba la tupla y utiliza un bucle for para imprimir cada uno
# de los elementos del menú revisado.
menus = ('entrantes', 'fideuá', 'tepanyaki', 'dorayaki', 'nigri sushi')
for menu in menus:
    print(menu)

# Apartado 3 con list comprehension
nuevo_menu = [menu for menu in menus]
print(nuevo_menu)

nuevo_menu2 = [print(menu) for menu in menus]
nuevo_menu2