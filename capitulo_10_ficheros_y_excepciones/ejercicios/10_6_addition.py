# Un problema habitual cuando se solicita la inserción de datos numéricos, ocurre cuando la gente proporciona
# texto en lugar de números. Cuando intentas convertir la entrada a un int, obtendrás un ValueError.
# Escribe un programa que pida dos números. Súmalos e imprime el resultado.
# Captura el ValueError si cualquiera de los valores de entrada no es un número e imprime un mensaje de error amigable.
# Prueba tu programa introduciendo dos números y luego introduciendo algo de texto en lugar de un número.

num1 = input("Introduce el número 1: ")
num2 = input("Introduce el número 2: ")

try:
    total = int(num1) + int(num2)
    print(total)
except ValueError:
    print("Sólo puedes introducir números, me cago en tu puta madre!!")