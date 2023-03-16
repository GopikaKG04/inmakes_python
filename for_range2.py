for i in range(10):
    if i==5:
       break
    print(i)
else:
    print("am else part")
    #first for loop i default 0 range 10
    #0==5 false print 0 ,i =1 1 checking 1==5 false no working if condition
    #then print 1, another print
    #last i=5 if condition checking i==5 , 5==5 conditon true
    #so if working break
    # so loop is termined or stop execution
# break after the else part cnn't work the loop stop execution