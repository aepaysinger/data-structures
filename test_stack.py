import io
import sys

import pytest

from stack import Stack


def test_push():
    s = Stack([7, 3, "yes"])
    s.push("please")

    assert len(s) == 4


def test_pop():
    s = Stack([6, 2, 6, 1])

    assert s.pop() == 1
    assert len(s) == 3
    assert s.pop() == 6
    assert len(s) == 2


def test_pop_empty():
    s = Stack()

    with pytest.raises(ValueError) as exc_info:
        s.pop()
    assert exc_info.value.args[0] == "The stack is empty."


def test_len():
    s = Stack(["go", "fight", "win"])

    assert len(s) == 3
