from stack.stack import Stack


class PseudoQueue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, value):
        self.s1.push(value)

    def dequeue(self):
        while self.s1.top:
            self.s2.push(self.s1.pop())
            print(self.s2.peek())
        top = self.s2.pop()
        while self.s2.top:
            self.s1.push(self.s2.pop())
        return top


if __name__ == '__main__':
    pass
