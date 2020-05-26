def binomialCoefficint(n,k):
    cArray=[[0 for x in range(k+1)] for x in range(n+1)]
    for i in range(n+1):
        for j in range(min(i,k)+1):
            if j==0 or j==i:
                cArray[i][j]=1
            else:
                cArray[i][j]=cArray[i-1][j-1]+cArray[i-1][j]
    return cArray[n][k]

a=binomialCoefficint(5,2)
print(a)