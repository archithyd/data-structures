class Stack:
    def __init__(self):
        self.items=[]

    def push(self,data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items==[]

    def __str__(self):
        return str(self.items)

def postfixEval(infix_exp):
    operandStack=Stack()
    tokenlist=infix_exp.split()
    for token in tokenlist:
            if token in "0123456789":
                operandStack.push(int(token))
            else:
                operand2=operandStack.pop()
                operand1=operandStack.pop()
                result=domath(token,operand1,operand2)
                operandStack.push(result)
    return operandStack.pop()

def domath(op,op1,op2):
    if(op=="+"):
        return op1+op2
    if (op == "-") :
        return op1 - op2
    if(op=="*"):
        return op1*op2
    if(op=="/"):
        return op1/op2



print(postfixEval('123*+5-'))
