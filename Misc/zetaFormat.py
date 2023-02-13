import re

_RE_COMBINE_WHITESPACE = re.compile(r"\s+")

with open("Misc\\Zeta.txt",encoding="utf8") as f:
    unformatted_data = f.read()

remove_list = ['(煌)",','-','(煌)']

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
with open("zeta_final.txt", 'w',encoding="utf8") as file_object:
	for i in range(len(index_dx)):
		file_object.write(f"{unformatted_list[x:index_dx[i]-3]}\n")
		x = index_dx[i]-3

#Not written by me
lines = []
with open("zeta_final.txt", 'r',encoding="utf8") as fp:
    lines = fp.readlines()

with open("zeta_final.txt", 'w',encoding="utf8") as fp:
    for number, line in enumerate(lines):
        if number not in [0]:
            fp.write(line)
#

with open("zeta_final.txt", 'r',encoding="utf8") as file_object:
	for lines in file_object:
		lines = lines.replace('[',"")
		lines = lines.replace(']',"")
		lines = lines.replace("'","")
		lines = lines.replace(" ","")
		lines = lines.replace("_"," ")
		print(lines.rstrip())