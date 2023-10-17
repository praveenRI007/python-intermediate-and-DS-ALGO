class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def ConvertsortedArrayToBST(arr):
    if not arr:
        return None

    mid = len(arr)//2

    root = Node(arr[mid])

    root.left = ConvertsortedArrayToBST(arr[:mid])

    root.right = ConvertsortedArrayToBST(arr[mid+1:])

    return root


def deleteNode(root, k):
    # Base case
    if root is None:
        return root

    # Recursive calls for ancestors of
    # node to be deleted
    if root.data > k:
        root.left = deleteNode(root.left, k)
        return root
    elif root.data < k:
        root.right = deleteNode(root.right, k)
        return root

    # We reach here when root is the node
    # to be deleted.

    # If one of the children is empty
    if root.left is None:
        temp = root.right
        del root
        return temp
    elif root.right is None:
        temp = root.left
        del root
        return temp

    # If both children exist
    else:

        succParent = root

        # Find successor
        succ = root.right
        while succ.left is not None:
            succParent = succ
            succ = succ.left

        # Delete successor.  Since successor
        # is always left child of its parent
        # we can safely make successor's right
        # right child as left of its parent.
        # If there is no succ, then assign
        # succ.right to succParent.right
        if succParent != root:
            succParent.left = succ.right
        else:
            succParent.right = succ.right

        # Copy Successor Data to root
        root.data = succ.data

        # Delete Successor and return root
        del succ
        return root

def findbinarysearch(root,key):
    if not root or root.data == key:
        return "key found !"

    if root.data < key:
        return findbinarysearch(root.right,key)

    return findbinarysearch(root.left,key)




def insert(root, key):
    if root is None:
        return Node(key)
    else:
        # doesnt allow duplicates
        if root.data == key:
            return root
        elif root.data < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


# Compute the height of a tree--the number of nodes
# along the longest path from the root node down to
# the farthest leaf node
def height(node):
    if node is None:
        return 0
    else:

        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)

        # Use the larger one
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1


# Function to  print level order traversal of tree
def printLevelOrder(root):
    h = height(root)
    for i in range(1, h + 1):
        printCurrentLevel(root, i)


# Print nodes at a current level
def printCurrentLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        printCurrentLevel(root.left, level - 1)
        printCurrentLevel(root.right, level - 1)

def preorder(node):
    if not node:
        return None

    print(node.data,end=" ")
    preorder(node.left)
    preorder(node.right)


arr = [1,2,3,4,5,6,7]
root = ConvertsortedArrayToBST(arr)
insert(root,5)
deleteNode(root,5)
print(findbinarysearch(root,2))
print("Preorder traversal of sorted array to BST:")
preorder(root)
print("\n")
print("level order traversal of BST:")
printLevelOrder(root)


# 1.Depth First Search or DFS
#     Inorder Traversal
#     Preorder Traversal
#     Postorder Traversal

# 2.Level Order Traversal or Breadth First Search or BFS