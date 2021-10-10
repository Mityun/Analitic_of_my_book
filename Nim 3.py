a = int(input())
b = int(input())
c = int(input())
a -= a
print(a, b, c)
while b != 0 or c != 0:
    k = int(input())
    ka = int(input())
    if k == 2:
        while ka > b:
            ka = int(input())
    elif k == 3:
        while ka > c:
            ka = int(input())
    if k == 2:
        b -= ka
        c -= ka
        print(a, b, c)
    elif k == 3:
        b -= ka
        c -= ka
        print(a, b, c)
print("ВЫИГРАЛ ИИ!!!")