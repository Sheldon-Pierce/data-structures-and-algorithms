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

    def delete_value(self, del_value):
        current = self.head
        if current.value == del_value:
            self.head = self.head.next
        while current.next:
            if current.next.value == del_value:
                current.next = current.next.next
                return
            current = current.next

    def kth_from_end(self, k):
        if k < 0:
            raise TargetError
        try:
            lst = []
            current = self.head
            while current:
                lst.insert(0, current.value)
                current = current.next
            return lst[k]
        except Exception:
            raise TargetError

    @staticmethod
    def zip_lists(link_list_1, link_list_2):
        if not link_list_1.head:
            return link_list_2
        if not link_list_2.head:
            return link_list_1

        new_list = LinkedList()
        head_1 = link_list_1.head
        head_2 = link_list_2.head
        while head_1 and head_2:
            new_list.insert(head_1.value)
            new_list.insert(head_2.value)
            head_1 = head_1.next
            head_2 = head_2.next
        print(new_list)

        while head_1:
            new_list.insert(head_1.value)
            head_1 = head_1.next
        while head_2:
            new_list.insert(head_2.value)
            head_2 = head_2.next

        reversed_new_list = LinkedList()
        some_number = new_list.head
        while some_number:
            reversed_new_list.insert(some_number.value)
            some_number = some_number.next
        print(reversed_new_list)

        return reversed_new_list


class Node:

    def __init__(self, value, _next=None):
        self.value = value
        self.next = _next


class TargetError(ValueError):
    pass


if __name__ == "__main__":
    list_a = LinkedList()
    for value in reversed([1, 2, 3]):
        list_a.insert(value)
    list_b = LinkedList()
    for value in reversed(["a", "b", "c"]):
        list_b.insert(value)
    print(list_a)
    print(list_b)
    LinkedList.zip_lists(list_a, list_b)



