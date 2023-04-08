from binary_tree.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Put docstring here
    """

    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node(value)

        def walk(root):
            if value < root.value:
                if root.left is None:
                    root.left = Node(value)
                else:
                    walk(root.left)

            if value > root.value:
                if root.right is None:
                    root.right = Node(value)
                else:
                    walk(root.right)

        walk(self.root)

    def contains(self, value):
        if self.root is None:
            return False

        def walk(root):
            if root is None:
                return False
            if value < root.value:
                return walk(root.left)
            if value > root.value:
                return walk(root.right)
            if value == root.value:
                return True
        return walk(self.root)

