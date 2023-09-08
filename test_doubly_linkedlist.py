import pytest

from doubly_linkedlist import Dll


def test_dll():
    dll = Dll([4, 6, 8, 2])

    assert dll.head.value == 2
    assert dll.head.next.value == 8
    assert dll.head.next.next.previous.value == 8
    assert dll._length == 4


def test_push():
    dll = Dll([5, 7, 8])
    dll.push(3)

    assert dll.head.value == 3
    assert dll._length == 4
    assert dll.head.previous == None
    assert dll.head.next.value == 8


def test_append():
    dll = Dll([])
    dll.append(33)

    assert dll.head.value == 33
    assert dll.head.next == None
    assert dll._length == 1

    dll.append(8)

    assert dll.head.value == 33
    assert dll.head.next.value == 8
    assert dll._length == 2


def test_pop():
    dll = Dll([5, 7, 1, 0])

    assert dll.pop() == 0
    assert dll.head.value == 1
    assert dll._length == 3
    assert dll.head.next.next.previous.value == 7
    assert dll.head.previous == None


def test_pop_empty():
    dll = Dll([])

    with pytest.raises(ValueError) as exc_info:
        dll.pop()
    assert exc_info.value.args[0] == "Empty Dll"


def test_shift():
    dll = Dll([4, 8, 1])

    assert dll.shift() == 4
    assert dll._length == 2
    assert dll.head.next.value == 8
    assert dll.head.next.previous.value == 1


def test_shift_empty():
    dll = Dll([])

    with pytest.raises(ValueError) as exc_info:
        dll.shift()
    assert exc_info.value.args[0] == "Empty Dll, no items to shift"


def test_remove_head():
    dll = Dll([3, 7, 5])
    dll.remove(5)

    assert dll.head.value == 7
    assert dll._length == 2


def test_remove_middle():
    dll = Dll([8, 5, 8, 2])
    dll.remove(8)

    assert dll.head.value == 2
    assert dll.head.next.value == 5
    assert dll.head.next.next.value == 8
    assert dll._length == 3
    assert dll.head.next.previous.value == 2


def test_remove_tail():
    dll = Dll([3, 7, 8])
    dll.remove(3)

    assert dll.head.value == 8
    assert dll.head.next.value == 7
    assert dll.head.next.next == None
    assert dll._length == 2


def test_remove_not_present():
    dll = Dll([5, 8, 2])

    with pytest.raises(ValueError) as exc_info:
        dll.remove("No")
    assert exc_info.value.args[0] == "Value not in Dll"


def test_len():
    dll = Dll([7, 3, 9, 1])

    assert len(dll) == 4
