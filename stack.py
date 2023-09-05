from linkedlist import LinkedList, Node


# class Stack:
#     def __init__(self, values=None):
#         self.ll = LinkedList(values)
#         self._length = 0


#     def push(self, val):
#         self.ll.push(val)
#         self._length += 1

#     def pop(self):
#         if self.ll.head:
#             self._length -= 1
#             return self.ll.pop()
#         else:
#             raise ValueError("The stack is empty.")

#     def __len__(self):
#         return self.ll._length
class Stack:
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
            raise ValueError("The stack is empty.")
        return old_head


    def __len__(self):
        return self._length




  