import re

_RE_COMBINE_WHITESPACE = re.compile(r"\s+")

with open("Misc\\Zeta.txt",encoding="utf8") as f:
    garbage = f.read()
#garbage.splitlines()

#or i in garbage:
#print(garbage)

#print(garbage)
#garbageNew = ""
#garbageNew = garbageNew.join(garbage.split())
#print (garbageNew)

garbageNew = _RE_COMBINE_WHITESPACE.sub("|", garbage).strip()
#print(garbageNew)

garbage_list = []
garbage_list = garbageNew.strip("|").split("|")

remove = ['(煌)",','-','(煌)']

removeCount = 0
for i in range(len(remove)):
	removeCount = removeCount + garbage.count(remove[i])
#removeCount = garbage.count(remove[0])
#removeCount = removeCount + garbage.count(remove[1])

z = 0
print(f"{removeCount} remove")
while z < removeCount:
	for i in range(len(remove)):
		if remove[i] in garbage_list:
			garbage_list.remove(remove[i])
	z += 1

print(garbage_list)
u = 2
for i in range(len(garbage_list)//19):
	#print(f"test {u}")
	#print(garbage_list[u])
	temp = garbage_list.index("DX")
	res = garbage_list[u:temp]
	garbage_list[u : temp] = [' '.join(garbage_list[u : temp])]
	u += 19

#garbage_list[2 : temp] = [' '.join(garbage_list[2 : temp])]




#garbage_list.remove('(煌)",')
#garbage_list.remove('-')
#print(res)
#print(garbage_list)
print(len(garbage_list))
print(garbage_list.count("FESTiVAL"))
print(garbage_list.count("Splash+"))

count = 0
x = 0
y = 19

while count < 44:
	print(garbage_list[x:y]) 
	#print("test")
	x += 19
	y += 19
	count += 1