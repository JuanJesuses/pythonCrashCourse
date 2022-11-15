# Function range()

for value in range(1, 5): # Esto imprime de 1 a 4 porque Python para cuando llega al valor del segundo argumento.
    print(value)

for value in range(6): # Si solo le proporcionamos un argumento, comienza a imprimir desde 0. Esto imprime de 0 a 5.
    print(value)

# Utilizar una lista de números.
numbers = list(range(1, 6))
print(numbers)