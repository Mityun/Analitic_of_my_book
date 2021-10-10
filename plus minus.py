q = float(input())
w = float(input())
e = input()
if e == "-" and w != 0:
    print(q - w)
elif e == "+" and w != 0:
    print(q + w)
elif e == "*" and w != 0:
    print(q * w)
elif e == "/" and w != 0:
    print(q / w)
elif e != "+" and e != "-" and e != "*" and e != "/":
    print(888888)
elif w == 0:
    print(888888)
