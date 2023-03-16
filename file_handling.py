

file=open("demo.txt",'r')
content=file.read()
print(content)
file.close()

file=open("demo.txt",'r')
content=file.readline()
print(content)
file.close()

file=open("demo.txt",'r')
content=file.read(10)
print(content)
file.close()

file=open("demo.txt",'w')
file.write("am python django")
file.close()

file=open("demo.txt",'a')
file.write("am append")
file.close()