# Empaqueta el código del ejercicio 10-6 en un bucle while para que el usuario pueda seguir introduciendo números
# incluso si comete un error e introduce texto en lugar de un número.

otro = 's'

while otro != 'n':

    num1 = input("Introduce el número 1: ")
    num2 = input("Introduce el número 2: ")

    try:
        total = int(num1) + int(num2)
        print(total)
    except ValueError:
        print("Sólo puedes introducir números, me cago en tu puta madre!!")

    otro = input("¿Quieres continuar (s/n)?: ")

