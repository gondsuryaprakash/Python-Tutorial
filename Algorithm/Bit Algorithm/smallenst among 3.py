def smallest(x,y,z):
    c=0
    while x and y and z:
        x=x-1
        y=y-1
        z=z-1
        c+=1
    return c

a=smallest(111,44,5)
print(a)

CHAR_BIT=8
def min(x,y):
    return y+((x-y)&((x-1)>>32*CHAR_BIT-1))
def smallest(x,y,z):
    return min(x,min(y,z))
x = 12
y = 15
z = 5
print("Minimum of 3 numbers is ",
               smallest(x, y, z)) 