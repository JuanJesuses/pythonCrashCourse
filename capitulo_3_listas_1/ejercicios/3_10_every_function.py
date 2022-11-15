lista = ['richard stallman', 'alan turing', 'stephen hawking', 'linus torvalds', 'sheldon cooper']

# print()
print(lista)
# indice[]
print(lista[3])
# title()
print(f'{lista[0].title()} es un tipo que aboga por el software libre.')
# indice[-1] – Último elemento
print('El último elemento de la lista es', lista[-1].title())
# indice[i] = ‘loquesea’ – Modifcar elementos
lista[-1] = 'Neil DeGrass Tyson'
print(lista[-1])
# list.append() - Añadir al final
lista.append('Michio Kaiko')
print(lista)
# list.insert(posicion, ‘elemento’)
lista.insert(3, 'Ada Lovelace')
print(lista[3])
print(lista)
# del list[i] – Eliminar elemento de la lista en la posición i
lista.append('sheldon cooper')
del lista[-1]
print(lista)
# lista.pop() - Eliminar usando el valor eliminado
lista.append('sheldon cooper')
ficcion = lista.pop()
print(f'El elemento elminado es {ficcion}, que es unpersonaje de ficción.')
# list.remove[‘nombreDeElemento’]
lista.append('sheldon cooper')
print(lista)
lista.remove('sheldon cooper')
print(lista)
# list.sort() - ordenar permanentemente
lista.sort()
print(lista)
# reverse=True – ordenar a la inversa
lista.sort(reverse=True)
print(lista)
# sorted(list) – ordenar temporalemente
print(sorted(lista))
print(lista)
# list.reverse() - ordenar a la inversa permanentemente
lista.reverse()
print(lista)
# len(list) – longitud de la lista
print('La longitud de la lista es de ', len(lista), 'elementos.')