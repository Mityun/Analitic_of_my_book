a = input()
s = input()
if (a == "да" and s == "да") or (a == "да" and s == "нет") \
        or (a == "нет" and s == "да") or \
        (a == "нет" and s == "нет"):
    print("ВЕРНО")
else:
    print("НЕВЕРНО")