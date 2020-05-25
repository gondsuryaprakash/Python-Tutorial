def printMessge():
    name=int(input('Name: '))
    if name%2==0:
        print('Even')
    else:
        print('Odd')


'''Parameter'''
def printEven(n):
    if n%2==0:
        print('Even')
    else:
        print('Odd')

printEven(9)
'''return Value'''
def square(number):
    return number*number

print(square(89))
