#1.write a function which divide two numbers,desgin the function in a manner that it handles the divide by zero exception

def division(a,b):
    try:
        return a/b
    except:
         print("an error")
    finally:
        print("am finally")

num1=int(input("enter first number"))
num2=int(input("enter second number"))
result=(division(num1,num2))
print(result)




