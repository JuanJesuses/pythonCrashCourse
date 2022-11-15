# Un diccionario Python se puede usar para modelar un diccionario actual, sin embargo,
# para evitar confusión, llamémosle glosario.

# 1. Piensa cinco palabras de programación que hayas aprendido en los capítulos anteriores.
# Usa esas palabras como claves en tu glosario y almacena sus significados como valores.

# 2. Imprime cada palabra y su significado con un formato de salida claro.
# Puedes imprimir la palabra seguida de una coma y después su significado,
# o imprimir la palabra en una línea y luego imprimir su significado indentado en una segunda línea.
# Utiliza el carácter newline(\n) para insertar una línea en blanco entre cada par palabra-significado en la salida.

glossary = {
    'variable' : 'is like a box you can store values in.',
    'string' : 'is a series of characters.',
    'comments' : 'allows you to write notes that interpreter ignores.',
    'list' : 'a collection of items in a particular order.',
    'boolean' : 'is a data type wich value is either True or False.',
}
# Versión 1
"""
print(f"Variable, {glossary['variable']}")
print(f"\nString, {glossary['string']}")
print(f"\nComments, {glossary['comments']}")
print(f"\nList, {glossary['list']}")
print(f"\nBoolean, {glossary['boolean']}")"""

# Versión 2
print(f"Variable:\n\t {glossary['variable']}")
print(f"\nString:\n\t{glossary['string']}")
print(f"\nComments:\n\t{glossary['comments']}")
print(f"\nList:\n\t{glossary['list']}")
print(f"\nBoolean:\n\t{glossary['boolean']}")