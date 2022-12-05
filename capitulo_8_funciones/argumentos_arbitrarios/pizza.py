def make_pizza(size, *toppings):
    """" Resume la pizza que estamos a punto de hacer."""
    print(f"\nHaciendo una pizza de tamaño {size}-inch con los siguientes ingredientes: ")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')