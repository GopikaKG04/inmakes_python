def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)  # 5*5-1=4,4*4-1=3,3*3-1=2,2*2-1=1 5*4*3*2*1=120


print(fact(7))


# itself call during the function
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


result = factorial(5)
print(result)
