from linkedlist import LinkedList


class Stack:
    def __init__(self, values=None):
        self.ll = LinkedList(values)
        self._length = 0

    def push(self, val):
        self.ll.push(val)
        self._length += 1

    def pop(self):
        if self.ll.head:
            self._length -= 1
            return self.ll.pop()
        else:
            raise ValueError("The stack is empty.")

    def __len__(self):
        return self.ll._length
