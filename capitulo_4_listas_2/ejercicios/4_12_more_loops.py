# Escoge una versión de foods.py y escribe dos bucles for para imprimir cada lista de alimentos.
my_foods = ['pizza', 'falafel', 'carot cake', 'cannoli', 'ice cream']

for food in my_foods:
    print(food)

foods = [print(food) for food in my_foods] # Esto imprime los alimentos uno a uno
foods2 = [food for food in my_foods]

foods
print(foods2) # Esto imprime los alimentos como una lista.