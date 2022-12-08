# Escribe una función que almacene información sobre un coche en un diccionario.
# La función siempre debe recibir un fabricante y un nombre de modelo de coche.
# Debe aceptar un número arbitrario de palabras clave.
# Llama a la función con la información requerida con la información requerida y otros dos pares clave-valor
# como color o una función opcional. Tu función podría trabajar con una llamada como esta:

# car = make_car('subaru', 'outback', color='blue', tow_packages='True)

# Imprime el diccionario devuelto para asegurarte de que toda la información se ha almacenado correctamente.

def car(model, manufacturer, **modelo):
    """ Almacena información de un vehículo en un diccionario. """
    modelo['modelo'] = model
    modelo['fabricante'] = manufacturer

    return modelo


coche1 = car('Rodius', 'Ssang Yong', color='white', video=True)
coche2 = car('Primera', 'Nissan', color='blue', wheels='185/95')
coche3 = car('golf', 'volkswagen', color='black', assistant_direction=False)

print(coche1,"\n",coche2,"\n",coche3)
