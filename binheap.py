class BinaryHeap:
    def __init__(self, bin_type, values=None):
        self.storage = []
        self.size = 0
        self.bin_type = bin_type

        if values:
            for value in values:
                self.size += 1
                self.storage.append(value)
                if bin_type == "max":
                    self.heap_down()
                else:
                    self.heap_up()

    def parent_index(self, index):
        return (index - 1) // 2

    def left_child_index(self, index):
        return (2 * index) + 1

    def right_child_index(self, index):
        return (2 * index) + 2

    def has_parent(self, index):
        return self.parent_index(index) >= 0

    def has_left_child(self, index):
        return self.left_child_index(index) < self.size

    def has_right_child(self, index):
        return self.left_child_index(index) < self.size

    def parent_value(self, index):
        return self.storage[self.parent_index(index)]

    def left_child_value(self, index):
        return self.storage[self.left_child_index(index)]

    def right_child_value(self, index):
        return self.storage[self.right_child_index(index)]

    def heap_up(self):
        index = self.size - 1
        while (self.has_parent(index)) and self.parent_value(index) > self.storage[
            index
        ]:
            self.swap(self.parent_index(index), index)

    def heap_down(self):
        index = self.size - 1
        while (self.has_parent(index)) and self.parent_value(index) < self.storage[
            index
        ]:
            self.swap(self.parent_index(index), index)

    def swap(self, index1, index2):
        temp = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = temp

    def push(self, value):
        self.storage.append(value)
        self.size += 1
        if self.bin_type == "min":
            self.heap_up()
        else:
            self.heap_down()

    def pop(self):
        self.storage.pop(0)
        self.size -= 1
        if self.bin_type == "min":
            self.heap_up()
        else:
            self.heap_down()


# if __name__ == "__main__":
#     heap = BinaryHeap([2, 3, 1])
#     # print(heap.size)
#     # print(heap.heap_up())
#     print(heap.heap_down())
