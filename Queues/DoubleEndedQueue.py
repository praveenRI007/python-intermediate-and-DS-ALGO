class DoubleEndedQueue:
    def __init__(self):
        self.queue = list()

    def pop_left(self):
        del self.queue[0]

    def pop_right(self):
        self.queue.pop()

    def insert_left(self,val):
        if len(self.queue) != 0:
            self.queue.insert(0,val)
        else:
            self.queue.append(val)


    def insert_right(self,val):
        self.queue.append(val)


    def show(self):
        print([i for i in self.queue])

dqueue = DoubleEndedQueue()
dqueue.insert_right(1)
dqueue.insert_right(2)
dqueue.insert_right(3)
dqueue.insert_right(4)

dqueue.insert_left(5)
dqueue.insert_left(6)
dqueue.insert_left(7)
dqueue.insert_left(8)
dqueue.show()

dqueue.pop_left()

dqueue.show()