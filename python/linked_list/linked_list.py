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

    def append(self, value):
        current = self.head
        node = Node(value)
        while current.next:
            current = current.next
        current.next = node

    def insert_before(self, value, new_value):
        try:
            current = self.head
            prev = None
            node = Node(new_value)
            while current.value is not value:
                prev = current
                current = current.next
            node.next = current
            if prev:
                prev.next = node
            else:
                self.head = node
        except Exception:
            raise TargetError

    def insert_after(self, value, new_value):
        try:
            current = self.head
            next_node = current.next
            node = Node(new_value)
            while current.value is not value:
                current = current.next
            current.next = node
            node.next = next_node
        except Exception:
            raise TargetError

    def delete_value(self, value):
        current = self.head
        if current.value == value:
            self.head = self.head.next
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next


class Node:

    def __init__(self, value, _next=None):
        self.value = value
        self.next = _next


class TargetError(ValueError):
    pass


if __name__ == "__main__":
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    linked_list.insert("cucumber")

    linked_list.insert("Mango")

    linked_list.insert("Watermelon")

    linked_list.delete_value("cucumber")
    print(linked_list)



