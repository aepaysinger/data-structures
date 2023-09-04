import pytest

from linkedlist import LinkedList, Node


def test_push():
    ll = LinkedList()
    ll.push(3)
    ll.push(4)

    assert ll.head.value == 4
    assert ll.head.next.value == 3


def test_pop_empty():
    ll = LinkedList()

    with pytest.raises(ValueError) as e_info:
        ll.pop()
    assert e_info.value.args[0] == "Empty List"


def test_pop():
    ll = LinkedList([1, 2, 3])
    ll.pop()
    assert ll.head.value == 2

    assert ll.pop() == 2


def test_size():
    ll = LinkedList([3, 7, 4, 1])

    assert ll.size() == 4
    ll.pop()
    ll.pop()
    assert ll.size() == 2


def test_search_there():
    ll = LinkedList([3, 6, 2, 4])

    assert ll.search(6) == 6
    assert ll.head.next.next.value == 6


def test_serach_not_there():
    ll = LinkedList([6, 8, 2, 4, 5])

    assert ll.search(9) == None


def test_search_head_tail_middle():
    ll = LinkedList([3, 2, 1])

    assert ll.search(1) == 1
    assert ll.search(3) == 3
    assert ll.search(2) == 2


def test_remove_head():
    ll = LinkedList([3, 6, 4])
    ll.remove(ll.head)
    assert ll.head.value == 6
    assert ll.head.next.value == 3
    assert ll._length == 2


def test_remove_middle():
    ll = LinkedList([3, 6, 4])
    ll.remove(ll.head.next)
    assert ll.head.value == 4
    assert ll.head.next.value == 3
    assert ll._length == 2


def test_remove_last():
    ll = LinkedList([7, 6, 4, 2])
    ll.remove(ll.head.next.next.next)

    assert ll.head.value == 2
    assert ll.head.next.next.next == None
    assert ll._length == 3


def test_remove_not_there():
    ll = LinkedList([5, 3, 7])

    with pytest.raises(ValueError) as e_info:
        ll.remove(ll.head.next.next.next)
    assert e_info.value.args[0] == "node not in LinkedList"


def test_print():
    ll = LinkedList([5, 27, 8])

    assert print(ll) == "(5, 27, 8)"


def test_len():
    ll = LinkedList([5, 8, 4])

    assert len(ll) == 3
