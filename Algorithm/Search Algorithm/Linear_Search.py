def search(arr,n,x):
    for i in range(0,n):
        if arr[i]==x:
            print('{} is find at index {}'.format(arr[i],i))
            return i

    return -1


search(['s','sp','spDon'],3,'spDon')

