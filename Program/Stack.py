class Stack:
    def __init__(self):
        self.stack=list()

    def push(self,value):
        self.stack.append(value)
    def pop(self):
        if len(self.stack<1):
            print('The stack is Empty')
        else:
            self.stack.pop()
    def printStack(self):
        print(self.stack)
stack=Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)


stack.printStack()

