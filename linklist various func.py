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

class LinkedList:

    def __init__(self, head = None):
       self.head = head
       self.length = 0

    def clear(self):
        current = self.head
        prev = self.head
        while(current.get_next()!=None):
            prev = current.get_next()
            del current.data
            current = prev


    def list_length(self):
        count = 0
        current = self.head

        while(current!=None):
            count += 1
            current = current.get_next()

        return count

    def insertion_at_begin(self, data):
        new_node = node()
        new_node.set_data(data)

        if(self.length==0):
            self.head = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node
        self.length += 1

    def insertion_at_end(self, data):
        new_node = node()
        new_node.set_data(data)
        current = self.head
        while (current.get_next!=None):
            current = current.set_next
        current.set_next=new_node
        self.length += 1

    def insertion_in_middle(self,pos,data):
        if (pos>self.length or pos<0):
            return None
        else:
            new_node = node()
            new_node.set_data(data)
            current1 = self.head
            current2 = self.head
            count = 0
            while(count < pos):
                count += 1
                current2 = current1
                current1 = current1.get_next()
            current2.set_next(new_node)
            new_node.set_next(current1)

    def deletion_at_begin(self):
        if(self.length==0):
            return None
        else:
            self.head = self.get_next()
            self.length -= 1

    def deletion_at_end(self):
        if(self.length==0):
            return None
        else:
            current = self.head
            current1 = self.head
            while(current.get_next()!=None):
                current1 = current
                current = current.get_next()
            current.set_next(None)
            self.length -= 1

    def delete_at_pos(self, pos):
        if(pos>self.length or pos<0):
            return None
        else:
            count = 0
            current1 = self.head
            current2 = self.head
            while(count<pos):
                count += 1
                if(count==pos):
                    current2.set_next(current1.get_node())
                    self.length -= 1
                else:
                    current2 = current1
                    current1 = current1.get_next()
            current2 = current1.get_next()
            self.length -= 1

    def delete_by_data(self, data):
        if (self.length==0):
            return None
        else:
            current1 = self.head
            current2 = self.head
            while(current1.get_data()!=data):
                current2 = current1
                current1 = current1.get_next()
            current2.set_next(current1.get_next())
            self.length -= 1

    def print_list(self):
        current = self.head
        while(current!=None):
            print(current.get_data())
            current = current.get_next()

    def find_nth_element_from_last(self, n) :
        if (n > self.length) :
            return None
        else :
            count = 0
            pos = self.length-n
            print(pos)
            current = self.head
            while (count <= pos) :
                count += 1
                current = current.get_next()
                print(current.get_data())
            return current.get_data()


if __name__ == '__main__':
    myList = LinkedList()
    print("Inserting")
    myList.insertion_at_begin(577757)
    myList.insertion_at_begin(1522)
    myList.insertion_at_begin(254)
    myList.insertion_at_begin (23457)
    #myList.insertion_in_middle(2,200)
    myList.print_list()
    print("reverse element")
    myList.reverse_pairs()
    myList.print_list()









