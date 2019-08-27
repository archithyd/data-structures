class Stack:
    def __init__(self):
        self.stack=[]

    def add(self,data):
        self.stack.append(data)
        
    def peep(self):
        return(self.stack[0])

    def pop(self):
        print(self.stack.pop())

stack=Stack()
stack.add(5)
stack.add(6)
stack.add(7)
print(stack.peep())
stack.pop()