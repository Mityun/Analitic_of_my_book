a = int(input())
b = int(input())
c = int(input())
d = int(input())
if b > d:
    obs = b / d
    chis = d * obs
    res = b - chis
    if obs // res != 0:
        res = 1
        obs = obs // res
    elif int(obs) // int(res) == 0:
        print(obs / res)
elif d > b:
    obs = d / b
    chis = b * obs
    res = d - chis
    if obs // res != 0:
        res = 1
        obs = obs // res
    elif obs // res == 0:
        print(obs / res)