import os
import re
_RE_COMBINE_WHITESPACE = re.compile(r"\s+")

with open("Misc\\Zeta.txt",encoding="utf8") as f:
    unformatted_data = f.read()


remove_list = ['(煌)",','-','(煌)','(星)']

for i in range(len(remove_list)):
	unformatted_data = unformatted_data.replace(remove_list[i],"")
#Not written by me
garbageNew = _RE_COMBINE_WHITESPACE.sub("|", unformatted_data).strip()
#
unformatted_list = []
unformatted_list = garbageNew.strip("|").split("|")
#Not written by me
index_dx = [i for i, x in enumerate(unformatted_list) if x == "DX"]
#
x = 0
with open("Misc\\zeta_final_temp.txt", 'w',encoding="utf8") as file_object1:
	for i in range(len(index_dx)):
		
		file_object1.write(f"{unformatted_list[x:index_dx[i]-3]}\n")
		x = index_dx[i]-3

y = 6
with open("Misc\\zeta_final.txt", 'w',encoding="utf8") as file_object_w, open("Misc\\zeta_final_temp.txt", 'r',encoding="utf8") as file_object_r:
	lines = file_object_r.readlines()
	#print(lines)
	for lines in lines:
		res = lines.strip('][').replace("'","").replace("\n","").replace("]","").split(', ')
		del res[y:-1]
		res = " ".join(res)
		file_object_w.write(f"{res}\n")
		#print(res)

#Not written by me
lines = []
with open("Misc\\zeta_final.txt", 'r',encoding="utf8") as fp:
    lines = fp.readlines()

with open("Misc\\zeta_final.txt", 'w',encoding="utf8") as fp:
    for number, line in enumerate(lines):
        if number not in [0]:
            fp.write(line)
#
os.remove("Misc\\zeta_final_temp.txt") 