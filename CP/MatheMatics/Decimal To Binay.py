# By using recursion
def decimalToBinary(n):
    str=''
    if n>1:
        decimalToBinary(n//2)
    print(n%2,end=" ")

# by using inbuilt

def decimalToBinaryByInbuilt(n):
    return bin((n)).replace("0b","")

a=decimalToBinaryByInbuilt(5)
print(a)


