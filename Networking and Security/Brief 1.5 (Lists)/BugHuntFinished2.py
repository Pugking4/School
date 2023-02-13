different_thingos = [1, 2, 3, 4, 5]
for i in different_thingos: 
  if i == 2:
    different_thingos.remove(different_thingos[i-1])
print(different_thingos)