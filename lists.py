list1=["1","2","3","4","5"]   #array 1
print(list1[1])                 #array printed
list1[2]=80                     #array updation
print(list1[0:5])
print(len(list1))
list2=["1","2","3","4"]
print(list1+list2)              #append
print(list1*2)                  #repetion
for x in list1:
    print(x)
print(list2[0:5])
del list2                       #deletion
print("deleted")