# Abre un fichero en blanco en tu editor de texto y escribe unas pocas líneas resumiendo que has aprendido de Python
# hasta ahora. Comienza cada línea con la frase In Python you can… Guarda el fichero como learning_python.txt
# en el mismo directorio que los ejercicios de este capítulo. Escribe un programa que lea el fichero e imprima
# lo que has escrito tres veces.
# Imprime el contenido una vez leyendo el archivo completo, una vez recorriéndolo con un bucle sobre el
# objeto de archivo y otra vez almacenando las líneas en una lista y trabajando con ellas fuera del bloque.

with open('learning_python.txt') as file_object:
    contents = file_object.read()

for i in range (3):
    print(contents)

print(f"Esta es la impresión de sólo una vez: \n{contents}") # Una vez leyendo el archivo completo.

filename = 'learning_python.txt'

print('Esta es la impresión recorriendo con un bucle el objeto de archivo: ')
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

with open(filename) as file_object:
    lines = file_object.readlines()

print("\nEsta es la impresión del archivo trabajando fuera del bloque with: \n")
for line in lines:
    print(line.strip())


