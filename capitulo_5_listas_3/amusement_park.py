# Determinar el grupo de edad de una persona para saber cuánto le costará la entrada al parque de atracciones.

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f'Tu entrada cuesta {price} euros.')
'''
if age < 4:
    print('Tu entrada tienen coste 0.')
elif age < 18:
    print('Tu entrada tiene un coste de 25 Euros.')
else:
    print('Tu entrada tiene un coste de 40 Euros.')'''