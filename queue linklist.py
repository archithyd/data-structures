class Node:
    def __init__(self, data=None, next=None):
        self.next = next
        self.data = data
        self.last = None

    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next

    def set_last(self, last):
        self.last = last

    def get_last(self):
        return self.last

    def get_next(self):
        return self.next

    def get_data(self):
        return self.data

    def has_next(self):
        return self.next is not None


class Queue(object):
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def en_queue(self, data):
        self.lastNode = self.front
        self.front = Node(data, self.front)
        if self.lastNode:
            self.lastNode.set_last(self.front)
        if self.rear is None:
            self.rear = self.front
        self.length += 1

    def de_queue(self):
        if self.front is None:
            print("queue empty")
        else:
            result = self.rear.get_data()
            self.rear = self.rear.last
            self.length -= 1
            return result

    def rear_q(self):
        if self.front is None:
            print("queue empty")
        else:
            data = self.rear.get_data()
            return data

    def front_q(self):
        if self.front is None:
            print("queue empty")
        else:
            data = self.front.get_data()
            return data

    def size(self):
        return self.length



if __name__=="__main__":
    que=Queue()
    que.en_queue("1")
    que.en_queue("2")
    que.en_queue("3")
    que.en_queue("4")
    que.en_queue("5")
    que.en_queue("6")
    que.en_queue("7")
    que.en_queue("8")
    que.en_queue("9")
    que.en_queue("10")
    print(que.front_q())
    print(que.rear_q())
    print(que.size())

