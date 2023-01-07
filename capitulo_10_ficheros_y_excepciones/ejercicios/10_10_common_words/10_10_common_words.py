# Visita el proyecto (https://gutenberg.org/) y encuentra unos cuantos textos que te gusten para analizar.
# Descarga los archivos de texto de estas obras o copia el texto en bruto desde tu navegador a un archivo de texto
# en tu ordenador. Puedes usar el método count() para encontrar cuántas veces aparece una frase o una palabra
# en una cadena. Observa que convirtiendo la cadena a minúscula utilizando lower() captura todas las apariciones
# de la palabra que estás buscando independientemente de su formato.
# Escribe un programa que lea los ficheros que has encontrado en Project Gutenberg y determina cuántas veces
# aparece la palabra ‘the’ en cada texto.
# Esto será una aproximación, puesto que también contará palabras como ‘then’ y ‘there’.
# Intenta contar ‘the ‘, con un espacio en la cadena, y observa como se reduce el número de coincidencias.

def cuenta_the(filename):

    num_count = 0
    try:
        with open(filename) as file_object:
            prosas = file_object.readlines()
    except:
        pass

    for prosa in prosas:
        num_count = num_count + prosa.lower().count('the ')

    print(num_count)

filenames = ['fgol.txt', 'quijote.txt', 'romeo_julieta.txt', 'talltales.txt']

for filename in filenames:
    cuenta_the(filename)