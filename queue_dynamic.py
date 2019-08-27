class queue:
    def __init__(self,limit=5):
        self.que=[]
        self.front=None
        self.rear=None
        self.limit=limit
        self.size=0

    def en_queue(self,data):
        if(self.size>=self.limit):
            self.resize()
        else:
            self.que.append(data)
            print("enqueue",end=" " )
        if(self.front==None):
            self.front=self.rear=0
        else:
            self.rear=self.size
        self.size+=1

    def de_queue(self):
        if(self.size<=0):
            print("queue underflow")
        else:
            self.que.pop(0)
            print("dequeuet",end=" ")
        if(self.front==None):
            self.rear=self.front=0
        else:
            self.rear=self.size-1

    def front(self):
        if(self.front==None):
            print("queue is empty")
        else:
            return self.front

    def rear(self):
        if(self.front==None):
            print("stack is empty")
        else:
            return self.rear

    def size_q(self):
        return self.size

    def resize(self):
        New_queue=list(self.que)
        self.limit=2*self.limit
        self.que=New_queue

    def queue_show(self):
        return self.que


q=queue()
q.en_queue("first")
q.en_queue("second")
q.en_queue("third")
q.en_queue("fourth")
q.en_queue("fifth")
q.en_queue("sixth")
q.en_queue("seventh")
q.en_queue("eight")
q.en_queue("ninth")
print(q.queue_show())
q.de_queue()
q.de_queue()
q.de_queue()
q.de_queue()
q.de_queue()
q.de_queue()
q.de_queue()
q.de_queue()
print(q.queue_show())
