# Los números ordinales indican su posición en una lista como primero o segundo.
# La mayoría de los números ordinales terminan en th, excepto 1, 2 y 3 (first, second, third).

# 1. Almacena números del 1 al 9 en una lista.
# 2. Recorre la lista.
# 3. Utiliza una cadena if-elif-else dentro del bucle para imprimir la terminación ordinal apropiada para cada número.
# Tu salida debería leer “1st 2nd 3rd 4th 5th 6th 7th 8th 9th” y cada resultado debería está en una línea separada.

ordinal_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

for number in ordinal_numbers:
    if number == '1':
        print(f'{number}' + 'st')
    elif number == '2':
        print(f'{number}' + 'nd')
    elif number == '3':
        print(f'{number}' + 'rd')
    else:
        print(f'{number}' + 'th')