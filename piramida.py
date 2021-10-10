a = -1
d = int(input())
for i in range(d):
    s = a + 2
    a = s
    print(" " * (d - (i + 1)) + ("*" * s), sep="")
