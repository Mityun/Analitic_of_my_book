a = input()
s = input()
while True:
    if len(a) < 8:
        print("Короткий!")
        a = input()
        s = input()
    elif len(a) > 8 and "123" in a:
        print("Легкий!")
        a = input()
        s = input()
    elif len(a) > 8 and "123" not in a and s != a:
        print("Различаются.")
        a = input()
        s = input()
    elif len(a) > 8 and "123" not in a and s == a:
        print("OK")
        break

