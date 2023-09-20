import pytest

from priority_que import PriorityQueue


def test_priority_que():
    priority_q = PriorityQueue([(9, 0), (8, 3), (2, 1)])

    assert priority_q.peek() == 0
    assert len(priority_q) == 3


def test_insert():
    priority_q = PriorityQueue()
    priority_q.insert(6)

    assert priority_q.peek() == 6

    priority_q.insert(9, 7)

    assert priority_q.peek() == 9

    priority_q.insert(100, 2)

    assert priority_q.peek() == 9

    priority_q.insert(10, 8)

    assert priority_q.peek() == 10
    assert len(priority_q) == 4

    priority_q.insert(21, 8)

    assert priority_q.peek() == 10


def test_pop():
    priority_q = PriorityQueue()
    priority_q.insert("this")
    priority_q.insert(8)
    priority_q.insert("yes", 99)

    assert len(priority_q) == 3
    assert priority_q.peek() == "yes"
    assert priority_q.pop() == "yes"

    priority_q.pop()
    priority_q.pop()

    with pytest.raises(ValueError) as exc_info:
        priority_q.pop()
    assert exc_info.value.args[0] == "No items to pop."
    assert len(priority_q) == 0


def test_peek():
    priority_q = PriorityQueue([(0, 3), (0, 6), (2, 100), (7, 9)])

    assert priority_q.peek() == 9
    assert len(priority_q) == 4

    priority_q.pop()
    priority_q.pop()
    priority_q.pop()
    priority_q.pop()

    with pytest.raises(ValueError) as exc_info:
        priority_q.peek()
    assert exc_info.value.args[0] == "No items to see."
