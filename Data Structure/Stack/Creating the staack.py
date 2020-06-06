from sys import maxsize
def createStack():
    stack=[]
    return stack
def isEmpty(stack):
    return len(stack)==0

def push(stack ,element):
    stack.append(element)

def pop(stack):
    if(isEmpty(stack)):
        return
    return stack.pop()
def peek(stack):
    if(isEmpty(stack)):
        return str(-maxsize-1)
    return stack[-1]





