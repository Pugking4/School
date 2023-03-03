draft = []
usernames = set()
cond = False
count = 1

with open("classlist.txt", 'r') as f:
    for lines in f:
        lines = lines.rstrip().lower().split()
        if len(lines) == 3:
            lines = f"{lines[0]+lines[1]} {lines[2]}"
            lines = lines.split()
        draft.append(lines)

print(draft)

for names in draft:
    count = 1
    user = names[0]
    if user not in usernames:
        usernames.add(user)
    else:
        user = names[0]+names[1][0]
        if user not in usernames:
            usernames.add(user)
        else:
            while cond == False:
                user = names[0]+names[1][0]+str(count)
                if user not in usernames:
                    usernames.add(user)
                    cond = True
                else:
                    count += 1
#print(usernames)
for i in usernames:
    print(i)
