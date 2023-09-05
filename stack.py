from linkedlist import LinkedList


class Stack:
    def __init__(self, values=None):
        self.storage = LinkedList(values)

    def push(self, val):
        self.storage.push(val)

    def pop(self):
        if self.storage:
            return self.storage.pop()

        raise ValueError("The stack is empty.")

    def __len__(self):
        return self.storage._length
