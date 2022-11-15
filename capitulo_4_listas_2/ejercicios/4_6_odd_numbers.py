# Utiliza el tercer argumento de la función range() para hacer una lista de números impares desde el 1 al 20.
# Utiliza un bucle para imprimir cada número.
odd_number = []
for i in range(1, 21, 2):
    print(i)
    odd_number.append(i)
print(odd_number)

# Lo mismo con list comprhension
odd_numbers_2 = [i for i in range(1, 21, 2)]
print(odd_numbers_2)