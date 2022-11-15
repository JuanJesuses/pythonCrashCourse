# 5-2. More conditional tests

# 1. Un test de igualdad y no igualdad con cadenas.
cadena1 = 'prueba'
print(cadena1 != 'elemento')
print(cadena1 == 'prueba')
print(cadena1 != 'prueba')

# 2. Un test utilizando el método lower().
jusegos = ['B4Blood', 'diablo_II', 'silent hill', 'resident evil']
print(f'El jusego {jusegos[0]} == b4blood?')
print(jusegos[0].title() == 'b4blood')
print(f'Pero el jusego {jusegos[0]} == b4blood si es True')
print(jusegos[0].lower() == 'b4blood')

# 3. Test numéricos que incluyan igualdad y no igualdad,
# mayor que, mayor o igual que y menor que y menor o igual que.
numeros = [1, 3, 5, 7, 8, 10, 12, 14, 16]
print(numeros[3] == 7) # Igualdad
print(numeros[0] != numeros[4]) # No igualdad
print(numeros[2] > numeros[1]) # Mayor que
print(numeros[2] >= 5) # Mayor o igual que
print(numeros[8] < 16) # Menor que
print(numeros[7] <= 14) # Menor o igual que

# 4. Test utilizando las palabras clave and y or.
print('True or False es True')
print(True or False)
print('True and False es False')
print(True and False)

# 5. Test si un elemento está en una lista.
print('Juegos en una máquina de jusegos:')
print('B4Blood' in jusegos)
print('Sea of thieves' in jusegos)

# 6. Test si un elemento no está en una lista.
print('Jusegos en la otra máquina de jusegos:')
print('diablo_II' not in jusegos)
print('Sea of Thieves' not in jusegos)

