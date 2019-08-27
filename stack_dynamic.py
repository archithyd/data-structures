class Stack(object):
    def __init__(self,length=10):
        self.stk=length*[None]
        self.length=length

    def stack_empty(self):
        return len(self.stk)<=0

    def push(self,data):
        if(len(self.stk)>=self.length):
            self.resize()
        self.stk.append(data)

    def pop(self):
        if(len(self.stk)<=0):
            print("stack underflow")
        else:
            self.stk.pop()

    def peek(self):
        if(len(self.stk)<=0):
            print("stack underflow")
        else:
            print(self.stk)

    def length(self):
        return len(self.stk)

    def resize(self):
        Newlist=self.stk
        self.length=2*self.length
        self.stk=Newlist




myStack = Stack(5)
myStack.push (100)
myStack.push (150)
myStack.push (210)
myStack.push(102)
myStack.push(154)
myStack.push(204)
myStack.push(106)
myStack.push(154)
myStack.push(209)
myStack.push(108)
myStack.peek()
