# Utiliza la lista  sandwich_orders del ejercicio 7-8,  asegúrate de que el sandwich ‘pastrami’ aparece en la lista
# al menos tres veces. Añade código cerca del principio de tu programa para imprimir un mensaje diciendo que
# la tienda de delicatessen se ha quedado sin pastrami y luego utiliza un bucle while para eliminar
# todas las coincidencias de ‘sandwich_orders’. Asegúrate de que los sandwiches de pastrami no se añadan
# a finished_sandwiches.

sandwich_orders = ['pastrami', 'choriso', 'jamóm', 'jamon y queso', 'pastrami', 'choriso', 'mantequilla de cacahuete',
                   'pastrami', 'queso', 'atún']
finished_sandwiches = []

print("Lo sentimos, nos hemos quedado sin pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

for sandwich in sandwich_orders:
    print(f"Estamos haciendo tu sandwich de {sandwich}.")
    finished_sandwiches.append(sandwich)

print(finished_sandwiches)


