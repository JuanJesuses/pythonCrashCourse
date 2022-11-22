def describe_pet(pet_name, animal_type='perro'):
    """Muestra información acerca de una mascota."""
    print(f"\nTengo un {animal_type}.")
    print(f"Mi {animal_type} se llama {pet_name.title()}.")

describe_pet(pet_name='nuble')

describe_pet(pet_name='harry', animal_type='hamster')

# Un perro llamado Willie.
describe_pet('willie')
describe_pet(pet_name='willie')

# Un hamster llamado Harry.
describe_pet('harry', 'hámster')
describe_pet(pet_name='harry', animal_type='hámster')
describe_pet(animal_type='hámster', pet_name='harry')