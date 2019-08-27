class node:
    def __init__(self):
        self.data = None
        self.next = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def check_node(self):
        return self.next != None

class CLinklist:

    def __init__(self, head=None):
        self.head=head
        self.length=0

    def counting_node(self):
        if(self.head==None):
            return None
        else:
            current=self.head
            count=1
            while(current.get_next()==self.head):
                count+=1
                current=current.get_next()
        return count

    def printing_data(self):
        if(self.head==None):
            return None
        else:
            current=self.head
            while(current.get_next()!=self.head):
                current=current.get_next()
                print(current.get_data())

    def insert_at_begin(self,data):
        new_node=node()
        new_node.set_data(data)
        current = self.head
        while (current.get_next!=self.head):
            current = current.get_next()
        new_node.set_next (new_node)
        if (self.head == None):
            self.head = new_node;
        else:
            new_node.set_next(self.head)
            current.set_next(new_node)
            self.head=new_node


    def insert_at_end(self,data):
        new_node=node()
        new_node.set_data(data)
        current=self.head
        while(current.get_next()!=self.head):
            current=current.get_next()
        new_node.set_next(new_node)
        if(self.head==None):
            self.head=new_node;
        else:
            new_node.set_next(self.head)
            current.set_next(new_node)

    def delete_at_begin(self):
        if(self.head==None):
            print("empty")
            return
        else:
            current=self.head
            while(current.get_next!=self.head):
                current=current.get_next()
            current.set_next(self.head.get_next())
            self.head=self.head.get_next()
            return






myclist=CLinklist()
#myclist.insert_at_begin(30)
#print(myclist.counting_node())
#myclist.insert_at_end(40)
#myclist.printing_data()