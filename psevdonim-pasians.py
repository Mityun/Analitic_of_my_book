vse = int(input())
while vse != 0 and vse > 0:
    take = int(input())
    if take <= 3 and take <= vse:
        vse -= take
    print(vse)