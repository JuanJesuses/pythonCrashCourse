# Creamos una calculadora sencilla que sólo hace divisiones:

print("Dame dos números y los dividiré.")
print("Introduce 'q' para terminar.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)