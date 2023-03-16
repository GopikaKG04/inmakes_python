def add(a,b):
    return a+b
print(add(2,4))

#create a variable place value of function call
def add(num1,num2):
    return num1+num2
result=(add(10,5))
print(result)

#passing function to arguments to the function
def add(a,b):
    return a+b
def square(c):
    return c*c
result=square(add(2,3))
print(result)
