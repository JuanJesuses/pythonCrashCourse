# Escribe una cadena if-elif-else que determine la etapa de la vida de una persona.
# Establece una variable para la edad y luego:

age = 24

# 1. Si la persona es menor de 2 años, imprime un mensaje que indique que esa persona es un bebé.
if age < 2:
    person = 'baby'
# 2. Si la persona tiene al menos 2 años pero menos de 4, imprime un mensaje que indique que esa persona
# es un niño pequeño.
elif age >= 2 and age < 4:
    person = 'toddler'
# 3. Si la persona tiene al menos 4 años pero menos de 13, imprime un mensaje que indique que esa persona es un chico.
elif age >= 4 and age < 13:
    person = 'kid'
# 4. Si la persona tiene al menos 13 años pero menos de 20, imprime un mensaje que indique que esa persona
# es un adolescente.
elif age >= 13 and age < 20:
    person = 'teenager'
# 5. Si la persona tiene al menos 20 años pero menos de 65, imprime un mensaje que indique que esa persona es un adulto.
elif age >= 20 and age < 65:
    person = 'adult'
# 6. Si la persona tiene 65 años o más, imprime un mensaje que indique que esa persona es mayor.
else:
    person = 'elder'

print(f'Eres un {person.title()}.')