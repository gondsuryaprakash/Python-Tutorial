def goldMine(gold,m,n):
    goldTable=[[0 for i in range(n)] for j in range(m)]
    for col in range(n-1,-1,-1):
        for row in range(m):
            if col==n-1:
                right=0
            else:
                right=goldTable[row][col+1]
            if col==n-1 or row==m-1:
                rightDown=0
            else:
                rightDown=goldTable[row+1][col+1]
            if row==0 or col==n-1:
                rightUp=0
            else:
                rightUp=goldTable[row-1][col+1]

            goldTable[row][col]=gold[row][col]+max(rightUp,right,rightDown)


    res=goldTable[0][0]
    for i in range(1,m):
        res=max(res,goldTable[i][0])

    return res



gold = [[1, 3, 1, 5],
    [2, 2, 4, 1],
    [5, 0, 2, 3],
    [0, 6, 1, 2]]
m=4
n=4
print(goldMine(gold,m,n))