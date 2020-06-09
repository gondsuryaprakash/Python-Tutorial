C=4
R=4
def reverseColumns(arr):
    for i in range(C):
        j=0
        k=C-1
        while j<k:
            t=arr[j][i]
            arr[j][i]=arr[k][i]
            arr[k][i]=t
            j+=1
            k-=1
def transpose(arr):
    for i in range(R):
        for j in range(i,C):
            t=arr[i][j]
            arr[i][j]=arr[j][i]
            arr[j][i]=t
def printMatrix(arr):
    for i in range(R):
        for j in range(C):
            print(str(arr[i][j]),end=" ")
        print()


def rotate90(arr):
    transpose(arr)
    reverseColumns(arr)



arr = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ];


