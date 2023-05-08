import copy


def fizz_buzz_tree(tree):
    if not tree:
        return None

    # current = tree.root
    fizz_buzz_copy_tree = copy.deepcopy(tree)

    def walk(root_node):
        current = root_node
        if current.value % 3 == 0 and current.value % 5 == 0:
            current.value = "FizzBuzz"
        elif current.value % 3 == 0:
            current.value = 'Fizz'
        elif current.value % 5 == 0:
            current.value = 'Buzz'
        else:
            current.value = str(current.value)

        for child in root_node.children:
            walk(child)

    walk(fizz_buzz_copy_tree.root)
    return fizz_buzz_copy_tree

