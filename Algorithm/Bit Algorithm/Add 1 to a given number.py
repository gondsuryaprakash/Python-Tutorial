# Method 1
def addOne(x):
    m=1
    print(x^m)
    while(x&m):
        x=x^m
        print("{}={}^{}".format(x,x,m))
        m<<1
        print("{}<<1".format(m))
    x=x^m
    print("{}={}^{}".format(x,x,m))
    return x
a=addOne(100)
print(a)

# Method 2
def addOne1(x):
    return (-(~x))
print(addOne1(14))
print("surya")