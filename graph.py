from linkedlist import LinkedList


class Graph:
    def __init__(self):
        self._storage = {}

    def nodes(self):
        """Returns a list of all the nodes in the graph/"""
        return [node for node in self._storage]

    def edges(self):
        """Returns a list of all the edges in the graph."""
        return [edges for edges in self._storage.values()]

    def add_node(self, value):
        """Adds a new node with value 'n' to the graph."""
        self._storage[value] = set()

    def add_edge(self, value1, value2):
        """Adds a new edge to the graph connecting the node containing 'value1' and the node containing 'value 2'. 
        If either value1 or value2 are not already present in the graph, they should be added. If an edge already exists, overwrite it."""
        if value1 not in self._storage:
            self._storage[value1] = {(value1, value2)}
        if value2 not in self._storage:
            self._storage[value2] = {(value2, value1)}

        self._storage[value1].add((value1, value2))
        self._storage[value2].add((value2, value1))

    def del_node(self, value):
        """Deletes the node containing 'value' from the graph; raises an error if no such node exists."""
        if value in self._storage:
            del self._storage[value]
            for nodes, edges in self._storage.items():
                if (nodes, value) in edges:
                    edges.remove((nodes, value))
        else:
            raise ValueError("Node does not exist")               
        

    def del_edge(self, value1, value2):
        """Deletes the edge connecting 'value1' and 'value2' from the graph; raises an error if no such edge exists."""
        if (value1, value2) in self._storage[value1]:
            self._storage[value1].remove((value1, value2))
            self._storage[value2].remove((value2, value1))
        else:
            raise ValueError("Edge does not exist.")

    def has_node(self, value):
        """True if node containing value 'value' is contained in the graph, False if not."""
        return  value in self._storage

    def neighbors(self, value):
        """Returns the list of all nodes connected to the node containing "value" by edges; raises an error if value is not in graph."""
        

    def adjacent(self, value1, value2):
        """Returns True if there is an edge connecting 'value1' and 'value2', False if not; raises an error if either of 
        the supplied values are not in the graph."""
        pass


if __name__ == "__main__":
    graph = Graph()
    graph.add_edge(4, 6)
    graph.add_edge(4, 9)
    graph.add_edge(20, 6)
    # assert graph._storage == {4: {(4, 6), (4, 9)}, 6: {(6, 4), (6, 20)}, 9: {(9, 4)}, 20: {(20, 6)}}
    print(graph.del_edge(4, 6))