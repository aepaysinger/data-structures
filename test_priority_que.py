import pytest

from priority_que import PriorityQue


def test_priority_que():
    priority_q = PriorityQue([(0, 9), (3, 8), (1, 2)])

    assert priority_q._storage == [(0, 9), (1, 2), (3, 8)]
    assert priority_q._length == 3


def test_insert():
    priority_q = PriorityQue()
    priority_q.insert(6)

    assert priority_q._storage == [(0, 6)]

    priority_q.insert(9, 7)

    assert priority_q._storage == [(0, 6), (7, 9)]

    priority_q.insert(100, 2)

    assert priority_q._storage == [(0, 6), (2, 100), (7, 9)]

    priority_q.insert(3)

    assert priority_q._storage == [(0, 3), (0, 6), (2, 100), (7, 9)]
    assert priority_q._length == 4


def test_pop():
    priority_q = PriorityQue()
    priority_q.insert("this")
    priority_q.insert(8)
    priority_q.insert("yes", 99)

    assert priority_q._storage == [(0, 8), (0, "this"), (99, "yes")]
    assert priority_q._length == 3
    assert priority_q.pop() == "yes"

    priority_q.pop()
    priority_q.pop()

    with pytest.raises(IndexError) as exc_info:
        priority_q.pop()
    assert exc_info.value.args[0] == "No items to pop."
    assert priority_q._length == 0


def test_peek():
    priority_q = PriorityQue([(0, 3), (0, 6), (2, 100), (7, 9)])

    assert priority_q.peek() == 9
    assert priority_q._length == 4

    priority_q.pop()
    priority_q.pop()
    priority_q.pop()
    priority_q.pop()

    with pytest.raises(IndexError) as exc_info:
        priority_q.peek()
    assert exc_info.value.args[0] == "No items to see."
