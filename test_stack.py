import pytest

from stack import Stack


def test_stack():
    s = Stack([3, 6, 2])

    assert s._length == 3
    assert s.storage == [3, 6, 2]


def test_push():
    s = Stack([7, 3, "yes"])
    s.push("please")

    assert s._length == 4
    assert s.storage == [7, 3, "yes", "please"]


def test_pop():
    s = Stack([6, 2, 6, 1])

    assert s.pop() == 1
    assert s.storage == [6, 2, 6]
    assert s._length == 3


def test_pop_empty():
    s = Stack([])

    with pytest.raises(ValueError) as exc_info:
        s.pop()
    assert exc_info.value.args[0] == "The stack is empty."


def test_len():
    s = Stack(["go", "fight", "win"])

    assert len(s) == 3
