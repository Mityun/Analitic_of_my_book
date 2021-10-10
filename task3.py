def fibb(n):
    fib_num = {1: 1, 2: 2}
    if n in fib_num:
        return fib_num[n]
    fib = fibb(n - 1) + fibb(n - 2)
    fib_num.append(fib)
    print(fib_num[n])


print(fibb(5))




