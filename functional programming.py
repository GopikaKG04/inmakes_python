def additional(a, b):
    return a + b  # 10


def square(c):  # 10^2 =100 10*10=100
    return c * c


result = square(additional(2, 8))
print(result)


def additional(a, b):
    return a + b


def square(c):
    return c * c


result = square(additional(4, 8))
print(result)
