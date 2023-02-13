def describe_city(city,country):
    return f"{city} is in {country}."
cities = ["Canberra","Sydney","Adelaide","Helinski","Stockholm","Oslo"]
countries = ["Australia","Finland","Sweden","Norway"]
print(describe_city(cities[0],countries[0]))
print(describe_city(cities[1],countries[0]))
print(describe_city(cities[2],countries[0]))
print(describe_city(cities[3],countries[1]))
print(describe_city(cities[4],countries[2]))
print(describe_city(cities[5],countries[3]))