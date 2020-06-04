class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __int__(self):
        self.head=None

    def print(self):
        current=self.head
        while current:
            print("[{}]-->".format(current.data),end=" ")
            current=current.next
        print(None)




llist=LinkedList()
llist.head=Node(1)
second=Node(2)
third=Node(3)
fourht=Node(4)

llist.head.next=second
second.next=third
third.next=fourht
llist.print()

