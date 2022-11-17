number = input("Introduce un número y te diré si es par o impar: ")
number = int(number)

if number % 2 == 0:
    print(f"\nEl número {number} es par.")
else:
    print(f"\El número {number} es impar.")