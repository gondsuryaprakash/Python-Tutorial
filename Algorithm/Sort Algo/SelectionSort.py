def select(arr):


    for j in range(len(arr)-1):
        min=100000000000
        # print("j={}".format(j))

        min_index = -1
        for i in range(j, len(arr)):
            # print(arr[i])
            if arr[i] < min:
                min = arr[i]
                min_index = i
                # print("minIndex={}".format(i))
            # print("min={}".format(min))
        # print("swap={},{}".format(arr[j], arr[min_index]))
        arr[j], arr[min_index] = arr[min_index], arr[j]
        # print(arr)


t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    select(arr)
    print(arr)
'''
1
5
4 1 3 9 7
10
10 9 8 7 6 5 4 3 2 1

'''