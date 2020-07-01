'''Logic
1. go through index of element
2. if the array have same exact number of grater element in the array
than print that element
 1. for every element we find the



'''


def hIndex(arr):
    n=len(arr)
    low=0
    high=len(arr)
    while low<=high:
        mid=(low+(high-low))/2
        if arr[mid]==n-mid:
            return arr[mid]

        elif arr[mid]>n-mid:
            high=mid-1
        else:
            low=mid+1
    return n-low


arr=[0,1,3,5,6]
a=hIndex(arr)
print(a)
