def find(self,list):
    if(self.head==None):
        return
    else:
        current=self.head
        while(current is None):
            current=current.get_next().get_next()
            if(current==None):
                return 1
            else:
                return 0

