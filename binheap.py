class BinaryHeap:
    def __init__(self, bin_type, values=None):
        self._storage = []
        self._bin_type = bin_type

        if values:
            for value in values:
                self._storage.append(value)
                if self._bin_type == "max":
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
        return self._left_child_index(index) < len(self)

    def _has_right_child(self, index):
        return self._right_child_index(index) < len(self)

    def _parent_value(self, index):
        return self._storage[self._parent_index(index)]

    def _left_child_value(self, index):
        return self._storage[self._left_child_index(index)]

    def _right_child_value(self, index):
        return self._storage[self._right_child_index(index)]

    def _heap_up(self):
        index = len(self) - 1
        while (self._has_parent(index)) and self._parent_value(index) > self._storage[
            index
        ]:
            self._swap(self._parent_index(index), index)
            index = self._parent_index(index)

    def _heap_down(self):
        index = len(self) - 1
        while (self._has_parent(index)) and self._parent_value(index) < self._storage[
            index
        ]:
            self._swap(self._parent_index(index), index)
            index = self._parent_index(index)

    def _heap_down_pop(self):
        index = 0
        while index < len(self._storage):
            if self._has_left_child(index):
                if self._has_right_child(index):
                    if (
                        self._left_child_value(index) > self._right_child_value(index)
                        and self._left_child_value(index) > self._storage[index]
                    ):
                        self._swap(self._left_child_index(index), index)
                    elif (
                        self._right_child_value(index) > self._left_child_value(index)
                        and self._right_child_value(index) > self._storage[index]
                    ):
                        self._swap(self._right_child_index(index), index)
                else:
                    if self._left_child_value(index) > self._storage[index]:
                        self._swap(self._left_child_index(index), index)
                    else:
                        return
            index += 1

    def _heap_up_pop(self):
        index = 0
        while index < len(self._storage):
            if self._has_left_child(index):
                if self._has_right_child(index):
                    print(self._storage, index, self._has_right_child(index))
                    if (
                        self._left_child_value(index) < self._right_child_value(index)
                        and self._left_child_value(index) < self._storage[index]
                    ):
                        self._swap(self._left_child_index(index), index)
                    elif (
                        self._right_child_value(index) < self._left_child_value(index)
                        and self._right_child_value(index) < self._storage[index]
                    ):
                        self._swap(self._right_child_index(index), index)
                else:
                    if self._left_child_value(index) < self._storage[index]:
                        self._swap(self._left_child_index(index), index)
                    else:
                        return
            index += 1

    def _swap(self, index1, index2):
        temp = self._storage[index1]
        self._storage[index1] = self._storage[index2]
        self._storage[index2] = temp

    def push(self, value):
        self._storage.append(value)
        if self._bin_type == "min":
            self._heap_up()
        else:
            self._heap_down()

    def pop(self):
        try:
            old_top = self._storage[0]
        except IndexError:
            raise ValueError("No items to pop.")
        self._storage[0] = self._storage[-1]
        self._storage = self._storage[:-1]
        if self._bin_type == "min":
            self._heap_up_pop()
        else:
            self._heap_down_pop()
        return old_top

    def peek(self):
        try:
            return self._storage[0]
        except IndexError:
            return None

    def __len__(self):
        return len(self._storage)

    def __bool__(self):
        return True if self._storage else False
