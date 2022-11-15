# Haz una lista de múltiplos de 3 desde el 3 hasta el 30. Utiliza un bucle para imprimir los números de tu lista.
threes = []
for i in range(1, 31):
    print(i*3)
    threes.append(i*3)

print(threes)

# lo mismo con list comprehension
threes_2 = [(i * 3) for i in range(1, 31)]
print(threes_2)