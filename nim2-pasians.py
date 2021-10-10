vse1 = int(input())
vse2 = int(input())
while (vse1 != 0) or (vse2 != 0):
    n = int(input())
    if n == 1:
        take1 = int(input())
        vse1 -= take1
        print(vse1, vse2)
    elif n == 2:
        take2 = int(input())
        vse2 -= take2
        print(vse1, vse2)