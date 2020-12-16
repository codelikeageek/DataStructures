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
                if val > current.val:
                    if not current.right:
                        current.right = newNode
                        break
                    current = current.right
                elif val <= current.val:
                    if not current.left:
                        current.left = newNode
                        break
                    current = current.left
        return self.root

    def find(self, val):
        if not self.root:
            return None
        if self.root.val == val:
            return self.root
        else:
            current = self.root
            while True:
                if val == current.val:
                    return current
                elif val < current.val:
                    if not current.left:
                        return None
                    current = current.left
                elif val > current.val:
                    if not current.right:
                        return None
                    current = current.right
        return None

    def minValueNode(self, root):
        while root.left:
            root = root.left
        return root




            

bst = BinarySearchTree()
print(bst.insert(18).val)
print(bst.insert(12).val)
print(bst.insert(9).val)
print(bst.insert(21).val)
print(bst.insert(35).val)
print(bst.insert(15).val)
print(bst.insert(19).val)
print(bst.find(21).val, bst.find(21).left.val, bst.find(21).right.val)
print(bst.minValueNode(bst.root).val)