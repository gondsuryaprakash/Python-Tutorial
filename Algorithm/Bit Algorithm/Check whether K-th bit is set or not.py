# t=int(input())
# for i in range(t):
#     n=int(input())
#     k=int(input())
#     i=0
#     mask=1
#     while i<k:
#         mask=mask<<1
#         i+=1
#     print("Yes" if mask&n else "No")

t=int(input())
for i in range(t):
    n=int(input())
    val = 0
    i = 0
    while n:
        x = n >> 1
        y = n >> 1
        x, y = y, x
        if x & 1:
            val += pow(x, i + 1)
        if y & 1:
            val += pow(y, i)
        i += 1
        n >>= 1
    print(val - 1)





