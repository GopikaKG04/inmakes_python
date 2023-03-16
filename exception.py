#a=4
#b=0
#print(a/b)
#zerodivision error handing tyhis situation try and except block  so try block inside code
try:
    a=4
    b=2
    print(a/b)# print result handing 
except:
      print("there is an error")# no this is not working
finally:
      print("am finally")