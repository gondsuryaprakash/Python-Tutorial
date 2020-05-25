class priorityQueue(object):
    def __init__(self):
        self.queue=[]
    def __str__(self):
        return ' '.join([str[i] for i in self.queue])
    def is_Empty(self):
        return len(self.queue)==0
    def insert(self,data):
        self.queue.append(data)
    def delete(self):
        try:
            max=0
            for i in range(self.queue):
                if self.queue[i]>self.queue[max]:
                    max=i
            item=self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()



