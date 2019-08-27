import linklist


def merge_list(self,list1,list2):
    list3=linklist.node
    while(list1!=None and list2!=None):
        if(list1.get_data<list2.get_data()):
            list3.set_data(list1)
            list1.get_next()
        else:
            list3.set_data(list2)
            list2.get_next()
    if(list1==None):
        list3.set_data(list2)
    else:
        list3.set_data(list1)
