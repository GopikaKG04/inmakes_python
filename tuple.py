y = (8, 9, "python", "java")
print(y)
print(type(y))
print(len(y))
x = list(y)
print(x)
print(type(x))
x.insert(1, "c++")
print(x)
y = tuple(x)
print(y)

y = tuple(("net", "vb", 4, 7))
print(y)
print(len(y))
y = tuple((range(3)))
print(y)

a = tuple(("asp", "php"))
for t in a:
    print(t)
a = tuple(("asp", "php"))
for i in range(1):
    print(i)

x = (96, 8, "hello")
y = (9, 6, "hey")
print(x + y)
x = (96, 8, "hello")
m = x * 3
print(m)
x = (96, 8, "hello")
for i in x:
    print(x * 2)
x = tuple(("hello", 2))
for i in x:
    print(x)
