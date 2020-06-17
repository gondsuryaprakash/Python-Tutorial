class Node:
    def __int__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __int__(self):
        self.head=None
    def insertAtBiging(self,node):
        newNode=Node(node)
        newNode.next=self.head
        self.head=newNode
    def insertAtMid(self,node,pos):

        newNode=Node(node)
        prev=self.head
        while prev:
            if prev.data==pos:
                newNode.next=prev.next
                prev.next=newNode
                break
            prev=prev.next
    def insertAtEnd(self,node):
        newNode=Node(node)
        if self.head is None:
            self.head=newNode
            return
        currrent=self.head
        while currrent:
            currrent.next
        currrent.next=newNode






