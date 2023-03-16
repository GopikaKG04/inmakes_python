def function1(a,b):
     return a+b
x=int(input("enter first number"))
y=int(input("enter second number"))

print(function1(x,y))
#syntax error
def function1(a,b):# missing indendation
    print(a+b)
function1(2,2)
#logical error
#we add numbers
def function1(a,b):
    print(a*b)# a+b
function1(2,2)# ouput 4 bt logical mistake
