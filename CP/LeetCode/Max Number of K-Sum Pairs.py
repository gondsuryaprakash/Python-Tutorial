def findCountOfSum(arr,k):
    arr.sort()
    i=0
    j=len(arr)-1
    count=0
    while i<j:
        if arr[i]+arr[j]==k:
           count+=1
           j-=1
           i+=1
        elif arr[i]+arr[j]<k:
            i+=1
        else:
            j-=1

    return count

arr=[3,1,3,4,3]
k=6
a=findCountOfSum(arr,k)
print(a)

