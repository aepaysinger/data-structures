import pytest

from weighted_graph import WeightedGraph


def test_add_node():
    graph = WeightedGraph()
    graph.add_node(4)

    assert graph._storage == {4: set()}
    assert graph.nodes() == [4]
    assert graph.edges() == []


def test_add_edge():
    graph = WeightedGraph()
    graph.add_edge(4, 6, 21)

    assert graph.nodes() == [4, 6]
    assert graph.edges() == [(4, 6), (6, 4)]
    assert graph._storage == {4: {(6, 21)}, 6: {(4, 21)}}

    graph.add_edge(4, 9, 1)

    assert graph.nodes() == [4, 6, 9]
    assert graph.edges() == [(4, 9), (4, 6), (6, 4), (9, 4)]
    assert graph._storage == {4: {(6, 21), (9, 1)}, 6: {(4, 21)}, 9: {(4, 1)}}

    graph.add_edge(20, 6, 80)

    assert graph.nodes() == [4, 6, 9, 20]
    assert graph._storage == {
        4: {(6, 21), (9, 1)},
        6: {(4, 21), (20, 80)},
        9: {(4, 1)},
        20: {(6, 80)},
    }


def test_del_node():
    graph = WeightedGraph()
    graph.add_edge(4, 6, 21)
    graph.add_edge(4, 9, 1)
    graph.add_edge(20, 6, 80)

    assert graph._storage == {
        4: {(6, 21), (9, 1)},
        6: {(4, 21), (20, 80)},
        9: {(4, 1)},
        20: {(6, 80)},
    }

    graph.del_node(6)

    assert graph._storage == {4: {(9, 1)}, 9: {(4, 1)}, 20: set()}
    assert graph.nodes() == [4, 9, 20]
    assert graph.edges() == [(4, 9), (9, 4)]
    with pytest.raises(ValueError) as exc_info:
        graph.del_node(5)
    assert exc_info.value.args[0] == "Node does not exist"


def test_del_edge():
    graph = WeightedGraph()
    graph.add_edge(6, 9, 12)
    graph.add_edge(40, 2, 17)
    graph.add_edge(6, 2, 9)
    graph.add_node(27)

    assert graph._storage == {
        6: {(9, 12), (2, 9)},
        9: {(6, 12)},
        40: {(2, 17)},
        2: {(40, 17), (6, 9)},
        27: set(),
    }

    graph.del_edge(6, 2)

    assert graph._storage == {
        6: {(9, 12)},
        9: {(6, 12)},
        40: {(2, 17)},
        2: {(40, 17)},
        27: set(),
    }
    with pytest.raises(ValueError) as exc_info:
        graph.del_edge(2, 6)
    assert exc_info.value.args[0] == "Edge does not exist."


def test_has_node_true():
    graph = WeightedGraph()
    graph.add_edge(6, 9, 67)
    graph.add_node(3)
    graph.add_edge(5, 2, 7)
    graph.add_edge(6, 2, 54)
    graph.add_node(27)

    assert graph.has_node(6) == True
    assert graph.has_node(9) == True
    assert graph.has_node(27) == True


def test_has_node_false():
    graph = WeightedGraph()
    graph.add_edge(6, 9, 67)
    graph.add_node(3)
    graph.add_edge(5, 2, 7)
    graph.add_edge(6, 2, 54)
    graph.add_node(27)

    assert graph.has_node(7) == False


def test_neighbors():
    graph = WeightedGraph()
    graph.add_edge(6, 9, 67)
    graph.add_node(3)
    graph.add_edge(5, 2, 7)
    graph.add_edge(6, 2, 54)
    graph.add_node(27)

    assert graph._storage == {
        6: {(9, 67), (2, 54)},
        9: {(6, 67)},
        3: set(),
        5: {(2, 7)},
        2: {(5, 7), (6, 54)},
        27: set(),
    }
    assert graph.neighbors(2) == [6, 5]
    with pytest.raises(ValueError) as exc_info:
        graph.neighbors(8)
    assert exc_info.value.args[0] == "Value not in graph."


def test_adjacent():
    graph = WeightedGraph()
    graph.add_edge(4, 6, 21)
    graph.add_edge(4, 9, 1)
    graph.add_edge(20, 6, 80)

    assert graph._storage == {
        4: {(6, 21), (9, 1)},
        6: {(4, 21), (20, 80)},
        9: {(4, 1)},
        20: {(6, 80)},
    }
    assert graph.adjacent(6, 4) == True
    assert graph.adjacent(20, 4) == False
    assert graph.adjacent(4, 6) == True
    with pytest.raises(ValueError) as exc_info:
        graph.adjacent(4, 15)
    assert exc_info.value.args[0] == "One of the values are not in the graph"


