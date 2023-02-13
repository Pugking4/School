list = [" do lots of stuff."," so much stuff I couldnt list it all!","not list all the things you can do with it :("]
with open("misc",'w') as file_object:
    for i in range(len(list)):
        file_object.write(f"In Python you can{list[i]}\n")