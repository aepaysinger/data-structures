class Graph:
    def __init__(self):
        self._storage = {}

    def nodes(self):
        """Return a list of all the nodes in the graph."""
        return [node for node in self._storage]

    def edges(self):
        """Return a list of all the edges in the graph."""
        edges = []
        for node in self._storage:
            for edge in self._storage[node]:
                edges.append((node, edge))
        return edges

    def add_node(self, value):
        """Adds a new node(value) to the graph."""
        self._storage[value] = set()

    def add_edge(self, value1, value2):
        """
        Add a new edge to the graph connecting the node containing 'value1' and the node containing 'value2'.
        If either value1 or value2 are not already present in the graph, they should be added. If an edge already exisits overwrite it.
        """
        if value1 not in self._storage:
            self._storage[value1] = {value2}
        if value2 not in self._storage:
            self._storage[value2] = {value1}

        self._storage[value1].add(value2)
        self._storage[value2].add(value1)

    def del_node(self, value):
        """Delete the node containing 'value' from the graph; raise an error if no such node exists."""
        if value in self._storage:
            del self._storage[value]
            for edges in self._storage.values():
                if value in edges:
                    edges.remove(value)
        else:
            raise ValueError("Node does not exist")

    def del_edge(self, value1, value2):
        "Delete the edge connecting 'value1' and 'value2' from the graph; raise an error if no such edge exsits."
        if value2 in self._storage[value1]:
            self._storage[value1].remove(value2)
            self._storage[value2].remove(value1)
        else:
            raise ValueError("Edge does not exist.")

    def has_node(self, value):
        """Return if node containing 'value' is contained in the graph."""
        return value in self._storage

    def neighbors(self, value):
        """Return a list of all nodes connected to the node containing 'value' by edges; raise an error if 'value' is nto in graph."""
        if value in self._storage:
            return [edge_value for edge_value in self._storage[value]]
        else:
            raise ValueError("Value not in graph.")

    def adjacent(self, value1, value2):
        """Return if there is an edge connecting 'value1' and 'value2'; raise an error if either of the supplied values are not in graph."""
        if value1 not in self._storage or value2 not in self._storage:
            raise ValueError("One of the values are not in the graph")
        return value2 in self._storage[value1]

    def depth_first_traversal(self, start_val):
        """Return a list of depth_first_traversal starting at start_val"""
        path = [start_val]
        track = []

        for edge in self._storage[start_val]:
            track.append(edge)
        while track:
            current = track.pop(-1)
            path.append(current)
            for edge in self._storage[current]:
                if edge not in path:
                    track.append(edge)
        return path

    def breadth_first_traversal(self, start_val):
        """Return a list of breadth_first_traversal starting at start_val"""
        path = [start_val]
        need_to_check = [start_val]

        while need_to_check:
            val = need_to_check.pop(0)
            for edges in self._storage[val]:
                if edges not in path:
                    path.append(edges)
                    need_to_check.append(edges)

        return path

    def _find_all_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        paths = []
        for node in self._storage[start]:
            if node not in path:
                new_paths = self._find_all_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths


if __name__ == "__main__":
    graph = Graph()
    graph.add_edge("A", "B")
    graph.add_edge("A", "E")
    graph.add_edge("B", "C")
    graph.add_edge("B", "D")
    graph.add_edge("C", "D")
    print(graph._find_all_paths("A", "D"))
