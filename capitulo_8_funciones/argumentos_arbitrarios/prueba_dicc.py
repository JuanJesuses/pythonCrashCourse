# Esta prueba con el diccionario es para probar si admite claves pasadas de forma automática

diccionario = {}
diccionario2 = {}
claves = ['a', 'b', 'c', 'd', 'e']

def make_car(manufacturer, model, **kwargs):
    print(kwargs)

for i in range(5):
    diccionario[i] = i+2

print(diccionario)

for i in range(5):
    diccionario2[claves[i]] = str(i) + claves[i]

print(diccionario2)

car = make_car('subaru', 'outback', color='blue', tow_package=True)