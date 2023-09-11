class Dll:
    def __init__(self, values=None):
        self.head = None
        self._length = 0
        self.tail = None
        if values:
            for value in values:
                self.head = Node(value, self.head, None)
                if self.head.next:
                    self.head.next.previous = self.head
                else:
                    self.tail = self.head
                self._length += 1

    def push(self, val):
        if self.head:
            self.head.previous = Node(val, self.head, None)
            self.head = self.head.previous
        else:
            self.head = Node(val, self.head, None)
            self.tail = self.head

        self._length += 1

    def append(self, val):
        current = self.head
        if current:
            while current:
                if current.next == None:
                    if current == self.head:
                        self.head.next = Node(val, None, self.head)
                        self.tail = self.head.next
                        self._length += 1
                        return
                    current.next = Node(val, None, current)
                    self.tail = current.next
                    self._length += 1
                    return
                current = current.next
        else:
            self.head = Node(val, self.head, None)
            self.tail = self.head
            self._length += 1

    def pop(self):
        old_head = self.head
        if self.head:
            self.head = self.head.next
            self.head.previous = None
            self._length -= 1
            return old_head.value

        raise ValueError("Empty Dll")

    def shift(self):
        if self.head:
            old_tail = self.tail
            self.tail = self.tail.previous
            self.tail.next = None
            self._length -= 1
            return old_tail.value
        else:
            raise ValueError("Empty Dll, no items to shift")

    def remove(self, val):
        current = self.head

        while current:
            if current.value == val:
                if current == self.head:
                    self.head = self.head.next
                    self.head.previous = None
                    self._length -= 1
                    return
                current = current.previous
                current.next = current.next.next
                if current.next == None:
                    self.tail = self.tail.previous
                if current == self.head:
                    current.next.previous = self.head
                else:
                    current.previous.next = current
                self._length -= 1
                return
            current = current.next

        raise ValueError("Value not in Dll")

    def __len__(self):
        return self._length


class Node:
    def __init__(self, value, next, previous):
        self.value = value
        self.next = next
        self.previous = previous
