def leftRotate(arr,n):
    temp=arr[0]
    for i in range(n-1):
        arr[i]=arr[i+1]
    arr[n-1]=temp
def rotationOfArray(arr,d,n):
    for i in range(d):
        leftRotate(arr,n)

a=[1,2,3,4,5]
rotationOfArray(a,2,5)
print(a)


