with open("learning_python.txt",'r') as file_object:
    lines = file_object.readlines()
    for lines in lines:
        print(lines.rstrip())