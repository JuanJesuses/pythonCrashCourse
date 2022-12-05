# Empieza con tu trabajo del ejercicio 8-10.
# Llama a la función send_messages() con una copia de la lista de mensajes.
# Después de llamar a la función, imprime ambas listas para mostrar que la lista original ha conservado sus mensajes.

def send_messages(mensajes, mensajes_enviados):
    while mensajes:
        enviado = mensajes.pop()
        print(f"Se ha enviado el mensaje: ", enviado)
        mensajes_enviados.append(enviado)

def imprimir_mensajes(mensajes, mensajes_enviados):
    print(mensajes)
    print(mensajes_enviados)

mensajes = ['Hola qué tal', 'Mañana salimos', '¿Cómo lo llevas con Python?', 'Python mola']
mensajes_enviados = []

send_messages(mensajes[:], mensajes_enviados)
imprimir_mensajes(mensajes, mensajes_enviados)