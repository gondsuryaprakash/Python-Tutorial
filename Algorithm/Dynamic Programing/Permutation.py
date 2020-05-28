def permutation(n,k):
    cArray=[[0 for i in range(k+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(min(i,k)+1):

            if j==0:
                cArray[i][j]=1
            else:
                cArray[i][j]=cArray[i-1][j]+(j*cArray[i-1][j-1])
            if j<k:
                cArray[i][j+1]=0
    return cArray[n][k]


print(permutation(10,2))
