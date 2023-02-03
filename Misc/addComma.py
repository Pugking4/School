def addComma(filename):
    filename = input("Filename: ") #User inputs filename for text document they want commas added to
    filepath = f"Misc\\addCommaTXT\\{filename}" #Specifies the file path "Misc\addCommaTXT" for opening files in
    with open(filepath,encoding="utf8") as f: #Opens the user filepath as a "file" from the "with" statement
        lines = f.read().splitlines() #Stores the read data from ".read()" and ".splitlines()" splits the string from every line break (/n) into a list
#Closes the file path as "with" statement automatically closes the file when it ends

    with open(filepath, "w",encoding="utf8") as f: #Opens the user filepath as a "file" with the parameter "write" from the "with" statement
        for line in lines: #Repeats for however many line breaks there are
            f.write(line + ", ") #"f" specifies the current file open and will write every item in the list with a comma and line break at the end