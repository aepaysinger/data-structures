import pytest

from stack import Stack


# def test_stack():
#     s = Stack([3, 6, 2])

#     assert s.ll._length == 3
#     assert s.ll.head.value == 2


# def test_push():
#     s = Stack([7, 3, "yes"])
#     s.push("please")

#     assert s.ll._length == 4



# def test_pop():
#     s = Stack([6, 2, 6, 1])

#     assert s.pop() == 1
#     assert s.ll._length == 3


# def test_pop_empty():
#     s = Stack([])

#     with pytest.raises(ValueError) as exc_info:
#         s.pop()
#     assert exc_info.value.args[0] == "The stack is empty."


# def test_len():
#     s = Stack(["go", "fight", "win"])

#     assert len(s) == 3

def test_stack():
    s = Stack([3, 6, 4])

    assert s.head.value == 4
    assert s._length == 3


def test_stack_push():
    s = Stack([5, 3, 8])
    s.push("number")

    assert s.head.value == "number"
    assert s._length == 4


def test_pop():
    s = Stack([5, 8, 2])
    s.pop()

    assert s.head.value == 8
    assert s._length == 2


def test_len():
    s = Stack([5, 7, 2])

    assert len(s) == 3