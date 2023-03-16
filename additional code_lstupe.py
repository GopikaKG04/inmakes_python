# 1.created list nnd created new list  exiting list using string formating method
list1 = [3, 7, 9, 8, 6]
newstring = "my number is : {0},{1},{2} ".format(list1[1], list1[0], list1[2])
print(newstring)
# 2.create a list in 8 elements then print the 2th to 6th index
li = [100, 200, 300, 400, 500, 600, 700, 800]
print(li)
print(li[2:7])
# 3.create a tuple  then append and insert to the tuple 6 elements in tupleprint last second th one index vaule
x = ("hello", "python", "c++", 8, 9, 10)
print(x)
y = list(x)
y.insert(1, "html")
print(y)
y.append("java")
print(y)
x = tuple(y)
print(x)
print(x[-2])
