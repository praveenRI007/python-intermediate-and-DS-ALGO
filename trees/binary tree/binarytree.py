# Python program to create a Complete Binary Tree from
# its linked list representation

# Linked List node
class ListNode:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None


# Binary Tree Node structure
class BinaryTreeNode:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


""" Inorder traversal of a binary tree"""


def inorder(temp):
    if (not temp):
        return

    inorder(temp.left)
    print(temp.data, end=" ")
    inorder(temp.right)


"""function to insert element in binary tree """


def insert(temp, data):
    if not temp:
        root = BinaryTreeNode(data)
        return
    q = []
    q.append(temp)

    # Do level order traversal until we find
    # an empty place.
    while len(q):
        temp = q[0]
        q.pop(0)

        if not temp.left:
            temp.left = BinaryTreeNode(data)
            break
        else:
            q.append(temp.left)

        if not temp.right:
            temp.right = BinaryTreeNode(data)
            break
        else:
            q.append(temp.right)

        # Class to convert the linked list to Binary Tree


def deleteDeepest(root, d_node):
    q = []
    q.append(root)
    while (len(q)):
        temp = q.pop(0)
        if temp is d_node:
            temp = None
            return
        if temp.right:
            if temp.right is d_node:
                temp.right = None
                return
            else:
                q.append(temp.right)
        if temp.left:
            if temp.left is d_node:
                temp.left = None
                return
            else:
                q.append(temp.left)


# function to delete element in binary tree


def deletion(root, key):
    if root == None:
        return None
    if root.left == None and root.right == None:
        if root.key == key:
            return None
        else:
            return root
    key_node = None
    q = []
    q.append(root)
    temp = None
    while (len(q)):
        temp = q.pop(0)
        if temp.data == key:
            key_node = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    if key_node:
        x = temp.data
        deleteDeepest(root, temp)
        key_node.data = x
    return root


####################################################################################################################################
class Conversion:

    # Constructor for storing head of linked list
    # and root for the Binary Tree
    def __init__(self, data=None):
        self.head = None
        self.root = None

    def push(self, new_data):

        # Creating a new linked list node and storing data
        new_node = ListNode(new_data)

        # Make next of new node as head
        new_node.next = self.head

        # Move the head to point to new node
        self.head = new_node

    def convertList2Binary(self):

        # Queue to store the parent nodes
        q = []

        # Base Case
        if self.head is None:
            self.root = None
            return

        # 1.) The first node is always the root node,
        # and add it to the queue
        self.root = BinaryTreeNode(self.head.data)
        q.append(self.root)

        # Advance the pointer to the next node
        self.head = self.head.next

        # Until the end of linked list is reached, do:
        while (self.head):

            # 2.a) Take the parent node from the q and
            # and remove it from q
            parent = q.pop(0)  # Front of queue

            # 2.c) Take next two nodes from the linked list.
            # We will add them as children of the current
            # parent node in step 2.b.
            # Push them into the queue so that they will be
            # parent to the future node
            leftChild = None
            rightChild = None

            leftChild = BinaryTreeNode(self.head.data)
            q.append(leftChild)
            self.head = self.head.next
            if (self.head):
                rightChild = BinaryTreeNode(self.head.data)
                q.append(rightChild)
                self.head = self.head.next

            # 2.b) Assign the left and right children of parent
            parent.left = leftChild
            parent.right = rightChild

    def inorderTraversal(self, root):
        if (root):
            self.inorderTraversal(root.left)
            print(root.data, end=" ")
            self.inorderTraversal(root.right)

    def postorderTraversal(self, root):
        if (root):
            self.postorderTraversal(root.left)
            self.postorderTraversal(root.right)
            print(root.data, end=" ")

    def preorderTraversal(self, root):
        if (root):
            print(root.data, end=" ")
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)


# Driver Program to test above function

# Object of conversion class
conv = Conversion()
conv.push(36)
conv.push(30)
conv.push(25)
conv.push(15)
conv.push(12)
conv.push(10)

conv.convertList2Binary()

print("Inorder Traversal of the constructed Binary Tree is:")
conv.inorderTraversal(conv.root)
print("\n")
print("preorder Traversal of the constructed Binary Tree is:")
conv.preorderTraversal(conv.root)
print("\n")
print("postorder Traversal of the constructed Binary Tree is:")
conv.postorderTraversal(conv.root)
print("\n")

####################################################################################################################################
print(
    "####################################################################################################################################")
root = BinaryTreeNode(10)
root.left = BinaryTreeNode(11)
root.left.left = BinaryTreeNode(7)
root.right = BinaryTreeNode(9)
root.right.left = BinaryTreeNode(15)
root.right.right = BinaryTreeNode(8)

print("Inorder traversal before insertion:", end=" ")
inorder(root)

key = 12
insert(root, key)

print()
print("Inorder traversal after insertion:", end=" ")
inorder(root)
print("\n");
print("The tree before the deletion: ", end="")
inorder(root)
key = 11
root = deletion(root, key)
print("\n");
print("The tree after the deletion: ", end="")
inorder(root)
