def rotateArray(arr,n):
    tmp=arr[0]
    for i in range(n-1):
        arr[i]=arr[i+1]
    arr[n-1]=tmp
    return arr
def rotatebyD(arr,n,d):
    for i in range(d):
        rotateArray(arr, n)
    return arr




def rotateByK(arr,n,k):
    for j in range(k):
        tmp=arr[0]
        for i in range(n-1):
            arr[i]=arr[i+1]
        arr[n-1]=tmp
    return arr

# a=rotateByK(arr,n,d)
# for el in a:
#     print(el,end=" ")
# print()

# Efficent Method
def reverse(arr,start,end):
    while start<end:
        tmp=arr[start]
        arr[start]=arr[end]
        arr[end]=tmp
        start+=1
        end-=1
    return arr

def rotate(arr,k):
    reverse(arr,0,len(arr)-1)
    reverse(arr,0,k-1)
    reverse(arr,k,len(arr)-1)
    return arr








arr=[1,2,3,4]
a=rotate(arr,2)
print(a)
# n=4
# d=2
# a=revers(arr,d)
# print(a)