def test_depth_first_traversal():
    graph = WeightedGraph()
    graph.add_edge(4, 6, 18)
    graph.add_edge(4, 9, 76)
    graph.add_edge(4, 12, 13)
    graph.add_edge(6, 20, 10)
    graph.add_edge(6, 13, 54)
    graph.add_edge(13, 7, 24)
    graph.add_edge(9, 28, 3)

    assert graph._storage == {
        4: {(6, 18), (9, 76), (12, 13)},
        6: {(4, 18), (20, 10), (13, 54)},
        9: {(4, 76), (28, 3)},
        12: {(4, 13)},
        20: {(6, 10)},
        13: {(6, 54), (7, 24)},
        7: {(13, 24)},
        28: {(9, 3)},
    }
    assert (
        graph.depth_first_traversal(4)[1] == 6
        or graph.depth_first_traversal(4)[1] == 9
        or graph.depth_first_traversal(4)[1] == 12
    )
    if graph.depth_first_traversal(4)[1] == 6:
        assert (
            graph.depth_first_traversal(4)[2] == 20
            or graph.depth_first_traversal(4)[2] == 13
        )


def test_breadth_first_traversall_a():
    graph = WeightedGraph()
    graph.add_edge(4, 6, 18)
    graph.add_edge(4, 9, 76)
    graph.add_edge(4, 12, 13)
    graph.add_edge(6, 20, 10)
    graph.add_edge(6, 13, 54)
    graph.add_edge(13, 7, 24)
    graph.add_edge(9, 28, 3)

    assert graph._storage == {
        4: {(6, 18), (9, 76), (12, 13)},
        6: {(4, 18), (20, 10), (13, 54)},
        9: {(4, 76), (28, 3)},
        12: {(4, 13)},
        20: {(6, 10)},
        13: {(6, 54), (7, 24)},
        7: {(13, 24)},
        28: {(9, 3)},
    }

    assert (
        graph.breadth_first_traversal(4)[1] == 6
        or graph.breadth_first_traversal(4)[1] == 9
        or graph.breadth_first_traversal(4)[1] == 12
    )
    assert (
        graph.breadth_first_traversal(4)[4] == 20
        or graph.breadth_first_traversal(4)[4] == 13
        or graph.breadth_first_traversal(4)[4] == 28
    )
    assert graph.breadth_first_traversal(4)[-1] == 7


def test_breadth_first_traversall_b():
    graph = WeightedGraph()
    graph.add_edge(4, 6, 18)
    graph.add_edge(4, 9, 76)
    graph.add_edge(4, 12, 13)
    graph.add_edge(6, 20, 10)
    graph.add_edge(6, 13, 54)
    graph.add_edge(13, 7, 24)
    graph.add_edge(9, 28, 3)

    assert (
        graph.breadth_first_traversal(9)[1] == 4
        or graph.breadth_first_traversal(9)[1] == 28
    )
    assert (
        graph.breadth_first_traversal(9)[3] == 6
        or graph.breadth_first_traversal(9)[3] == 12
    )
    assert graph.breadth_first_traversal(9)[-1] == 7


def test_find_paths():
    graph = WeightedGraph()
    graph.add_edge("A", "B", 7)
    graph.add_edge("A", "E", 1)
    graph.add_edge("B", "C", 3)
    graph.add_edge("B", "D", 2)
    graph.add_edge("C", "D", 4)
    assert len(graph._find_all_paths("A", "D")) == 2
    assert len(graph._find_all_paths("C", "E")) == 2


def test_shortest_path():
    graph = WeightedGraph()
    graph.add_edge("A", "B", 7)
    graph.add_edge("A", "E", 1)
    graph.add_edge("B", "C", 3)
    graph.add_edge("B", "D", 2)
    graph.add_edge("C", "D", 4)

    assert graph._find_shortest_path("A", "D") == ["A", "B", "D"]

    graph.add_edge("D", "E", 6)

    assert graph._find_shortest_path("A", "D") == ["A", "E", "D"]


def test_dijkstra_algorithm():
    graph = WeightedGraph()
    graph.add_edge("A", "B", 4)
    graph.add_edge("A", "C", 2)
    graph.add_edge("C", "B", 1)
    graph.add_edge("B", "E", 3)
    graph.add_edge("B", "D", 2)
    graph.add_edge("E", "D", 1)

    assert graph.dijkstra_algorithm("A") == ["A", "C"]
    assert graph.dijkstra_algorithm("D") == ["D", "E"]
