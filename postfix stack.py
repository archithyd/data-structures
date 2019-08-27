class Stack:
    def __init__(self):
        self.stk=[]

    def push(self,data):
        self.stk.append(data)

    def pop(self):
        self.stk.pop()

    def peek(self):
        return self.stk[-1]

    def __str__(self):
        return str(self.iteam)

    def is_empty(self):
        return self.data==[]

def infix_to_post(infixexp):
    prec={}
    prec["*"]=3
    prec["/"]=3
    prec["+"]=2
    prec["-"]=2
    prec["("]=1
    opstack=Stack
    postfix={}
    tokenlist=infixexp.split()

    for token in tokenlist:
        if(token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789" ):
            postfix.append(token)
        elif token=="(":
            opstack.push(token)
        elif token==")":
            return


    return postfix


print(infix_to_post("A+B"))