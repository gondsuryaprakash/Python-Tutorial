def fibonacci(n):
    FibArray=[0,1]
    while len(FibArray)<n+1:
        FibArray.append(0)

    if n<=1:
        return n
    if FibArray[n-1]==0:
        FibArray[n-1]=fibonacci(n-1)
    if FibArray[n-2]==0:
        FibArray[n-2]=fibonacci(n-2)
    FibArray[n]=FibArray[n-1]+FibArray[n-2]

    return FibArray[-1]

print(fibonacci(10))