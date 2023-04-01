from data_structures.invalid_operation_error import InvalidOperationError


class Stack:
    """
    Sort of like a linked list, but vertical instead of horizontal
    """

    def __init__(self, top=None):
        self.top = top

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top:
            del_item = self.top
            top = self.top.next
            self.top = top
            return del_item.value
        raise InvalidOperationError('Method not allowed on empty collection')

    def is_empty(self):
        if self.top is None:
            return True
        return False

    def peek(self):
        if self.top:
            return self.top.value
        raise InvalidOperationError('Method not allowed on empty collection')


class Node:

    def __init__(self, value, _next=None):
        self.value = value
        self.next = _next


if __name__ == '__main__':
    s = Stack()
    s.peek()
    print(Exception.value)
