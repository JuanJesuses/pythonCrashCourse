my_foods = ['pizza', 'falafel', 'carot cake']
friend_foods = my_foods[:]

print('My favorite foods are: ')
print(my_foods)

print("\nMy friend's favorite foods are: ")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')

print('\nMy favorite foods are: ')
print(my_foods)

print("\nMy friend's favorite foods are: ")
print(friend_foods)

# Esto no funciona como queremos ahora mismo
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print('\nMy favorite foods are: ')
print(my_foods)