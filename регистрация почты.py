q = input()
w = input()
e = "@"
if e not in q and e in w:
    print("OK")
elif e in q and e in w:
    print("Некорректный логин")
elif e not in q and e not in w:
    print("Некорректный адрес")
elif e in q and e not in w:
    print("Некорректный логин")



