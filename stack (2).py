class Stack:
    def __init__(self):
        self.Stack=[]
        self.min_stack=[]

    def Stack_one(self,x):
        self.Stack.append(x)
        if not self.Stack<=self.min_stack:
            self.min_stack.append(x)

    def pop1(self):
        x=self.Stack.pop()
        if(x==self.min_stack):
            y=self.min_stack.pop()
        print(x)

    def Stack_min(self):
        return self.min_stack[-1]



mylist=Stack()
mylist.Stack_one(2)
mylist.Stack_one(6)
mylist.Stack_one(4)
mylist.Stack_one(1)
mylist.Stack_one(5)
mylist.pop1()
mylist.pop1()
print(mylist.Stack_min())
print(mylist.Stack_min())

