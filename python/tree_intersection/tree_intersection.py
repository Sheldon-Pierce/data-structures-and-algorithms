from binary_tree.binary_tree import BinaryTree, Node


def tree_intersection(tree_a, tree_b):
    """
    Finds the common values between two binary trees using sets.
    """
    if not tree_a.root or not tree_b.root:
        return []

    values_a = set()
    common_values = set()

    # Traverse tree_a and add values to the set
    def traverse(node):
        if node:
            values_a.add(node.value)
            traverse(node.left)
            traverse(node.right)

    traverse(tree_a.root)

    # Traverse tree_b and check if each value exists in the set
    def traverse_and_find_common(node):
        if node:
            if node.value in values_a:
                common_values.add(node.value)
            traverse_and_find_common(node.left)
            traverse_and_find_common(node.right)

    traverse_and_find_common(tree_b.root)

    return list(common_values)



