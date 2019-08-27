def reverse_pairs(self,list):
    current1=self.head
    current2=self.head
    x=0
    while(current1 is not None and current2 is not None):
        current1=current2.get_next()
        x=current1.get_data()
        current1.set_data(current2)
        current2.set_data(x)
        current2=current1.get_next()



