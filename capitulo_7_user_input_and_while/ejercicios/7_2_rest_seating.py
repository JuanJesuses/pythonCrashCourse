# Escribe un programa que pregunte al usuario cuántas personas serán en el grupo de la cena.
# Si la respuesta es más de 8, imprime un mensaje diciendo que tendrán que esperar una mesa libre,
# en caso contrario infórmales que hay mesa disponible.

persons = int(input('¿Cuántos sois para cenar?: '))

if persons > 8:
    print("\nTendréis que esperar a que haya una mesa disponible.")
else:
    print('Enhorabuena, podéis pasar a hincharos las pelotas!')