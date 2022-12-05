# Haz una lista que contenga una serie de mensajes de texto cortos.
# Pasa la lista a una función llamada show_messages(), que imprima cada mensaje de texto.

def show_messages(mess):
    """ Muestra los mensajes recibidos por parámetro. """
    for message in mess:
        print(message)

lista_mensaje = ['Hola qué tal', 'Mañana salimos', '¿Cómo lo llevas con Python?', 'Python mola']

show_messages(lista_mensaje)