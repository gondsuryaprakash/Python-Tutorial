class StackNode:
    def __int__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __int__(self):
        self.root=None
    def isEmpty(self):
        return True if self.root is None else False
    def push(self,data):
        newNode=StackNode(data)
        newNode.next=self.root
        self.root=newNode
    def pop(self):
        if self.isEmpty():
            return float("-inf")
        tmp=self.root
        self.root=self.root.next
        popped=tmp.data
        return popped
