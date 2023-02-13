def formatted_name(given_name,family_name,middle_name=""):
        return f"{family_name}, {given_name} {middle_name}".title()

print(formatted_name(given_name="augusta", middle_name="ada", family_name="lovelace"))
print(formatted_name(given_name="bob", family_name="bobbington"))
print(formatted_name(given_name="charles", family_name="babbage"))