
def breadth_first(tree):

    value_list = []
    values = []
    if value_list is None:
        return value_list
    if tree.root:
        value_list.append(tree.root)
    while value_list:
        node = value_list.pop(0)
        values.append(node.value)
        if node.left:
            value_list.append(node.left)
        if node.right:
            value_list.append(node.right)
    return values













# def breadth_first(tree):
#     if not tree.root:
#         return []
#
#     queue = [tree.root]
#     print(queue)
#     values = []
#
#     while queue:
#         current_node = queue.pop(0)
#         values.append(current_node.value)
#
#         if current_node.left:
#             queue.append(current_node.left)
#         if current_node.right:
#             queue.append(current_node.right)
#
#     return values
