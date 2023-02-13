with open("learning_python.txt",'r') as file_object:
    lines = file_object.readlines()
    
    for lines in lines:
        lines =str(lines.replace("Python","C++"))
        print(lines.rstrip())