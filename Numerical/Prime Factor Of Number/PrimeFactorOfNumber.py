import math
def getPrimeFactor(n):
    arr = []
    while n % 2 == 0:
        arr.append(2)
        n = n // 2
    print(int(math.sqrt(n)))
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            arr.append(i)
            n //= i
    if n > 2:
        arr.append(n)
    print(arr)
    return max(arr)


getPrimeFactor(666)
# t = int(input())
# for i in range(t):
#     n = int(input())
#     print(getPrimeFactor(n))

