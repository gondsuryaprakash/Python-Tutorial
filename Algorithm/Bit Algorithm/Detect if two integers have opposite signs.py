
def countSetBits(n):
    bitCOunt=0
    for i in range(1,n+1):
        bitCOunt+=countSetBitsUtils(i)
    return bitCOunt
def countSetBitsUtils(x):
    if x<=0:
        return 0
    return (0 if int(x%2)==0 else 1)+countSetBitsUtils(int(x/2))
t=int(input())
for i in range(t):
    n=int(input())
    res=countSetBits(n)
    print(res)
