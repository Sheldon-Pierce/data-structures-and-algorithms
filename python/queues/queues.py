from data_structures.invalid_operation_error import InvalidOperationError


class Queue:
    """
    Put docstring here
    """

    def __init__(self, front=None):
        self.front = front
        self.back = None

    def enqueue(self, value):
        node = Node(value)
        if not self.front:
            self.front = node
            self.back = node
        else:
            self.back.next = node
            self.back = node

    def dequeue(self):
        if self.front:
            temp = self.front
            self.front = self.front.next
            if not self.front:
                self.back = None
            return temp.value
        raise InvalidOperationError

    def peek(self):
        if self.front:
            return self.front.value
        raise InvalidOperationError

    def is_empty(self):
        return not self.front


class Node:

    def __init__(self, value, _next=None):
        self.value = value
        self.next = _next


if __name__ == '__main__':
    q = Queue()
    q.enqueue("apple")
    q.enqueue("banana")
    q.dequeue()
    q.peek()
