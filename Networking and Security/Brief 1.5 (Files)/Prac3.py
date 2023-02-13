name = input("Guest Name: ")
with open("Guest.txt",'w') as file_object:
    file_object.write(name)