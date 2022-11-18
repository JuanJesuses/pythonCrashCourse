# Un cine tiene diferentes precios de entrada dependiendo de la edad de las personas.
# Si una persona es menor de 3 años, la entrada es gratis; si tiene entre 3 y 12 cuesta 10 euros;
# y para los mayores de 12, 15 euros. Escribe un bucle que pregunte la edad al usuario
# y luego infórmales del coste de su entrada.

while True:

    edad = int(input('Introduzca su edad (0 para terminar): '))

    if edad == 0:
        break

    if edad > 0 and edad < 3:
        print("Su entrada gratis.")
    elif edad >= 3 and edad < 12:
        print("Su entrada cuesta 10 Euros.")
    elif edad >= 12:
        print("Su entrada cuesta 15 Euros.")
