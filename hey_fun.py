def hey():
    print("hello")
hey() #simple fun no argument
# we pass an argunment
def hey(name):
    print("my name is:"+ name)
hey("gopika")
# usr input
def hey(name):
    print("my name is:"+ name)
values="crosseroads"# variables input
hey(values)
# we have many arugmnents passing using arbitary argunment*
def hello(*values):
    print(values[0]+values[1])
def hay():
    print("python")
values="crossroads"
hay()
hello("nidhu","gopu")
#gobal outside function all varibles accessde and localinside function acessable only inside
values=10# gobal
def sample():
    print(values)
print(values)
sample()
#global
values=10
def sample():
    values=int(30)
    print(values)
sample()
print(values)
def sample(name,age=20):
    print(name,age)
sample("nidhu",32)
#return
def sample(num1,num2):
    sum=num1+num2
    return sum
result=sample(20,5)
print(result)
