from binheap import BinaryHeap

def test_push():
    binheap = BinaryHeap()

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
    binheap = BinaryHeap([2, 3, 1, 4])

    assert binheap.storage == [1, 3, 2, 4]

def test_heap_down():
    # binheap = BinaryHeap([2, 3, 1, 4])
    binheap = BinaryHeap([2, 3, 1])
    binheap.heap_down()
    assert binheap.storage == [3, 2, 1]