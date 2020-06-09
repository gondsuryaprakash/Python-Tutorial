n=218
import math
sum=1
flag=0
for i in range(int(math.sqrt(218))):
    sum+=2**i
    print(sum)
    if sum==n:
        flag=1
        break
    if sum>n:
        break

print("True" if flag==1 else "False")






