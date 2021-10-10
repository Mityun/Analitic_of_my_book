a = int(input())
b = int(input())
if a > b:
    a = a - (a - b)
    print(a, b)
elif a < b:
    b = b - (b - a)
    print(a, b)
elif a == b:
    print(a, b)
while a > 0 or b > 0:
    d = int(input())
    g = int(input())
    if d == 1:
        while g > a:
            g = int(input())
    elif d == 2:
        while g > b:
            g = int(input())
    if d == 1:
        a -= g
        b -= g
        print(a, b)
    elif d == 2:
        b -= g
        a -= g
        print(a, b)

