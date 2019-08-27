import heapq

a=[1,34,12,89,56]
heapq.heapify(a)
print(a)

heapq.heappush(a,5)     #heap uses first in first out means queue

print(a)

heapq.heappop(a)    #heap queue =heapq
print(a)

heapq.heapreplace(a,4)
print(a)

heapq.heappushpop(a,9)
print(a)

print(heapq.nlargest(3,a))

print(heapq.nsmallest(2,a))


