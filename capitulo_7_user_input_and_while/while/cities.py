prompt = "\nPor favor, introduce el nombre de la ciudad que has visitado: "
prompt += "\n(Introduce 'quit' cuando hayas acabado.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"Me gustaría ir a {city.title()}")