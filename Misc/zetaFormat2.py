import os

old_line = []
new_line = []
final_line = ""
os.remove("Misc\\zeta_final2.txt") 

with open("Misc\\zeta_final.txt",encoding="utf8") as file_object:
    unformatted_data = file_object.readlines()
    for lines in unformatted_data:
        lines = lines.replace("\n","")
        #print(lines)
        new_line = []
        old_line = lines.split(" ")
        #print(old_line)
        new_line.append(old_line[0])
        new_line.append(old_line[2])
        new_line.append(old_line[3])
        new_line.append(old_line[4])
        new_line.append(old_line[5])
        new_line.append(old_line[6])
        new_line.append(old_line[1])
        new_line = ",".join(new_line)
        new_line = new_line.replace("_"," ")
        final_line = new_line + "\n"
        #print(final_line)
        with open("Misc\\zeta_final2.txt",'a',encoding="utf8") as file_object_w:
            file_object_w.write(final_line)



#print(old_line)
