# Almacena información acerca de la pizza pedida.

pizza = {'corteza' : 'delgada',
         'ingredientes' : ['champiñones', 'extra de queso']}

# Resume el pedido
print(f"Has pedido una pizza de corteza - {pizza['corteza']} "
      f"con los siguientes ingredientes: ")

for topping in pizza['ingredientes']:
    print("\t" + topping)