class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, value):
        if not self.contains(value):
            self.size += 1
        if self.root:
            self.root._insert(value)
        else:
            self.root = Node(value)

    def contains(self, value):
        if self.root:
            return self.root.find(value)
        return False


class Node:
    def __init__(self, value):
        self.value = value
        self.right_child = None
        self.left_child = None

    def _insert(self, value):
        if self.value == value:
            raise Exception("value in tree")
        elif self.value > value:
            if self.left_child:
                self.left_child._insert(value)
            else:
                self.left_child = Node(value)
        else:
            if self.right_child:
                self.right_child._insert(value)
            else:
                self.right_child = Node(value)

    def find(self, value):
        if self.value == value:
            return True
        elif value < self.value and self.left_child != None:
            return self.left_child.find(value)
        elif value > self.value and self.right_child != None:
            return self.right_child.find(value)
        return False
