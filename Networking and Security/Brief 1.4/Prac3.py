def make_shirt(text,size):
    print(f"'{text}' is printed on this shirt and the size is {size}")
name = input("Text: ")
siz = input("Size: ")
make_shirt(name,siz)
make_shirt(text=name,size=siz)
make_shirt(size=siz,text=name)