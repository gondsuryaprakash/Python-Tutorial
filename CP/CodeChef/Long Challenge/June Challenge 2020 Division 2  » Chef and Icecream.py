t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    count5=0
    count10=0
    count15=0
    flag=0
    for i in range(n):
        if arr[i]==5:
            count5+=1
        elif arr[i]==10:
            if count5>=1:
                count5-=1
                count10 += 1
            else:
                flag=1
                break
        elif arr[i]==15:
            if count10>=1:
                count10-=1
                count15+=1
            elif count5>=2:
                count5-=2
                count15+=1
            else:
                flag=1
                break
    print("YES" if flag==0 else "NO")









