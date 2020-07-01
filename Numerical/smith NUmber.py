import math
def isprime(n):
    if n<=1:
        return False
    p=2
    while p*p<=n:
        if n%p==0:
            return False
        p+=1




def sumOfDigit(n):
    sum=0
    while n:
        rem=n%10
        sum+=rem
        n//=10
    return sum
def primeFactor(n):
    sum=0
    arr=[]
    while n%2==0:
       sum+=2
       arr.append(2)
       n//=2
    for i in range(3,int(math.sqrt(n)+1),2):
        while n%i==0:
            sum+=sumOfDigit(i)
            arr.append(i)
            n//=i
    if n>2:
        sum+=sumOfDigit(n)
        arr.append(n)
    return sum

t=int(input())
for _ in range(t):
    n=int(input())
    print(sumOfDigit(n))
    print(primeFactor(n))
    print(1 if sumOfDigit(n)==primeFactor(n)  else 0)

