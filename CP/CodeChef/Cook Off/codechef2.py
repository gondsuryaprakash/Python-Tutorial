t=int(input())
for i in range(t):
    n=int(input())
    arrA=list(map(int,input().split()))
    arrB=list(map(int,input().split()))
    x1=0
    x2=0
    wieredSum=0
    for i in range(n):
        x1+=arrA[i]
        x2+=arrB[i]
        if arrA[i]==arrB[i] and x1==x2:
            wieredSum+=arrA[i]

    print(wieredSum)
