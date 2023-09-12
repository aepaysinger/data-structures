from doubly_linkedlist import Dll


class Deque:
    def __init__(self, values=None):
        self._storage = Dll(values)

    def append(self, val):
        self._storage.append(val)

    def appendleft(self, val):
        self._storage.push(val)

    def pop(self):
        try:
            return self._storage.shift()
        except ValueError:
            raise ValueError("Empty Deque")

    def popleft(self):
        try:
            return self._storage.pop()
        except ValueError:
            raise ValueError("Empty Deque")

    def peek(self):
        if self._storage:
            return self._storage.tail.value
        return None

    def peekleft(self):
        if self._storage:
            return self._storage.head.value
        return None

    def size(self):
        return len(self._storage)
