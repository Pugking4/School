def make_shirt(text,size):
    print(f"'{text}' is printed on this shirt and the size is {size}")
name = input("Text: ")
#siz = input("Size: ")
siz = ""
def s_shirts(text):
    siz = "small"
    make_shirt(text,siz)

def m_shirts(text):
    siz = "medium"
    make_shirt(text,siz)

def l_shirts(text):
    siz = "large"
    make_shirt(text,siz)

s_shirts(name)
m_shirts(name)
l_shirts(name)