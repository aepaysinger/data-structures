import io, pytest, sys

from stack import Stack, LinkedList


def test_stack():
    s = Stack([3, 6, 2])

    captureOutput = io.StringIO()
    sys.stdout = captureOutput
    print(s.storage)
    sys.stdout = sys.__stdout__

    assert (
        captureOutput.getvalue() == "(2, 6, 3)\n"
    ), f"printed: {captureOutput.getvalue()}, instead of (2, 6, 3)"


def test_push():
    s = Stack([7, 3, "yes"])
    s.push("please")

    assert len(s.storage) == 4


def test_pop():
    s = Stack([6, 2, 6, 1])

    assert s.pop() == 1
    assert len(s.storage) == 3


def test_pop_empty():
    s = Stack([])

    with pytest.raises(ValueError) as exc_info:
        s.pop()
    assert exc_info.value.args[0] == "The stack is empty."


def test_len():
    s = Stack(["go", "fight", "win"])

    assert len(s) == 3
