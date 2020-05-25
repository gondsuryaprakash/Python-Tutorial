class Node:
    def __init__(self,value):
        self.value=value
        self.next =None
class LinkedList:
    def __init__(self):
        self.start=None
    def insert(self,value):
        if self.start==None:
            self.start=Node(value)
        current=self.start
        while current.next is not None:
            current=current.next
        current.next=Node(value)
    def print(self):
        current =self.start
        while current is not None:
            print(current.value)
            current=current.next



linkeList=LinkedList()
linkeList.insert(10)
linkeList.insert(20)
linkeList.insert(30)
linkeList.insert(40)
linkeList.insert(50)
linkeList.print()