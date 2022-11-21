def describe_pet(animal_type, pet_name):
    """Muestra información acerca de una mascota."""
    print(f"\nTengo un {animal_type}.")
    print(f"Mi {animal_type} se llama {pet_name.title()}.")

describe_pet('harry', 'hamster')