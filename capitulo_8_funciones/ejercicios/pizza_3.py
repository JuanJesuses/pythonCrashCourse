def make_pizza(size, *toppings):
    """" Resume la pizza que estamos a punto de hacer."""
    print(f"\nHaciendo una pizza de tamaño {size}-inch con los siguientes ingredientes: ")
    for topping in toppings:
        print(f"- {topping}")

def add_pizza(pizza):
    """ Guarda las pizzas en una lista """
    pedidos = []
    print("\nEsta pizza lleva:")
    for pedido in pizza:
        pedidos.append(pedido)
        print(f" - {pedido}")

def muestra_pedido(pedido):
    return pedido