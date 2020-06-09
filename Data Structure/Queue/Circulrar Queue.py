class CircularQueu():
    def __int__(self,size):
        self.size=size
        self.queue=[0 for i in range(size)]
        self.front=self.rear=-1
    def enqueue(self,item):
        if (self.rear+1)%self.size==self.front:
            return
        elif self.front==-1:
            self.front=0
            self.rear=0
            self.queue[self.rear]=item
        else:
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear]=item
    def deque(self):
        if self.front==-1:
            return
        elif self.front==self.rear:
            tmp=self.queue[self.front]
            self.front=-1
            self.rear=-1
            return tmp
        else:
            tmp=self.queue[self.front]
            self.front=(self.front+1)%self.size
            return tmp

