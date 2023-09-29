from linkedlist import LinkedList


class Graph:
    def __init__(self):
        self._storage = {}

    def nodes(self):
        """Return a list of all the nodes in the graph."""
        return [node for node in self._storage]

    def edges(self):
        """Return a list of all the edges in the graph."""
        return [edges for edges in self._storage.values()]

    def add_node(self, value):
        """Adds a new node(value) to the graph."""
        self._storage[value] = set()

    def add_edge(self, value1, value2):
        """
        Add a new edge to the graph connecting the node containing 'value1' and the node containing 'value2'.
        If either value1 or value2 are not already present in the graph, they should be added. If an edge already exisits overwrite it.
        """
        if value1 not in self._storage:
            self._storage[value1] = {(value1, value2)}
        if value2 not in self._storage:
            self._storage[value2] = {(value2, value1)}

        self._storage[value1].add((value1, value2))
        self._storage[value2].add((value2, value1))

    def del_node(self, value):
        """Delete the node containing 'value' from the graph; raise an error if no such node exists."""
        if value in self._storage:
            del self._storage[value]
            for node, edges in self._storage.items():
                if (node, value) in edges:
                    edges.remove((node, value))
        else:
            raise ValueError("Node does not exist")

    def del_edge(self, value1, value2):
        "Delete the edge connecting 'value1' and 'value2' from the graph; raise an error if no such edge exsits."
        if (value1, value2) in self._storage[value1]:
            self._storage[value1].remove((value1, value2))
            self._storage[value2].remove((value2, value1))
        else:
            raise ValueError("Edge does not exist.")

    def has_node(self, value):
        """Return if node containing 'value' is contained in the graph."""
        return value in self._storage

    def neighbors(self, value):
        """Return a list of all nodes connected to the node containing 'value' by edges; raise an error if 'value' is nto in graph."""
        if value in self._storage:
            return [edge_value[1] for edge_value in self._storage[value]]
        else:
            raise ValueError("Value not in graph.")

    def adjacent(self, value1, value2):
        """Return if there is an edge connecting 'value1' and 'value2'; raise an error if either of the supplied values are not in graph."""
        if value1 not in self._storage or value2 not in self._storage:
            raise ValueError("One of the values are not in the graph")
        return (value1, value2) in self._storage[value1]
