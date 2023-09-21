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


def test_delete_node():
    graph = Graph()
    graph.add_edge(4, 6)
    graph.add_edge(4, 9)
    graph.add_edge(20, 6)

    assert graph._storage == {4: {(4, 6), (4, 9)}, 6: {(6, 4), (6, 20)}, 9: {(9, 4)}, 20: {(20, 6)}}

    graph.del_node(6)

    assert graph._storage == {4: {(4, 9)}, 9: {(9, 4)}, 20: {}}
