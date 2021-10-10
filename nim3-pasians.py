a = int(input())
s = int(input())
d = int(input())
while a != 0 or s != 0 or d != 0:
    k = int(input())
    ka = int(input())
    if k == 1:
        a -= ka
        print(a, s, d)
    elif k == 2:
        s -= ka
        print(a, s, d)
    elif k == 3:
        d -= ka
        print(a, s, d)
