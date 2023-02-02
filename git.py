def f(n):
    return 1 if (n == 0 or n == 1) else f(n-1) + f(n-2)


print(f(5))
