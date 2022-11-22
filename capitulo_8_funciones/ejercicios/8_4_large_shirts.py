# Modifica la función make_shirt() para que las camisetas sean large por defecto con un mensaje en el que se lea
# I love Python. Haz una talla large y otra medium con el mensaje por defecto y una camiseta de cualquier talla
# con un mensaje diferente.

def make_shirt(message='I love Python', size='large'):
    """ Crea una camiseta con la talla y un mensaje impreso. """
    print(f"\nTalla: {size.title()}.")
    print(f"Impresión: {message}.")
    print(f"La camiseta fabricada es de talla {size} y lleva impreso el mensaje '{message}'.",)

make_shirt()
make_shirt(size='large')
make_shirt(size='medium')
make_shirt(size='smart', message='No importa qué estudies, practícalo!')