class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        if value < current.data:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursive(current.right, value)

    def inorder_traversal(self):
        self._inorder(self.root)

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.data, end=" ")
            self._inorder(node.right)


# مثال تجريبي


bst = BinarySearchTree()

values = [16, 19, 21, 99, 71, 25, 30, 60, 40, 20, 50]

for v in values:
    bst.insert(v)

print("Inorder Traversal:")
bst.inorder_traversal()
