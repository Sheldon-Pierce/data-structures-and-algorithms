class BinaryTree:
    """
    Put docstring here
    """

    def __init__(self, root=None):
        self.root = root

    def pre_order(self, values=[]):

        def walk(input_node, value_list):
            if not input_node:
                return
            value_list.append(input_node.value)
            walk(input_node.left, value_list)
            walk(input_node.right, value_list)

        walk(self.root, values)
        return values

    def in_order(self, values=[]):

        def walk(input_node, value_list):
            if not input_node:
                return
            walk(input_node.left, value_list)
            value_list.append(input_node.value)
            walk(input_node.right, value_list)

        walk(self.root, values)
        return values

    def post_order(self, values=[]):

        def walk(input_node, value_list):
            if not input_node:
                return
            walk(input_node.left, value_list)
            walk(input_node.right, value_list)
            value_list.append(input_node.value)

        walk(self.root, values)
        return values

    def find_maximum_value(self):

        def walk(input_node):
            if not input_node:
                return -999999
            left_val = walk(input_node.left)
            right_val = walk(input_node.right)
            return max(input_node.value, left_val, right_val)
        return walk(self.root)


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
