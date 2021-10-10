a = int(input())
s = a // 100
d = (a - (100 * s)) // 10
f = a - (s * 100) - (d * 10)
if s != d and s != f and f != d:
    print("ОК")
elif s != d and s != f and f == d:
    print("В числе две одинаковые цифры")
elif s != d and s == f and f != d:
    print("В числе две одинаковые цифры")
elif s == d and s != f and f != d:
    print("В числе две одинаковые цифры")
elif s != d and s == f and f == d:
    print("В числе все цифры одинаковые")
elif s == d and s == f and f != d:
    print("В числе все цифры одинаковые")
elif s == d and s != f and f == d:
    print("В числе все цифры одинаковые")
elif s == d and s == f and f == d:
    print("В числе все цифры одинаковые")