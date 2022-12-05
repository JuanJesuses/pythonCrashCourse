# Empieza con una copia de tu programa del ejercicio 8-9.
# Escribe una función llamada send_messages() que imprima cada mensaje de texto y mueva cada mensaje
# a una nueva lista llamada sent_messages a medida que se imprime. Después de llamar a la función,
# imprime ambas listas para asegurarte de que los mensajes se hayan movido correctamente.

def send_messages(mensajes, mensajes_enviados):
    while mensajes:
        enviados = mensajes.pop()
        print(f"Se ha enviado el mensaje: {enviados}.")
        mensajes_enviados.append(enviados)


def mostrar_enviados(mensajes_enviados):
    print("\nSe han enviado los siguientes mensajes: ")
    for enviado in mensajes_enviados:
        print(enviado)

mensajes = ['Hola qué tal', 'Mañana salimos', '¿Cómo lo llevas con Python?', 'Python mola']
mensajes_enviados = []

send_messages(mensajes, mensajes_enviados)
mostrar_enviados(mensajes_enviados)

mostrar_enviados(mensajes) # así comprobamos que la lista original ha quedado vacía por completo.

# ESTA VERSIÓN NO MOLA
"""
def send_messages(mess):
    '''Imprime los mensajes, los guarda en una nueva lista y vacía la anterior. '''
    copy_list = []
    while mess:
        for message in mess:
            print(message)
            copy_list.append(message)

    print('\nLista original:')
    print(mess)
    print("\nLista copia:")
    print(copy_list)

lista_mensaje = ['Hola qué tal', 'Mañana salimos', '¿Cómo lo llevas con Python?', 'Python mola']
send_messages(lista_mensaje)"""