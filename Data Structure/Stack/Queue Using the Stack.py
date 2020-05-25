class Queue:
    def __init__(self):
        self.s1=[]
        self.s2=[]
    def enqueue(self,x):
        while len(self.s1)!=0:
            self.s2.append(self.s1[-1])
            self.s1.pop()
        self.s1.append(x)
        while len(self.s2)!=0:
            self.s1.append(self.s2[-1])
            self.s2.pop()
    def dequeue(self):
        if len(self.s1)==0:
            print('Q is Empty')

        x=self.s1[-1]
        self.s1.pop()
        return x

q=Queue()
q.enqueue(2)
q.enqueue(22)
q.enqueue(1)
q.enqueue(33)
q.enqueue(89)
print(q.dequeue())
print(q.dequeue())