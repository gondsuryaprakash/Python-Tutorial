def rotateByD(arr,d,n):
    for i in range(d):
        return leftRotation(arr,n)
def leftRotation(arr,n):
    for i in range(n-1):
        temp=arr[0]
        arr[i]=arr[i+1]
    arr[n-1]=temp
    return arr

a=[11,22,44,33,55,66]
print(rotateByD(a,3,6))