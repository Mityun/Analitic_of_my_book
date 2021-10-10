a = int(input())
q = a % 4
w = a % 100
e = a % 400
if q == 0 and w != 0 or e == 0:
    print("Високосный")
else:
    print("Не високосный")
