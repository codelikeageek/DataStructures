class QueueNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def enqueue(self, val):
        newNode = QueueNode(val)
        if self.size == 0:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        self.size += 1
        return self

    def dequeue(self):
        if self.size == 0:
            return
        popped = self.first
        if self.size == 1:
            self.first = None
            self.last = None
        else:
            self.first = popped.next
            popped.next = None
        self.size -= 1
        return popped.val

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        newNode = Node(val)
        if not self.root:
            self.root = newNode
        else:
            current = self.root
            while True:
                if val < current.val:
                    if not current.left:
                        current.left = newNode
                        break
                    current = current.left
                elif val > current.val:
                    if not current.right:
                        current.right = newNode
                        break
                    current = current.right
        return self.root

    def breadthFirstSearch(self, root):
        queue = Queue()
        result = []
        if not root:
            return None
        queue.enqueue(root)
        while queue.size != 0:
            current = queue.dequeue()
            result.append(current.val)
            if current.left:
                queue.enqueue(current.left)
            if current.right:
                queue.enqueue(current.right)
        return result

    def dfsPreOrder(self, root):
        result = []
        def traverse(root):
            if root:
                result.append(root.val)
            if root.left:
                traverse(root.left)
            if root.right:
                traverse(root.right)
        traverse(root)
        return result

    def dfsInOrder(self, root):
        result = []
        def traverse(root):
            if root.left:
                traverse(root.left)
            if root:
                result.append(root.val)
            if root.right:
                traverse(root.right)
        traverse(root)
        return result

    def dfsPostOrder(self, root):
        result = []
        def traverse(root):
            if root.left:
                traverse(root.left)
            if root.right:
                traverse(root.right)
            if root:
                result.append(root.val)
        traverse(root)
        return result

bst = BinarySearchTree()

print(bst.insert(10))
print(bst.insert(2))
print(bst.insert(5))
print(bst.insert(3))
print(bst.insert(15))
print(bst.insert(18))
print(bst.insert(1))
print(bst.insert(6))
print(bst.insert(12))
print(bst.insert(14))
print(bst.insert(0))
print(bst.breadthFirstSearch(bst.root))
print(bst.dfsPreOrder(bst.root))
print(bst.dfsInOrder(bst.root))
print(bst.dfsPostOrder(bst.root))

#                  10
#          2               15 
#      1       5       12      18
#   0       3     6       14




