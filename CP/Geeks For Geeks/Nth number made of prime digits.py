arr=[]
for i in range(2,2278):
    flag=True

    n=i
    while i>0:
        rem=i%10
        # print(rem)
        if rem==2 or rem==3 or rem==5 or rem==7:
            flag &= True
            # print("rem={}".format(rem))
        else:
            flag &= False
        i=i//10
    if flag:
        arr.append(n)
t=int(input())
for i in range(t):
    n=int(input())
    res=arr[n-1]
    print(res)





