# Haz una lista de números desde uno a un millón y luego utiliza las funciones min() y max()
# para comprobar que tu lista empieza en uno y llega al millón. También us la función sum() para ver lo rápido
# que suma Python un millón de números.
lista_milion = []
for i in range(1, 1000001):
    lista_milion.append(i)

print(max(lista_milion))
print(min(lista_milion))
print(sum(lista_milion))


# Lo mismo con list comprehension
lista_milion_2 = [i for i in range(1, 1000001)]
print(max(lista_milion_2))
print(min(lista_milion_2))
print(sum(lista_milion_2))
