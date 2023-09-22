import pytest

from graph import Graph


def test_add_node():
    graph = Graph()
    graph.add_node(4)

    assert graph._storage == {4: set()}
    assert graph.nodes() == [4]
    assert graph.edges() == [set()]


def test_add_edge():
    graph = Graph()
    graph.add_edge(4, 6)

    assert graph.nodes() == [4, 6]
    assert graph.edges() == [{(4, 6)}, {(6, 4)}]
    assert graph._storage == {4: {(4, 6)}, 6: {(6, 4)}}


    graph.add_edge(4, 9)

    assert graph.nodes() == [4, 6, 9]
    assert graph.edges() == [{(4, 6), (4, 9)}, {(6, 4)}, {(9, 4)}]
    assert graph._storage == {4: {(4, 6), (4, 9)}, 6: {(6, 4)}, 9: {(9, 4)}}

    graph.add_edge(20, 6)

    assert graph.nodes() == [4, 6, 9, 20]
    assert graph._storage == {4: {(4, 6), (4, 9)}, 6: {(6, 4), (6, 20)}, 9: {(9, 4)}, 20: {(20, 6)}}


def test_del_node():
    graph = Graph()
    graph.add_edge(4, 6)
    graph.add_edge(4, 9)
    graph.add_edge(20, 6)

    assert graph._storage == {4: {(4, 6), (4, 9)}, 6: {(6, 4), (6, 20)}, 9: {(9, 4)}, 20: {(20, 6)}}

    graph.del_node(6)

    assert graph._storage == {4: {(4, 9)}, 9: {(9, 4)}, 20: set()}
    assert graph.nodes() == [4, 9, 20]
    assert graph.edges() == [{(4, 9)}, {(9,4)}, set()]
    with pytest.raises(ValueError) as exc_info:
        graph.del_node(5)
    assert exc_info.value.args[0] == "Node does not exist"


def test_del_edge():
    graph = Graph()
    graph.add_edge(6, 9)
    graph.add_edge(40, 2)
    graph.add_edge(6, 2)
    graph.add_node(27)

    assert graph._storage == {6: {(6, 9), (6, 2)}, 9:{(9, 6)}, 40: {(40, 2)}, 2: {(2, 40), (2, 6)}, 27: set()}
    
    graph.del_edge(6, 2)

    assert graph._storage == {6: {(6, 9)}, 9:{(9, 6)}, 40: {(40, 2)}, 2: {(2, 40)}, 27: set()}
    with pytest.raises(ValueError) as exc_info:
        graph.del_edge(2, 6)
    assert exc_info.value.args[0] == "Edge does not exist."


def test_has_node_true():
    graph = Graph()
    graph.add_edge(6, 9)
    graph.add_node(3)
    graph.add_edge(5, 2)
    graph.add_edge(6, 2)
    graph.add_node(27)

    assert graph.has_node(6) == True
    assert graph.has_node(9) == True
    assert graph.has_node(27) == True


def test_has_node_false():
    graph = Graph()
    graph.add_edge(6, 9)
    graph.add_node(3)
    graph.add_edge(5, 2)
    graph.add_edge(6, 2)
    graph.add_node(27)

    assert graph.has_node(7) == False

