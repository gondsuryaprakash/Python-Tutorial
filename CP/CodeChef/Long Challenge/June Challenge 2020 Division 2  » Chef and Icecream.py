t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    coin=[5,10,15]
    hashMap={5:0,10:0,15:0}
    flag=0
    for i in range(n):
        if arr[i]==5:
            hashMap[arr[i]]+=1
        elif arr[i]==10:
            hashMap[arr[i]]+=1
            if hashMap[arr[i]-5]>=1:
                hashMap[arr[i]-5]-=1
            else:
                flag=1
                break
        elif arr[i]==15:
            hashMap[arr[i]]+=1
            if hashMap[arr[i]-5]>=1:
                hashMap[arr[i]-5]-=1
            elif hashMap[arr[i]-10]>=2:
                hashMap[arr[i]-10]-=2
            else:
                flag=1
                break
    print("Yes" if flag==0 else "NO")





