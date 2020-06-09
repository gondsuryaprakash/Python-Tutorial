t=int(input())
for i in range(t):

    n=int(input())
    res = [0] * (n)
    arr=list(map(int,input().split()))
    for i in range(n):
        res[arr[i]-1]=i+1
        # print("arr[i]={},i+1={},res={}".format(arr[i]-1,i+1,res))

    for i in res:
        print(i,end=" ")
    print()
# 1
# 10
# 5 1 8 3 2 4 10 6 7 9