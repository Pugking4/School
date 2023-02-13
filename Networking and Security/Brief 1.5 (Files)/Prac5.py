from datetime import datetime
name = "placeholder"
with open("poll.txt",'a') as file_object:
    while name != "":
        name = input("Why do you like programming? ")
        if name == "":
            break
        file_object.write(f"'{name}' logged at {datetime.now()}\n")