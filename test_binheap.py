from binheap import BinaryHeap


def test_push():
    binheap = BinaryHeap("min")

    binheap.push(4)

    assert binheap.storage == [4]
    assert binheap.size == 1

    binheap.push(1)
    binheap.push(3)
    binheap.push(2)

    assert binheap.storage == [1, 2, 3, 4]
    assert binheap.parent_index(1) == 0
    assert binheap.left_child_index(0) == 1
    assert binheap.right_child_index(0) == 2
    assert binheap.has_parent(0) == False
    assert binheap.has_parent(3) == True
    assert binheap.has_left_child(0) == True
    assert binheap.has_left_child(2) == False
    assert binheap.has_right_child(0) == True
    assert binheap.has_right_child(2) == False
    assert binheap.parent_value(1) == 1
    assert binheap.left_child_value(0) == 2
    assert binheap.right_child_value(0) == 3


def test_heap_up():
    binheap = BinaryHeap("min", [2, 3, 1, 4])

    assert binheap.storage == [1, 3, 2, 4]


def test_heap_down():
    binheap = BinaryHeap("max", [2, 3, 1])
    binheap.heap_down()
    assert binheap.storage == [3, 2, 1]


def test_pop_min():
    binheap = BinaryHeap("min", [5, 7, 1, 3, 8])

    assert binheap.storage == [1, 3, 5, 7, 8]

    binheap.pop()

    assert binheap.storage == [3, 5, 7, 8]
    assert binheap.size == 4


def test_pop_max():
    binheap = BinaryHeap("max", [9, 2, 50, 6, 32, 1])

    assert binheap.storage == [50, 32, 9, 2, 6, 1]

    binheap.pop()

    assert binheap.storage == [32, 9, 2, 6, 1]
