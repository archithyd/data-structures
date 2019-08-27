class node:
    def __init__(self, data=None, next=None, prev=None ):
        self.data = data
        self.next = next
        self.prev = prev

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def set_prev(self, prev):
        self.prev = prev

    def get_prev(self):
        return self.prev

    def has_next(self):
        return self.next != None

    def has_prev(self):
        return self.prev != None


class Double_Linklist:

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.length = 0

    def list_length(self):
        count = 0
        current = self.head

        while (current != None):
            count += 1
            current = current.get_next()

        return count

    def print_dlink(self):
        current = self.head
        while(current!=None):
            print(current.data)
            current = current.get_next()

    def print_dlink_rev(self):
        current=self.tail
        while(current!=None):
            print(current.get_data())
            current=current.get_prev()

    def insert_begin(self, data):
        new_node = node(data,None,None)
        if(self.head==None):
            new_node.set_next(None)
            new_node.set_prev(None)
            self.head = self.tail = new_node
        else:
            new_node.set_next(self.head)
            new_node.set_prev(None)
            self.head = new_node


    def insert_end(self, data):
        new_node = node(data,None,None)
        current = self.head
        if(self.head == None):
            self.head = self.tail = new_node
        else:
            while(current.get_next()!=None):
                current = current.get_next()
            current.set_next(new_node)
            new_node.set_prev(current)
            new_node.set_next(None)
            self.tail = new_node

    def insert_data_after(self,data,data1):
        new_node = node(data,None,None)
        current = self.head
        if(self.head==None):
            self.head = self.tail = new_node
        else:
            while(current.get_data()!=data1):
                current = current.get_next()
            new_node.set_next(current.get_next())
            current.set_next(new_node)
            new_node.set_prev(current)

    def insert_data_pos(self,data,pos):
        if(pos>self.length or pos<0):
            return None
        else:
            new_node = node(data, None, None)
            current1 = self.head
            current2 = self.head
            count = 0
            while(count<pos):
                count += 1
                current2 = current1
                current1 = current1.get_next()
            current2.set_next(new_node)
            new_node.set_prev(current2)
            current1.set_prev(new_node)
            new_node.set_next(current1)

    def deletion_at_begin(self):
        if(self.head==None):
            return None
        else:
            current=self.head
            self.head=current.get_next()
            self.head.set_prev(None)
            current.set_next(None)

    def deletion_at_end(self):
        if(self.head==None):
            return None
        else:
            current=self.head
            currentp=self.head
            while(current.get_next()!=None):
                currentp=current
                current=current.get_next()
            currentp.set_next(None)
            current.set_prev(None)

    def deletion_by_data(self, data):
        if(self.head==None):
            return None
        else:
            if(self.head.get_data()==data):
                self.head=None
            else:
                currentn=self.head
                currentp=self.head
                while(currentn.get_data()!=data):
                    currentp=currentn
                    currentn=currentn.get_next()
                currentp.set_next(currentn.get_next())
                currentn.set_prev(None)


if __name__ == '__main__':
    myDLink = Double_Linklist()
    print("insertion")
    myDLink.insert_begin(50)
    myDLink.insert_end(60)
    myDLink.insert_data_after(40,50)
    print("printing")
    myDLink.print_dlink()
    myDLink.deletion_at_begin()
    myDLink.deletion_by_data(40)
    myDLink.deletion_at_end()
    print("after deletion")
    myDLink.print_dlink()



