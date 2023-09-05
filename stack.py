class Stack():
    def __init__(self, values=None):
        self.storage = []
        self._length = 0
        if values:
            for value in values:
                self.storage.append(value)
                self._length += 1

    def push(self, val):
        self.storage.append(val)
        self._length += 1

    def pop(self):
        if self.storage:
            self._length -= 1
            return self.storage.pop()
        else:
            raise ValueError("The stack is empty.")
        
    def __len__(self):
        return self._length