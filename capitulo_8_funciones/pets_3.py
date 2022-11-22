def describe_pet(animal_type, pet_name):
    """Muestra información acerca de una mascota."""
    print(f"\nTengo un {animal_type}.")
    print(f"Mi {animal_type} se llama {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')