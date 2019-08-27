import string

class Generictree:
    def __init__(self, parent, value=None):
        self.parent = parent
        self.value = value
        self.childlist=[]
        if parent is None:
            self.birthlist=0
        else:
            self.birthlist=len(parent.childlist)
            parent.childlist.append(self)

    def n_child(self):
        return len(self.childlist)

    def nth_child(self, n):
        return self.childlist[n]


