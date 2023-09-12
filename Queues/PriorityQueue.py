class Node:

  def __init__(self, info, priority):
    self.info = info
    self.priority = priority

# class for Priority queue
class PriorityQueue:

  def __init__(self):
    self.queue = list()
    # if you want you can set a maximum size for the queue

  def insert(self, node):
    # if queue is empty
    if self.size() == 0:
      # add the new node
      self.queue.append(node)
    else:
      # traverse the queue to find the right place for new node
      for x in range(0, self.size()):
        # if the priority of new node is greater
        if node.priority >= self.queue[x].priority:
          # if we have traversed the complete queue
          if x == (self.size()-1):
            # add new node at the end
            self.queue.insert(x+1, node)
          else:
            continue
        else:
          self.queue.insert(x, node)
          return True

  def delete(self):
    # remove the first node from the queue
    return self.queue.pop(0)

  def show(self):
    for x in self.queue:
      print(str(x.info)+" - "+str(x.priority))

  def size(self):
    return len(self.queue)


pq = PriorityQueue()

pq.insert(Node(1,10))
pq.insert(Node(2,9))
pq.insert(Node(3,8))
pq.insert(Node(4,7))
pq.insert(Node(1,1))
pq.insert(Node(2,2))
pq.insert(Node(3,5))
pq.insert(Node(4,11))

pq.show()
print('before delete')
pq.delete()

pq.show()