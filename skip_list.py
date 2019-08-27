class Skipnode:
    def __init__(self, height=None, data=None):
        self.data=data
        self.height=[None]*height

class Skiplist:

    def __init__(self):
        self.head=Skipnode()

    def __len__(self) :
        return self.len

    def updateList(self, elem):

        update = [None] * len(self.head.next)
        x = self.head

        for i in reversed (range (len (self.head.next))) :
            while x.next[i] != None and x.next[i].elem < elem:
                x = x.next[i]
            update[i] = x

        return update

    def find(self, elem, update=None) :
        if update == None :
            update = self.updateList (elem)
        if len (update) > 0 :
            candidate = update[0].next[0]
            if candidate != None and candidate.elem == elem :
                return candidate
        return None

    def insert(self, elem):
        node = Skipnode (self.randomHeight(), elem)

        while len (self.head.next) < len(node.next):
            self.head.next.append(None)

        update = self.updateList (elem)
        if (self.find (elem, update) == None):
            for i in range (len (node.next)) :
                node.next[i] = update[i].next[i]
                update[i].next[i] = node

    def remove(self, elem) :

        update = self.updateList (elem)
        x = self.find (elem, update)
        if x != None :
            for i in range (len (x.next)) :
                update[i].next[i] = x.next[i]
                if self.head.next[i] == None :
                    self.maxHeight -= 1
            self.len -= 1

    def printList(self) :
        for i in range (len (self.head.next) - 1, -1, -1) :
            x = self.head
            while x.next[i] != None :
                print
                x.next[i].elem,
                x = x.next[i]
            print('')

