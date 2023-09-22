import pytest

from binheap import BinaryHeap


def test_push_min():
    binheap = BinaryHeap("min")

    binheap.push(4)

    assert binheap._storage == [4]
    assert len(binheap) == 1

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
    assert len(binheap) == 3

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
    assert binheap.pop() == 1
    assert binheap._storage == [3, 7, 5, 8]
    assert len(binheap) == 4


def test_pop_max():
    binheap = BinaryHeap("max", [9, 2, 50, 6, 32, 1])

    assert binheap._storage == [50, 32, 9, 2, 6, 1]
    assert binheap.pop() == 50
    assert binheap._storage == [32, 6, 9, 2, 1]


def test_pop_empty():
    binheap = BinaryHeap("min")

    assert binheap._storage == []
    with pytest.raises(ValueError) as exc_info:
        binheap.pop()
    assert exc_info.value.args[0] == "No items to pop."


def test_push_a():
    binheap = BinaryHeap("max")
    binheap.push(4)

    assert binheap._storage == [4]

    binheap.push(3)

    assert binheap._storage == [4, 3]

    binheap.push(5)

    assert binheap._storage == [5, 3, 4]

    binheap.push(8)

    assert binheap._storage == [8, 5, 4, 3]

    binheap.push(11)

    assert binheap._storage == [11, 8, 4, 3, 5]

    binheap.push(15)

    assert binheap._storage == [15, 8, 11, 3, 5, 4]


def test_push_b():
    binheap = BinaryHeap("max")
    binheap.push(11)

    assert binheap._storage == [11]

    binheap.push(3)

    assert binheap._storage == [11, 3]

    binheap.push(8)

    assert binheap._storage == [11, 3, 8]

    binheap.push(5)

    assert binheap._storage == [11, 5, 8, 3]

    binheap.push(4)

    assert binheap._storage == [11, 5, 8, 3, 4]

    binheap.push(15)

    assert binheap._storage == [15, 5, 11, 3, 4, 8]


def test_push_c():
    binheap = BinaryHeap("min")
    binheap.push(17)

    assert binheap._storage == [17]

    binheap.push(15)

    assert binheap._storage == [15, 17]

    binheap.push(9)

    assert binheap._storage == [9, 17, 15]

    binheap.push(6)

    assert binheap._storage == [6, 9, 15, 17]

    binheap.push(12)

    assert binheap._storage == [6, 9, 15, 17, 12]

    binheap.push(5)

    assert binheap._storage == [5, 9, 6, 17, 12, 15]

    binheap.push(1)

    assert binheap._storage == [1, 9, 5, 17, 12, 15, 6]


def test_heap_down_pop_a():
    binheap = BinaryHeap("max", [21, 20, 19])

    assert binheap.pop() == 21
    assert binheap._storage == [20, 19]


def test_heap_down_pop_b():
    binheap = BinaryHeap("max", [21, 19, 20])

    assert binheap.pop() == 21
    assert binheap._storage == [20, 19]


def test_peek():
    binheap = BinaryHeap("max")

    assert binheap.peek() == None

    binheap.push(5)

    assert binheap.peek() == 5


def test_bool_false():
    binheap = BinaryHeap("min")

    assert bool(binheap) == False


def test_bool_true():
    binheap = BinaryHeap("max", [21, 19, 20])

    assert bool(binheap) == True


def test_heap_up_pop_a():
    binheap = BinaryHeap("min", [1, 20, 18, 30])

    assert binheap.pop() == 1
    assert binheap._storage == [18, 20, 30]


def test_heap_up_pop_b():
    binheap = BinaryHeap("min", [1, 45, 8])

    assert binheap.pop() == 1
    assert binheap._storage == [8, 45]
