a = int(input())
q = 0
w = 0
e = 0
r = 0
t = 0
f = input()
for i in range(a):
    if 'тип I' in f:
        q += 1
        if 'тип IIA' in f:
            w += 1
            if 'тип IIB' in f:
                e += 1
                if 'SO(32)' in f:
                    r += 1
                    if 'E8xE8' in f:
                        t += 1
    else:
        if 'тип IIA' in f:
            w += 1
            if 'тип IIB' in f:
                e += 1
                if 'SO(32)' in f:
                    r += 1
                    if 'E8xE8' in f:
                        t += 1
        else:
            if 'тип IIB' in f:
                e += 1
                if 'SO(32)' in f:
                    r += 1
                    if 'E8xE8' in f:
                        t += 1
            else:
                if 'SO(32)' in f:
                    r += 1
                    if 'E8xE8' in f:
                        t += 1
                else:
                    if 'E8xE8' in f:
                        t += 1
                    else:
                        continue
print('«тип I»:', q)
print('«тип IIA»:', w)
print('«тип IIB»:', e)
print('«SO(32)»:', r)
print('«E8xE8»:', t)