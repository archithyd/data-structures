class Stack(object):
    def __init__(self,length=10):
        self.stk=[]
        self.length=length

    def stack_empty(self):
        return len(self.stk)<=0

    def push(self,data):
        if(len(self.stk)>=self.length):
            print("stack overflow")
        else:
            self.stk.append(data)

    def pop(self):
        if(len(self.stk)<=0):
            print("stack underflow")
            return
        else:
            self.stk.pop()


    def peek(self):
        if(len(self.stk)<=0):
            print("stack underflow")
            return
        else:
            print(self.stk)

    def stack_len(self):
        return len(self.stk)


#def palindrome(str):
 #   strStck=Stack()
  #  flag="false"
   # for char1 in str:
    #    strStck.push(char1)
    #for char in str:
     #   popped=strStck.pop()
      #  if(char==popped):
       #     flag="true"
        #else:
         #   flag="false"
   # return flag









myStack=Stack(5)
myStack.push(5)
myStack.push(6)
myStack.push(-2)
myStack.push(-3)
print(myStack.stack_len())
myStack.stack_pair()

