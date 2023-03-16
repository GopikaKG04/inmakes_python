x = lambda a, b: a + b
print(x(2, 3))
x = lambda a: a + 30
print(x(7))
x = lambda a, b, c: a + 30 + b * c
print(x(7, 7, 4))


def fun(b):
    return lambda b: b + b


x = fun(2)
print(x(8))
