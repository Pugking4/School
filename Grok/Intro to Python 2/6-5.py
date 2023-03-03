draft = []
usernames = []
cond = False
count = 1

with open("classlist.txt", 'r') as f:
    for lines in f:
        lines = lines.rstrip().lower().split()
        if len(lines) == 3:
            lines = f"{lines[0]+lines[1]} {lines[2]}"
            lines = lines.split()
        draft.append(lines)

#print(draft)

for names in draft:
    cond = False
    count = 1
    user = names[0]
    #print("testing 0", user)
    if user not in usernames:
        usernames.append(user)
        #print("testing success 0", user)
    else:
        user = names[0]+names[1][0]
        #print("testing 1", user)
        #print(usernames)
        if user not in usernames:
            usernames.append(user)
            #print("testing success 1", user)
        else:
            while cond == False:
                #print("testing", count+1, user)
                user = names[0]+names[1][0]+str(count)
                if user not in usernames:
                    usernames.append(user)
                    cond = True
                    #print("testing success", count+1, user)
                else:
                    count += 1
#print(usernames)
for i in usernames:
    print(i)
