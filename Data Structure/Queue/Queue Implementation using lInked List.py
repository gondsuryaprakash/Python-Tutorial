class Node:
    def __int__(self,data):
        self.data=data
        self.next=None
class LList:
    def __int__(self):
        self.head=None

class Queue:
    def __int__(self):
        self.front=None
        self.rear=None
    def isEmpty(self):
        return self.front==None

    def Enqueue(self,item):
        new_Node=Node(item)
        if self.rear==None:
            self.front=self.rear=new_Node
        self.rear.next=new_Node
        self.rear=new_Node
    def Dequeue(self):
        if self.isEmpty():
            return
        tmp=self.front
        self.front=tmp.next
        if self.front==None:
            self.rear=None
            
