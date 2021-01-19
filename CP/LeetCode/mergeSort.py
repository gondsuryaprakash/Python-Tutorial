def mergeSort(arr1,m,arr2,n):
    for i in range(n-1,0):
        last=arr2[m-1]
        for j in range(m-2,0):
            if arr2[i]<arr1[j]:
                arr1[j+1]=arr2[j]
            else:
                arr1[j]=arr2[i]
                arr2[i]=last


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

mergeSort(nums1,m,nums2,n)




