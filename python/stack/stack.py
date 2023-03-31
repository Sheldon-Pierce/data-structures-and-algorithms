class Stack:
    """
    Put docstring here
    """

    def __init__(self, top=None):
        self.top = top

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        top = self.top
        self.top.next = top

    def some_method(self):
        # method body here
        pass


class Node:

    def __init__(self, value, _next=None):
        self.value = value
        self.next = _next


if __name__ == '__main__':
    s = Stack()
    s.push("apple")
    print(s.top.value)
    s.push("banana")
    print(s.top.value)
    s.push("cucumber")
    print(s.top.value)
