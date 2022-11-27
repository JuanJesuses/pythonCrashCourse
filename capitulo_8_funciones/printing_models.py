# Comienza con algunos diseños que necesitan ser impresos
unprinted_desings = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulta la impresión de cada diseño hasta que no quede ninguno.
# Mueve cada diseño a comleted_models después de imprimirlo.
while unprinted_desings:
    current_desing = unprinted_desings.pop()
    print(f"Printing model: {current_desing}")
    completed_models.append(current_desing)

# Muestra todos los modelos completados
print("\nLos siguientes modelos han sido impresos: ")
for completed_model in completed_models:
    print(completed_model)