# Impelmentation of the stack using the list
# append is use the insert the value
stack=[]
stack.append('a')
stack.append('c')
stack.append('d')
# print(stack)

# pop is used to popup the value from the stack
stack.pop()
stack.pop()
# print(stack)

# Implementation by using the collection.queue

from collections import deque
s=deque()
s.append('Surya')
s.append('Nisha')
s.append('Rishabh')
s.append('Indresh')
# print(s)

# Implementation by using the queue model
from queue import LifoQueue
stack1=LifoQueue(maxsize=3)
# print(stack1.qsize())
# put() is used to insert the element
# get() function is used to the delete the element from the stack
stack1.put('a')
stack1.put('b')
stack1.put('c')
print(stack1)