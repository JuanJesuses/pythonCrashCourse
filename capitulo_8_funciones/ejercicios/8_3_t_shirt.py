# Escribe una función llamada make_shirt() que acepte una talla y el texto de un mensaje
# que debe ser impreso en la camiseta. La función podría imprimir una frase resumiendo la talla de la camiseta
# y el mensaje impreso en ella. Llama a la función usando argumentos posicionales para hacer la camiseta.
# Llama a la función una segunda vez utilizando argumentos de palabras clave.

def make_shirt(size, message):
    """ Crea una camiseta con la talla y un mensaje impreso. """
    print(f"\nTalla: {size.title()}.")
    print(f"Impresión: {message}.")
    print(f"La camiseta fabricada es de talla {size} y lleva impreso el mensaje '{message}'.",)

make_shirt('medium', 'Estoy aprendiendo Python')
make_shirt(size='large', message='¿Tú que lenguaje estás aprendiendo?')
