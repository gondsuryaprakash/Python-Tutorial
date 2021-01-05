def linearSort(arr):
    for i in range(len(arr)):
        # take the min_index
        min_index=i
        for j in range(i+1,len(arr)):
            if arr[min_index]>arr[j]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
print(linearSort([24,2,53,5,45]))
