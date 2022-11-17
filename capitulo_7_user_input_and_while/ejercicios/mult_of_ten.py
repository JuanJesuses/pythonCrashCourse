# Pregunta al usuario por un número y dile so el número es múltiplo de 10 o no.

number = int(input('Introduce un número para saber si es múltiplo de 10 o no: '))

if number % 10 == 0:
    print(f"El número {number} es múltiplo de 10.")
else:
    print(f"El número {number} NO es múltiplo de 10.")