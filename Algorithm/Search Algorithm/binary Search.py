def binarySearch(arr,l,r,x):
    if r>=l:
        mid=l+(r-l)//2
        if arr[mid]==x:
            print("{} is found at the position of the {}".format(x,mid))
            return mid
        elif arr[mid]>x:
            return binarySearch(arr,l,mid-1,x)
        else:
            return binarySearch(arr,mid+1,r,x)

    else:
        print("The given elemten")
        return -1






binarySearch([1,2,3,380,4],0,3,380)

