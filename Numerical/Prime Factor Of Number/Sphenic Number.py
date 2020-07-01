import math
def primeFactorNumber(n):
    arr=set()
    while n%2==0:
        arr.add(2)
        n//=2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n%i==0:
            arr.add(i)
            n//=i

    if n>2:
        arr.add(n)
    return  True if len(arr)==3 else False

t=int(input())
for _ in range(t):
    n=int(input())
    print(1 if primeFactorNumber(n) else 0)

