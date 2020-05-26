def Catalan(n):
    if n==0 or n==1:
        return 1
    catalanArray=[0 for i in range(n+1)]
    catalanArray[0]=1
    catalanArray[1]=1
    for i in range(2,n+1):
        catalanArray[i]=0
        for j in range(i):
            catalanArray[i]=catalanArray[i]+catalanArray[j] * catalanArray[i-j-1]

    return catalanArray[n]


a=Catalan(10)
print(a)

