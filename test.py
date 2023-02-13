def describe_pet(pet_name, animal_type="dog"):
    return f"I have a {animal_type}. My {animal_type}'s name is {pet_name}."

print(describe_pet(pet_name='sam'))
print(describe_pet(animal_type='cat', pet_name='kaylee'))
