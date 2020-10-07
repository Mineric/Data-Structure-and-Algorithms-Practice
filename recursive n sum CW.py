def digital_root(n):
    str_n=str(n)
    sum=0
    if len(str(str_n)) == 1:
        return int(str_n)
    for i in str_n:
        sum += int(i)
        str_n=sum
    return digital_root(str_n)

def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))


def digital_root(n):
    # ...
    while n>9:
        n=sum(map(int,str(n)))
    return n


def digital_root(n):
    while n>10:
        n = sum([int(i) for i in str(n)])
    return n