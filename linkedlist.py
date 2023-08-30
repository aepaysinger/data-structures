class LinkedList():
    def __init__(self, values=None):
        self.head = None
        self._length = 0
        self.values = values

        if values:
            for value in values:
                self.head = Node(value, self.head)
                self._length +=1

    def push(self, value):
        self.head = Node(value, self.head)
        self._length += 1

    def pop(self):
        old_head = self.head
        if self._length > 0:
            self.head = self.head.next
            self._length -= 1
        else:
            raise ValueError("Nothing")
        return old_head.value
    
    def size(self):
        return self._length
                

    def search(self, value):
        for val in self.values:
            if val == value:
                return value
            
        return None
    
    def remove(self, node):
        pass

            


class Node():
    def __init__(self, value, next):
        self.value = value
        self.next = next

   