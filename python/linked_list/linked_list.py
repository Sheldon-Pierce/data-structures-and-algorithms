class LinkedList:
    """
    A singly-linked list.

    Attributes:
        head (Node): The first node in the linked list
    """

    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        current_node = self.head
        lst = []
        if self.head is None:
            return str(self.head)
        else:
            while current_node is not None:
                lst.append('{{ {} }}'.format(current_node.value))
                current_node = current_node.next
            lst.append(str(None))
            return ' -> '.join(lst)


    def traverse_list(self):
        pass

    def some_method(self):
        # method body here
        pass

    def insert(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def includes(self, value):
        current = self.head
        lst = []
        while current:
            lst.append(current.value)
            current = current.next

        if value in lst:
            return True
        else:
            return False


class Node:

    def __init__(self, value, _next=None):
        self.value = value
        self._next = next


class TargetError:
    pass


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    linked_list.insert(4)
    linked_list.insert(5)
    print(linked_list)



