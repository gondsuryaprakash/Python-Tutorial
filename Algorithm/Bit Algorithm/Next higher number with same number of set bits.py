def snoob(x):
    next=0
    if(x):
        rightOne=x&-x
        print(rightOne)
        nextHigherOneBit=x+int(rightOne)
        print("x+int(rightOne)",nextHigherOneBit)
        rightOnesPattern=x^int(nextHigherOneBit)
        print("x^int(nextHigherOneBit)",rightOnesPattern)
        rightOnesPattern=(int(rightOnesPattern))/(int(rightOne))
        print("(int(rightOnesPattern))/(int(rightOne))",rightOnesPattern)
        rightOnesPattern=int(rightOnesPattern)>>2
        print("int(rightOnesPattern)>>2",rightOnesPattern)
        next=nextHigherOneBit|rightOnesPattern
        print("{}|{}={}".format(nextHigherOneBit,rightOnesPattern,next))
    return next

a=snoob(156)
print(a)