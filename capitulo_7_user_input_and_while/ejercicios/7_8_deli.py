# Haz una lista llamada sandwich_orders y rellénala con nombres de varios sandwiches.
# Luego haz una lista vacía llamada finished_sandwiches. Recorre la lista de pedidos de sandwich
# e imprime un mensaje para cada pedido, como He hecho tu sandwich de atún.
# Cada sandwich hecho muévelo a la lista de sandwiches terminados. Después de hacer todos los sandwiches,
# imprime un mensaje que enumere cada sandwich que se hizo.

sandwich_orders = ['jamóm', 'jamon y queso', 'pastrami', 'choriso', 'mantequilla de cacahuete']
finished_sandwiches = []

for sandwich in sandwich_orders:
    print(f"He hecho tu sandwich de {sandwich}.")
    finished_sandwiches.append(sandwich)

print("\nHemos hecho varios sandwiches de: ")
for sandwich in finished_sandwiches:
    print(f"{sandwich.title()}")