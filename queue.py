class Queue:
    def __init__(self):
        self.queue=list()

    def addf(self,data):
        if data not in self.queue:
            self.queue.insert(0,data)
            return True
        return False

    def disp(self):
        return len(self.queue)

    def pop(self):
        if(len(self.queue)>1):
            return self.queue.pop()
        return len(self.queue)    


a=Queue()
a.addf(19)
a.addf(5)
a.addf(56)
print(a.disp())
print("pooped element is",a.pop())