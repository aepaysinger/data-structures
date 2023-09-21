from binheap import BinaryHeap


class PriorityQueue:
    def __init__(self, values=None):
        self._storage = BinaryHeap("max")
        if values:
            for priority, value in values:
                self._storage.push(Node(priority, value))

    def __len__(self):
        return len(self._storage)

    def insert(self, value, priority=0):
        self._storage.push(Node(priority, value))

    def pop(self):
        try:
            return self._storage.pop().value
        except ValueError:
            raise ValueError("No items to pop.")

    def peek(self):
        return self._storage.peek().value if self._storage else None


class Node:
    def __init__(self, priority, value):
        self.value = value
        self.priority = priority

    def __gt__(self, other):
        return self.priority > other.priority
