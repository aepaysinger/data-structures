import pytest
from binary_search_tree import BinarySearchTree


def test_binary_search_tree_insert():
    tree = BinarySearchTree()
    tree.insert(8)
    tree.insert(2)
    tree.insert(20)

    assert tree.root.value == 8
    assert tree.root.left_child.value == 2
    assert tree.root.right_child.value == 20
    assert tree.size == 3

    with pytest.raises(Exception) as exc_info:
        tree.insert(2)
    assert exc_info.value.args[0] == "value in tree"


def test_binary_search_tree_contains():
    tree = BinarySearchTree()
    tree.insert(50)
    tree.insert(15)
    tree.insert(69)
    tree.insert(5)
    tree.insert(21)

    assert tree.root.value == 50
    assert tree.root.left_child.left_child.value == 5
    assert tree.root.right_child.value == 69
    assert tree.size == 5
    assert tree.contains(15) == True
    assert tree.contains(70) == False
