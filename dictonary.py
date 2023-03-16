x = {"chair": 500, "table": 900, 34: "seat"}
print(x)
print(len(x))
x = {
    "chair": 500,
    "table": 900,
    34: "seat"}
print(x)
print(x["chair"])
x["veg"] = 100
print(x)
x.update({12: "fruits"})
print(x)
x.pop("chair")
print(x)
# using for loop for print
for y in x:
    print(y)  # key
for y in x.values():
    print(y)
for y in x.items():
    print(y)
    # get function
numbers = {
    1: "one",
    2: "two",
    3: "three"
}
print(numbers.get(2))
print(numbers.get(5))
print(numbers.get(5, "there is no 5"))
print(numbers.get(2, "in the two"))
