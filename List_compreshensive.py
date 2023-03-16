# result = []
#  for i in "inmakes":
#      result.appened(i)
# print(result)
# lc syntax [expre forloop ]
result = [i for i in "inmakes"]
print(result)
result = ["python", "django", "flask", "people"]
new = [i for i in result]
print(new)
# p condition normally
result = ["python", "django", "flask", "people"]
new = []
for i in result:
    if 'p' in i:
        new.append(i)
print(new)
# easy lc
result = ["python", "django", "flask", "people"]
new = [i for i in result if 'p' in i]
print(new)
# range using
new = [i for i in range(10)]
print(new)
new = [i for i in range(2, 10, 2)]
print(new)
result = ["python", "django", "flask", "people"]
new = ["inmakes" for i in result]
print(new)
result = ["python", "django", "flask", "people"]
new = [i.upper() for i in result]
print(new)
new = [i.lower() for i in result]
print(new)
num = [5, 8, 9, 4]
new = [i * i for i in num]
print(new)
a = [6, 8, 9, 10]
b = [7, 8, 9, 0]
n = [x + y for x in a for y in b]
print(n)
num = [i for i in range(1, 11)]
print(num)


def square(x):
    return x * x


sq = [square(x) for x in range(1, 5)]
print(sq)
# 1|*1 2*2 3*3 4*4


a = [6, 8, 9, 10]
b = [7, 8, 9, 0]
c = [1, 2, 4, 5, 7]
number = [a[i] + c[i] for i in range(0, len(a))]
print(number)
