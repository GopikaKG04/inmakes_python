# set datatype
number = {10, 20, 40, 60, 90}
number.add(78)
number.add("hello")
number.remove(40)
print(number)
seta = {1, 2, 3, 4, 5}
setb = {4, 5, 6, 7, 8}
print(seta | setb)  # union()
print(seta & setb)  # intersection common elements
print(seta - setb)  # difference()
print(setb - seta)
