# Utilizando tu última clase Restaurant, almacénala en un módulo. Haz un archivo separado que importe Restaurant.
# Haz una instancia Restaurant y llama a un método de Restaurant que muestre que la sentencia
# import está funcionando adecuadamente.

from restaurant import Restaurant

restaurante1 = Restaurant('El Frijolito', 'Comida Mejicana')
restaurante1.number_served = 26
restaurante1.describe_restaurant()