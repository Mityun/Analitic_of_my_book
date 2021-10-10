a = input()
s = input()
d = input()
if d == ">":
    print(max(a, s))
elif d == "<":
    print(min(a, s))
elif a == s:
    print(a)