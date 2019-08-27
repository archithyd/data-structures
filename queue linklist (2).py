class queue:
    def __init__(self,limit=5):
        self.que=[]
        self.limit=limit
        self.front=None
        self.rear=None
        self.size=0

    def en_queue(self,data):
        if(self.size>=self.limit):
            print("Queue overflow")
            return
        else:
            self.que.append(data)
        if(self.front==None):
            self.front=self.rear=0
        else:
            self.rear=self.size
        self.size+=1

    def de_queue(self):
        if(self.size<=0):
            print("queue Underflow")
            return
        else:
            self.que.pop(0)
        if(self.front==None):
            self.rear=self.front=0
        else:
            self.rear=self.limit-1

    def queue_rear(self):
        if(self.front==None):
            print("queue is empty")
        else:
            return self.que[self.rear]

    def queue_front(self):
        if(self.front==None):
            print("queue is empty")
        else:
            return self.que[self.front]

    def size_q(self):
        return self.size




q=queue()
q.en_queue("first")
q.en_queue("second")
q.en_queue("third")
q.en_queue("fourth")
q.en_queue("fifth")
print(q.queue_front())
print(q.queue_rear())
print(q.size_q())

