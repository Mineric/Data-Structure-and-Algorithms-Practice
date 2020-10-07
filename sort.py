def take(s):
    return s[1]
def second_lowest(n, s):
    sort = sorted(s, key=take) 
    sort_a=[]
    for i in range(n):
        if sort[i][1] == sort[1][1]:
            sort_a.append(sort[i])
    for j in sorted(sort_a):
        print(j[0])
