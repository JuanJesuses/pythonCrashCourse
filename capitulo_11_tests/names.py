from name_function import get_formatted_name

print("Introduce 'q' en cualquier momento para terminar.")
while True:
    first = input("\nDime tu nombre: ")
    if first == 'q':
        break
    last = input("Dime tu apellido: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNombre bien formateado: {formatted_name}")