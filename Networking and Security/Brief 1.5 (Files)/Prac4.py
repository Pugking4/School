from datetime import datetime
name = "placeholder"
with open("guest_book.txt",'a') as file_object:
    while name != "":
        name = input("Guest Name: ")
        if name == "":
            break
        file_object.write(f"'{name}' visted at {datetime.now()}\n")