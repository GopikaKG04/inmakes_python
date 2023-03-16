def simpleinterest(p, r, n):
    return (p * r * n) / 100


p = int(input("enter first number"))
r = int(input("enter second number"))
n = int(input("enter third number"))
simple = (simpleinterest(p, n, r))
print(simple)
