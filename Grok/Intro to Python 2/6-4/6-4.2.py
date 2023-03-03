from collections import Counter

temp_mas = []
master = []
count_dict = {}
count = 1
cap_sort = {}

with open("novel2.txt", 'r') as f:
  for lines in f:
    lines = lines.split()
    for words in lines:
      master.append(words)

#print(master)

for x in master:
  count = 1
  #print(x[0].isalnum())
  if x[0] == x[0].upper() and x[0].isalnum() == True:
    #print(x, "is capped")
    if x in count_dict:
      #print(x, "+")
      count = count_dict[x] + 1
    count_dict[x] = count

#print(count_dict)

"""
temperatures = {}
for city in count_dict:
  temp = count_dict[city]
  if temp in temperatures:
    temperatures[temp].append(city)
  else:
    temperatures[temp] = [city]

for temp in sorted(temperatures):
  for city in temperatures[temp]:
    print(temp, city)
"""

k = Counter(count_dict)
high = k.most_common(3)

for i in high:
  #print(" ".join(high[i]))
  #print(" ".join(i))
  print(i[1],i[0])
  #print(i)
