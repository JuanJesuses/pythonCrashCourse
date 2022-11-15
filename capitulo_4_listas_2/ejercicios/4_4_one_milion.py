# Haz una lista de números desde uno a un millón y utiliza un bucle para imprimirlos.
for i in range(1000001):
    print(i)

# Mismo ejercicio con list comprehension
lista_millon = [i for i in range(1, 1000001)]
print(lista_millon)