from linkedlist import LinkedList


class Stack:
    def __init__(self, values=None):
        self._storage = LinkedList(values)

    def push(self, val):
        self._storage.push(val)

    def pop(self):
        try:
            return self._storage.pop()
        except ValueError:
            raise ValueError("The stack is empty.")

    def __len__(self):
        return len(self._storage)
