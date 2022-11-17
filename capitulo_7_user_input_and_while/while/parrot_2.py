prompt = "\nDime algo y lo repetiré para tí: "
prompt += "\nIntroduce 'quit' para finalizar el programa. "

message = ""

while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)