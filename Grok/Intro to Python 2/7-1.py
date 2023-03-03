def find_middle(a,b,c):
    num_min = min(a,b,c)
    num_max = max(a,b,c)
    num_list = [a, b, c]
    #print(num_min, num_max)
    for i in num_list:
        if i != num_min and i != num_max:
            return i
    return a
print(find_middle(-14398, -578, -32598310))
print(find_middle(-14394463458, 5782525, 3252532598310))
print(find_middle(0, 0, 0))
print(find_middle(0.5, 2.8, 28.8))