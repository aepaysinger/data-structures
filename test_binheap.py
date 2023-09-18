import pytest

from binheap import BinaryHeap


def test_push_min():
    binheap = BinaryHeap("min")

    binheap.push(4)

    assert binheap._storage == [4]
    assert binheap._size == 1

    binheap.push(1)
    binheap.push(3)
    binheap.push(2)

    assert binheap._storage == [1, 2, 3, 4]
    assert binheap._parent_index(1) == 0
    assert binheap._left_child_index(0) == 1
    assert binheap._right_child_index(0) == 2
    assert binheap._has_parent(0) == False
    assert binheap._has_parent(3) == True
    assert binheap._has_left_child(0) == True
    assert binheap._has_left_child(2) == False
    assert binheap._has_right_child(0) == True
    assert binheap._has_right_child(2) == False
    assert binheap._parent_value(1) == 1
    assert binheap._left_child_value(0) == 2
    assert binheap._right_child_value(0) == 3


def test_push_max():
    binheap = BinaryHeap("max")
    binheap.push(49)
    binheap.push(20)
    binheap.push(35)

    assert binheap._storage == [49, 20, 35]
    assert binheap._size == 3

    binheap.push(40)

    assert binheap._storage == [49, 40, 35, 20]
    assert binheap._parent_index(1) == 0
    assert binheap._left_child_index(0) == 1
    assert binheap._right_child_index(0) == 2
    assert binheap._has_parent(0) == False
    assert binheap._has_parent(3) == True
    assert binheap._has_left_child(0) == True
    assert binheap._has_left_child(2) == False
    assert binheap._has_right_child(0) == True
    assert binheap._has_right_child(2) == False
    assert binheap._parent_value(1) == 49
    assert binheap._left_child_value(0) == 40
    assert binheap._right_child_value(0) == 35


def test_heap_up():
    binheap = BinaryHeap("min", [2, 3, 1, 4])

    assert binheap._storage == [1, 3, 2, 4]


def test_heap_down():
    binheap = BinaryHeap("max", [2, 3, 1])
    binheap._heap_down()
    assert binheap._storage == [3, 2, 1]


def test_pop_min():
    binheap = BinaryHeap("min", [5, 7, 1, 3, 8])

    assert binheap._storage == [1, 3, 5, 7, 8]

    binheap.pop()

    assert binheap._storage == [3, 5, 7, 8]
    assert binheap._size == 4


def test_pop_max():
    binheap = BinaryHeap("max", [9, 2, 50, 6, 32, 1])

    assert binheap._storage == [50, 32, 9, 2, 6, 1]

    binheap.pop()

    assert binheap._storage == [32, 9, 2, 6, 1]


def test_pop_empty():
    binheap = BinaryHeap("min")

    assert binheap._storage == []
    with pytest.raises(ValueError) as exc_info:
        binheap.pop()
    assert exc_info.value.args[0] == "Empty BinaryHeap, no items to pop."
