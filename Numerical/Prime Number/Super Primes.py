isPrime=[True for i in range(10000001)]
isPrime[0]=False
isPrime[1]==False
p=2
primeArray=[]
while p*p<=10000001:
    if isPrime[p]==True:
        for i in range(p*p,10000001,p):
            isPrime[i]=False
    p+=1
for i in range(2,10000001):
    if isPrime[i]:
        primeArray.append(i)

t=int(input())
for _ in range(t):
    n=int(input())
    count=0
    aprimeArray=list(filter(lambda x:x<=n,primeArray))
    for i in range(len(aprimeArray)):
        for j in range(i+1,len(aprimeArray)):
            sum=aprimeArray[i]+aprimeArray[j]
            if sum in primeArray:
                count+=1

    print(count)