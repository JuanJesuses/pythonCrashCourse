# Pon las funciones del ejemplo printing_models.py en un archivo separado llamado printing_functions.py.
# Escribe una sentencia import en la parte superior de printing_models.py,
# y modifica el archivo para utilizar las funciones importadas.

import printing_functions

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models(completed_models)