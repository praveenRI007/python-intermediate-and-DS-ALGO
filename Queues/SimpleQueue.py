class Queue:
    def __init__(self):
        self.queue = list()

    def add_element(self,val):
        if val not in self.queue:
            self.queue.insert(0,val)
            return True
        return False

    def size(self):
        return len(self.queue)

    def remove_element(self):
        if len(self.queue)>0:
            return self.queue.pop()
        return "queue is empty !"


que = Queue()
que.add_element("January")
que.add_element("February")
que.add_element("March")
que.add_element("April")

print(que.queue)