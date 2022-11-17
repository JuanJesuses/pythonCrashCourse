prompt = "\nDime algo y lo repetiré para tí: "
prompt += "\nIntroduce 'quit' para finalizar el programa. "

active = True

while active:
    message = input(prompt)

    if message == 'quit':
        active =  False
    else:
        print(message)
