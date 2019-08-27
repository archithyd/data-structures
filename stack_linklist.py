class node:
    def __init__(self):
        self.data=None
        self.next=None

    def set_data(self,data):
        self.data=data

    def get_data(self):
        return self.data

    def set_next(self,next):
        self.next=next

    def get_next(self):
        return self.next

    def has_next(self):
        return self.next!=None

class LinkStack(object):
    def __init__(self):
        self.head=None

    def push(self,data):
        new_node=node()
        new_node.set_data(data)
        if(self.head==None):
            self.head=new_node
        else:
            new_node.set_next(self.head)
            self.head=new_node

    def pop(self):
        if(self.head is None):
            return
        else:
            current=self.head
            self.head=self.head.get_next()
            current.set_next(None)

    def peek(self):
        if(self.head==None):
            return
        else:
            return self.head.get_data()



my_stack=LinkStack()
my_stack.push(10)
print(my_stack.peek())
my_stack.push(100)
print(my_stack.peek())
my_stack.push(1000)
print(my_stack.peek())
my_stack.push(10000)
print(my_stack.peek())
my_stack.pop()
print(my_stack.peek())
my_stack.pop()
print(my_stack.peek())
my_stack.pop()
print(my_stack.peek())
