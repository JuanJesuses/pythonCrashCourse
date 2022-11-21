# Escribe un programa que encueste a usuarios sobre sus vacaciones de ensueño.
# Escribe un mensaje similar a Si pudieras visitar un lugar en el mundo,
# ¿dónde te gustaría ir? Incluye un bloque de código que imprima los resultados de la encuesta.

respuestas = {}
active = True

while active:
    nombre = input('\n¿Cuál es tu nombre?: ')
    viaje = input('¿Si pudieras visitar un lugar en el mundo, cuál sería?: ')

    respuestas[nombre] = viaje

    repetición = input('¿Quieres preguntar a otra persona(si/no)?: ')
    if repetición == 'no':
        active = False

print('\n--- Resultados de la Encuesta ---')
for nombre, lugar in respuestas.items():
    print(f"Hola {nombre}, a  tí te gustaría viajar a {lugar}")
