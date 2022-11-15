# Limpia el código del ejercicio 6-3 reemplazando tus series de llamadas a print()
# con un bucle que recorra las claves y los valores del diccionario.
# Cuando estés seguro de que tu bucle funciona, añade cinco términos Python más a tu diccionario.
# Cuando ejecutes tu programa de nuevo, esas nuevas palabras y significados deberían ser incluidas
# automáticamente en la salida.

glossary = {
    'variable' : 'is like a box you can store values in.',
    'string' : 'is a series of characters.',
    'comments' : 'allows you to write notes that interpreter ignores.',
    'list' : 'a collection of items in a particular order.',
    'boolean' : 'is a data type wich value is either True or False.',
    'dictionary' : 'a collection data type.',
    'if' : 'conditional instruction wich look for True or False values.',
    'for' : 'type of loop who loops through the sentences.',
    'key-value pair' : 'a way to store data in dictionaries.',
    'editor' : 'software who helps you to write code.',
}

for palabra in glossary:
    print(f'{palabra.title()},', glossary[palabra])

print('\n')

for palabra in glossary:
    print(f'{palabra.title()}:\n\t'
          ,glossary[palabra])