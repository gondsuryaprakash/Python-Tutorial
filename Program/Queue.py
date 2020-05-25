class Queue:
    def __init__(self):
        self.queue=list()
        self.first=-1
        self.last=-1


    def enqueue(self,value):
        if self.first==-1:
            self.first=self.first+1
        self.last=self.last+1
        self.queue.insert(self.last,value)
  

queue=Queue()
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)


