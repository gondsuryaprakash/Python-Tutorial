def findMissingNumber(arr,n):
    arr.sort()

    for i in range(0,n):
        if arr[i]!=i+1:
            print('arr[i]=={} and i={}'.format(arr[i],i))
            return i+1



def secondMethod(arr,n):
    totalSum=n*(n+1)/2
    sum1=sum(arr)
    return int(totalSum-sum1)

print(secondMethod([1,2,3,4,6,7],7))

