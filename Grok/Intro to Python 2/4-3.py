eng_list = input("Line: ").split()

#eng_list = ["English", "Tim", "Nicky", "James", "Tara", "John", "Ben"]

del eng_list[0]
other_input = input("Line: ")
eng_set = set(eng_list)
in_set = set()

final_set = set()

master = []
temp_list = []


#master = [["Nicky", "Tim"],["Tim", "John"]]


while other_input:
    temp_list = other_input.split()
    del temp_list[0]
    master.append(temp_list)
    other_input = input("Line: ")

for i in master:
    other_set = set(i)
    for x in other_set:
#        print("testing",x)
        if x in eng_set:
            in_set.add(x)
#            print(x)

final_set = eng_set - in_set
#print(f"{final_set} = {eng_list} - {in_set}")

if final_set != set():
    for i in final_set:
        print(f"{i} is monolingual.")
else:
    print("Everyone is multilingual!")
#for i in master:
#    for x in other_set:
#        if x not in not_set:
#            add

#print(master)
#print(final_set)