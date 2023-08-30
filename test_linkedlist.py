import pytest

from linkedlist import LinkedList


def test_push():
    ll = LinkedList()
    ll.push(3)
    ll.push(4)

    assert ll.head.value == 4
    assert ll.head.next.value == 3

def test_pop_empty():
    ll = LinkedList([])

    with pytest.raises(ValueError) as e_info:
        ll.pop()
    assert e_info.value.args[0] == "Nothing"


def test_pop():
    ll = LinkedList([1, 2, 3])
    ll.pop()
    assert ll.head.value == 2
    
    assert ll.pop() == 2


def test_size():
    ll = LinkedList([3,7,4,1])

    assert ll.size() == 4
    ll.pop()
    ll.pop()
    assert ll.size() == 2


def test_search_there():
    ll = LinkedList([3,6,2,4])
    
    assert ll.search(6) == 6


def test_serach_not_there():
    ll = LinkedList([6,8,2,4,5])

    assert ll.search(9) == None