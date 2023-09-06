from linkedlist import LinkedList


class Stack:
    def __init__(self, values=None):
        self.storage = LinkedList(values)

    def push(self, val):
        self.storage.push(val)

    def pop(self):
        try:
            return self.storage.pop()
        except ValueError:
            raise ValueError("The stack is empty.")

    def __len__(self):
        return len(self.storage)
    
s = Stack([3, 6, 2])
print(s.storage)
