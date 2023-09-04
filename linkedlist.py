class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self._length = 0

        if values:
            for value in values:
                self.head = Node(value, self.head)
                self._length += 1

    def push(self, value):
        self.head = Node(value, self.head)
        self._length += 1

    def pop(self):
        old_head = self.head
        if self._length > 0:
            self.head = self.head.next
            self._length -= 1
        else:
            raise ValueError("Empty List")
        return old_head.value

    def size(self):
        return self._length

    def search(self, val):
        current = self.head
        count = 0
        if self.head:
            while count < self._length:
                if current.value == val:
                    return current.value
                current = current.next
                count += 1
        return None

    def remove(self, node):
        current = self.head
        previous = None
        while current:
            if current == node:
                if current == self.head:
                    self.head = self.head.next
                    self._length -= 1
                    return
                previous.next = current.next
                self._length -= 1
                return
            previous = current
            current = current.next
        raise ValueError("node not in LinkedList")

    def display(self):
        statement = "("
        current = self.head
        while current:
            statement += str(current.value) + ", "
            current = current.next
        return statement[:-2] + ")"

    def __len__(self):
        return self._length

    def __repr__(self):
        return self.display()


class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next
