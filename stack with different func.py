class Stack:
    def __init__(self,iteams=[]):
        self.stack=iteams

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return not self.stack

    def length(self):
        return len(self.stack)

    def return_stack(self):
        return self.stack

    def __repr__(self):
        return "Stack{0}".format(self.stack)

def reverse_elements(stack1):
    stack2=Stack()
    l=len(stack1)
    for i in range (l):
        stack2.push(stack1.pop())
    return stack2


if __name__=="__main__":
    list=Stack()
    list.push(1)
    list.push(2)
    list.push(3)
    print(list.length())
    x=(list.return_stack())
    print(x)
    print(reverse_elements(x))