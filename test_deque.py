import pytest

from deque import Deque


def test_peek_empty():
    deque = Deque()

    assert deque.peek() == None


def test_peek():
    deque = Deque([3, 6, 1, 4])

    assert deque.peek() == 3


def test_peekleft_empty():
    deque = Deque()

    assert deque.peekleft() == None


def test_peekleft():
    deque = Deque([5, 8, 1, 3, 2])

    assert deque.peekleft() == 2


def test_size_empty():
    deque = Deque()

    assert deque.size() == 0


def test_size():
    deque = Deque([55, 7, 2, 5])

    assert deque.size() == 4


def test_append():
    deque = Deque()
    deque.append(5)

    assert deque.peek() == 5
    assert deque.peekleft() == 5
    assert deque.size() == 1

    deque.append(6)
    deque.append(9)

    assert deque.peek() == 9
    assert deque.peekleft() == 5
    assert deque.size() == 3


def test_appendleft():
    deque = Deque()
    deque.appendleft(98)

    assert deque.peek() == 98
    assert deque.peekleft() == 98
    assert deque.size() == 1

    deque.appendleft(86)
    deque.appendleft(635)

    assert deque.peek() == 98
    assert deque.peekleft() == 635
    assert deque.size() == 3


def test_pop_empty():
    deque = Deque()

    with pytest.raises(ValueError) as exc_info:
        deque.pop()
    assert exc_info.value.args[0] == "Empty Deque"


def test_pop():
    deque = Deque([65, 8, 2, 5])

    assert deque.pop() == 65
    assert deque.peek() == 8
    assert deque.peekleft() == 5
    assert deque.size() == 3


def test_popleft_empty():
    deque = Deque()

    with pytest.raises(ValueError) as exc_info:
        deque.popleft()
    assert exc_info.value.args[0] == "Empty Deque"


def test_popleft():
    deque = Deque([4, 7, 2])

    assert deque.popleft() == 2
    assert deque.peek() == 4
    assert deque.peekleft() == 7
    assert deque.size() == 2
