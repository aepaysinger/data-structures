import pytest

from graph import Graph


def test_add_node():
    graph = Graph()
    graph.add_node(4)

    assert graph._storage == {4: set()}
    assert graph.nodes() == [4]
    assert graph.edges() == []


def test_add_edge():
    graph = Graph()
    graph.add_edge(4, 6)

    assert graph.nodes() == [4, 6]
    assert graph.edges() == [(4, 6), (6, 4)]
    assert graph._storage == {4: {6}, 6: {4}}

    graph.add_edge(4, 9)

    assert graph.nodes() == [4, 6, 9]
    assert graph.edges() == [(4, 9), (4, 6), (6, 4), (9, 4)]
    assert graph._storage == {4: {6, 9}, 6: {4}, 9: {4}}

    graph.add_edge(20, 6)

    assert graph.nodes() == [4, 6, 9, 20]
    assert graph._storage == {
        4: {6, 9},
        6: {4, 20},
        9: {4},
        20: {6},
    }


def test_del_node():
    graph = Graph()
    graph.add_edge(4, 6)
    graph.add_edge(4, 9)
    graph.add_edge(20, 6)

    assert graph._storage == {
        4: {6, 9},
        6: {4, 20},
        9: {4},
        20: {6},
    }

    graph.del_node(6)

    assert graph._storage == {4: {9}, 9: {4}, 20: set()}
    assert graph.nodes() == [4, 9, 20]
    assert graph.edges() == [(4, 9), (9, 4)]
    with pytest.raises(ValueError) as exc_info:
        graph.del_node(5)
    assert exc_info.value.args[0] == "Node does not exist"


def test_del_edge():
    graph = Graph()
    graph.add_edge(6, 9)
    graph.add_edge(40, 2)
    graph.add_edge(6, 2)
    graph.add_node(27)

    assert graph._storage == {
        6: {9, 2},
        9: {6},
        40: {2},
        2: {40, 6},
        27: set(),
    }

    graph.del_edge(6, 2)

    assert graph._storage == {
        6: {9},
        9: {6},
        40: {2},
        2: {40},
        27: set(),
    }
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


def test_neighbors():
    graph = Graph()
    graph.add_edge(6, 9)
    graph.add_node(3)
    graph.add_edge(5, 2)
    graph.add_edge(6, 2)
    graph.add_node(27)

    assert graph._storage == {
        6: {9, 2},
        9: {6},
        3: set(),
        5: {2},
        2: {5, 6},
        27: set(),
    }
    assert graph.neighbors(2) == [5, 6]
    with pytest.raises(ValueError) as exc_info:
        graph.neighbors(8)
    assert exc_info.value.args[0] == "Value not in graph."


def test_adjacent():
    graph = Graph()
    graph.add_edge(4, 6)
    graph.add_edge(4, 9)
    graph.add_edge(20, 6)

    assert graph._storage == {
        4: {6, 9},
        6: {4, 20},
        9: {4},
        20: {6},
    }
    assert graph.adjacent(6, 4) == True
    assert graph.adjacent(20, 4) == False
    assert graph.adjacent(4, 6) == True
    with pytest.raises(ValueError) as exc_info:
        graph.adjacent(4, 15)
    assert exc_info.value.args[0] == "One of the values are not in the graph"


def test_depth_first_traversal():
    graph = Graph()
    graph.add_edge(4, 6)
    graph.add_edge(4, 9)
    graph.add_edge(4, 12)
    graph.add_edge(6, 20)
    graph.add_edge(6, 13)
    graph.add_edge(13, 7)
    graph.add_edge(9, 28)

    assert graph.depth_first_traversal(4) == [4, 12, 9, 28, 6, 20, 13, 7]


def test_breadth_first_traversall_a():
    graph = Graph()
    graph.add_edge(4, 6)
    graph.add_edge(4, 9)
    graph.add_edge(4, 12)
    graph.add_edge(6, 20)
    graph.add_edge(6, 13)
    graph.add_edge(13, 7)
    graph.add_edge(9, 28)

    assert graph.breadth_first_traversal(4) == [4, 9, 12, 6, 28, 13, 20, 7]


def test_breadth_first_traversall_b():
    graph = Graph()
    graph.add_edge(4, 6)
    graph.add_edge(4, 9)
    graph.add_edge(4, 12)
    graph.add_edge(6, 20)
    graph.add_edge(6, 13)
    graph.add_edge(13, 7)
    graph.add_edge(9, 28)

    assert graph.breadth_first_traversal(9) == [9, 4, 28, 12, 6, 13, 20, 7]
