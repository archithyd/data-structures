class node:
    def __init__(self, val=None):
        self.dataval=val
        self.next=None

class Slinklist:
    def __init__(self):
        self.headval=None

    def delete(self,data):
        pointer=self.headval
        if(pointer is not None):
            if(pointer.dataval==data):
                self.headval=pointer.next
                pointer=None
                return

        while(pointer is not None):
            if(pointer.dataval==data):
                break
            prev=pointer
            pointer=pointer.next
        prev.next = pointer.next
        pointer = None



    def search(self):
        printval=self.headval
        while printval is not None:
         print(printval.dataval)
         printval=printval.next

    def new(self,data):
        newnode=node(data)
        newnode.next=self.headval
        self.headval=newnode    

list1=Slinklist()
list1.new(7)
list1.new(5)
list1.new(50)
list1.search()
list1.delete(5)
list1.search()