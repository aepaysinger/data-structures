import pytest

from que_ import Queue


def test_enqueue():
    que = Queue()

    que.enqueue(5)

    assert len(que) == 1
    assert que.peek() == None

    que.enqueue(6)

    assert que.peek() == 6
    assert len(que) == 2


def test_dequeue():
    que = Queue()

    with pytest.raises(ValueError) as exc_info:
        que.dequeue()
    assert exc_info.value.args[0] == "The queue is empty."

    que.enqueue(7)

    assert len(que) == 1
    assert que.dequeue() == 7


def test_peek():
    que = Queue()

    assert que.peek() == None

    que.enqueue(8)

    assert que.peek() == None
    assert len(que) == 1

    que.enqueue(6)

    assert que.peek() == 6
    assert len(que) == 2


def test_size():
    que = Queue([6, 8, 2, 1])

    assert que.size() == 4
