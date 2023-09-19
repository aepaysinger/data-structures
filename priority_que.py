import bisect


class PriorityQue:
    def __init__(self, values=None):
        self._storage = []
        self._length = 0
        if values:
            for value in values:
                bisect.insort_left(self._storage, value, key=lambda pair: pair[0])
                self._length += 1

    def insert(self, value, priority=0):
        bisect.insort_left(self._storage, (priority, value), key=lambda pair: pair[0])
        self._length += 1

    def pop(self):
        if self._storage:
            self._length -= 1
        try:
            return self._storage.pop()
        except IndexError:
            raise IndexError("No items to pop.")

    def peek(self):
        try:
            return self._storage[-1]
        except IndexError:
            raise IndexError("No items to see.")
