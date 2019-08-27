class node:
    def __init__(self):
        self.data=None
        self.ptrdiff=None

    def set_data(self, data):
        self.data=data

    def get_data(self):
        return self.data

    def set_ptrdiff(self,next,prev):
        self.ptrdiff=next^prev

    def get_ptrdiff(self):
        return self.ptrdiff

