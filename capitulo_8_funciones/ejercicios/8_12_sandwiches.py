# Escribe una función que acepte una lista de elementos que una persona quiera en un sándwich.
# La función debe tener un parámetro que coleccione tantos elementos como proporcione la llamada a la función
# y debería imprimir un resumen del sándwich que se ha pedido.
# Llama a la función tres veces utilizando diferentes números de argumentos cada vez.

def making_sandwich(*toppings):
    """ Función que recibe ingredientes de un sandwich e imprime
        el sandwich que se ha pedido."""
    print("\nHa pedido un sandwich de: ")
    for topping in toppings:
        print(f"{topping.title()}.")

making_sandwich('queso', 'majón york')
making_sandwich('atún', 'huevo', 'mahonesa', 'lechuga')
making_sandwich('aceite', 'sal')