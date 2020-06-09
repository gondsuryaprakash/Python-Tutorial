def findOne(arr):
    ones=0
    twos=0
    for i in range(len(arr)):
        twos=twos|(ones &arr[i])
        ones^=arr[i]
        common_bitMask=~(ones & twos)
        ones &= common_bitMask
        twos &= common_bitMask
    return ones


a=findOne([2 ,2 ,5, 5 ,20 ,30 ,30])
print(a)
