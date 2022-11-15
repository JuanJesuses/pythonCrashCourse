# Haz una lista de los primeros 10 cubos (eso es, el cubo de cada entero desde 1 hasta 10)
# y utiliza un bucle para imprimir el valor de cada cubo.

cubes = []
for i in range(1, 11):
    print(i**3)
    cubes.append(i**3)

print(cubes)