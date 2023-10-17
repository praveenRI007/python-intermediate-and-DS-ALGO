class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    # add a new node
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next

    # view all nodes data
    def view(self):
        current_node = self.head
        while(current_node):
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("\n")

    # insert at particular index
    def insert_at(self,index,value):
        print(f"after inserting item at {index} with value {value}")
        node = Node(value)
        i = 0
        current_node = self.head
        if current_node is None:
            self.head = node
            return
        while current_node:
            if i == index - 1:
                node.next = current_node.next
                current_node.next = node
                return
            if index == 0:
                node.next = current_node
                self.head = node
                return

            current_node = current_node.next
            i += 1
        print("index not found")

    # update node
    def update_at(self, index, value):
        print(f"after updating item at {index} with {value}")
        i = 0
        current_node = self.head
        while current_node:
            if i == index:
                current_node.data = value
                return
            current_node = current_node.next
            i += 1
        print("index not found")

    # remove at last index
    def pop(self):
        print(" popping :")
        if self.head is None:
            return

        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next

        current_node.next = None

    # remove at index
    def remove_at(self, index):
        print(f"removing item at {index}")
        i = 0
        current_node = self.head
        if current_node is None:
            return

        while current_node:
            if index == 0:
                self.head = current_node.next
                return
            if i == index - 1:
                current_node.next = current_node.next.next
                return

            current_node = current_node.next
            i += 1
        print("index not found")

    def sort(self):
        print("after sort:")
        current_node = self.head
        max = None
        while current_node:
            max = current_node.data

    def insertionSort(self):

        # Initialize sorted linked list
        sorted = None

        # Traverse the given linked list and insert every
        # node to sorted
        current = self.head
        while (current != None):
            # Store next for next iteration
            next = current.next

            # insert current in sorted linked list
            sorted = self.__sortedinsert(sorted,current)

            # Update current
            current = next
        self.head = sorted

        # function to insert a new_node in a list. Note that this

    # function expects a pointer to head_ref as this can modify the
    # head of the input linked list (similar to push())
    def __sortedinsert(self,head_ref, new_node):

        current = None

        # Special case for the head end */
        if (head_ref == None or (head_ref).data >= new_node.data):

            new_node.next = head_ref
            head_ref = new_node

        else:

            # Locate the node before the point of insertion
            current = head_ref
            while (current.next != None and
                   current.next.data < new_node.data):
                current = current.next

            new_node.next = current.next
            current.next = new_node

        return head_ref




linkedlist = LinkedList()
linkedlist.append(3)
linkedlist.append(4)
linkedlist.append(1)
linkedlist.append(2)
linkedlist.append(5)

linkedlist.insert_at(1, 6)

# linkedlist.update_at(1,1)

linkedlist.view()

linkedlist.pop()

linkedlist.view()

linkedlist.remove_at(1)

linkedlist.view()

linkedlist.insertionSort()

linkedlist.view()


