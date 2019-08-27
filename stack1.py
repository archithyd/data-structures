class Stack:
    def __init__(self):
        self.Stack=[]
        self.min_Stack=[]

    def peek1(self):
        return self.Stack

    def peek2(self):
        return self.min_Stack

    def stack_push(self,data):
         if(self.Stack==[] and self.min_Stack==[]):
            self.Stack.append(data)
            self.min_Stack.append(data)
         else:
            self.Stack.append(data)
            if(self.Stack[-1]<=self.min_Stack[-1]):
                self.min_Stack.append(data)
            else:
                self.min_Stack.append(self.min_Stack[-1])

    def stack_pop(self):
        x=self.Stack.pop()
        y=self.min_Stack.pop()
        print(x,y)



mystack=Stack()
mystack.stack_push(2)
mystack.stack_push(6)
mystack.stack_push(4)
mystack.stack_push(1)
mystack.stack_push(5)
mystack.stack_pop()
mystack.stack_pop()
mystack.stack_pop()
mystack.stack_pop()
mystack.stack_pop()
