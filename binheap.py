class BinaryHeap:
    def __init__(self, bin_type, values=None):
        self._storage = []
        self._size = 0
        self.bin_type = bin_type

        if values:
            for value in values:
                self._size += 1
                self._storage.append(value)
                if bin_type == "max":
                    self._heap_down()
                else:
                    self._heap_up()

    def _parent_index(self, index):
        return (index - 1) // 2

    def _left_child_index(self, index):
        return (2 * index) + 1

    def _right_child_index(self, index):
        return (2 * index) + 2

    def _has_parent(self, index):
        return self._parent_index(index) >= 0

    def _has_left_child(self, index):
        return self._left_child_index(index) < self._size

    def _has_right_child(self, index):
        return self._left_child_index(index) < self._size

    def _parent_value(self, index):
        return self._storage[self._parent_index(index)]

    def _left_child_value(self, index):
        return self._storage[self._left_child_index(index)]

    def _right_child_value(self, index):
        return self._storage[self._right_child_index(index)]

    def _heap_up(self):
        index = self._size - 1
        while (self._has_parent(index)) and self._parent_value(index) > self._storage[
            index
        ]:
            self._swap(self._parent_index(index), index)

    def _heap_down(self):
        index = self._size - 1
        while (self._has_parent(index)) and self._parent_value(index) < self._storage[
            index
        ]:
            self._swap(self._parent_index(index), index)

    def _swap(self, index1, index2):
        temp = self._storage[index1]
        self._storage[index1] = self._storage[index2]
        self._storage[index2] = temp

    def push(self, value):
        self._storage.append(value)
        self._size += 1
        if self.bin_type == "min":
            self._heap_up()
        else:
            self._heap_down()

    def pop(self):
        if self._storage:
            self._storage.pop(0)
            self._size -= 1
            if self.bin_type == "min":
                self._heap_up()
            else:
                self._heap_down()
        else:
            raise ValueError("Empty BinaryHeap, no items to pop.")