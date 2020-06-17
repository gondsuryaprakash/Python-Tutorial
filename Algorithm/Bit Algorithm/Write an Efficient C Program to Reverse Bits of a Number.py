def getReverse(x):
    No_OF_BIT=32
    rev=0
    for i in range(No_OF_BIT):
        if x&(1<<i):
            rev|=1<<((No_OF_BIT-1)-i)
    return rev
a=getReverse(1)
print(a)