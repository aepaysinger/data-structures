class WeightedGraph:
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
                edges.append((node, edge[0]))
        return edges

    def add_node(self, value):
        """Adds a new node(value) to the graph."""
        self._storage[value] = set()

    def add_edge(self, value1, value2, weight):
        """
        Add a new edge to the graph connecting the node containing 'value1' and the node containing 'value2'.
        If either value1 or value2 are not already present in the graph, they should be added. If an edge already exisits overwrite it.
        """
        if value1 not in self._storage:
            self._storage[value1] = {(value2, weight)}
        if value2 not in self._storage:
            self._storage[value2] = {(value1, weight)}

        self._storage[value1].add((value2, weight))
        self._storage[value2].add((value1, weight))

    def del_node(self, value):
        """Delete the node containing 'value' from the graph; raise an error if no such node exists."""
        to_remove = []
        if value in self._storage:
            for edges in self._storage[value]:
                to_remove.append((edges[0], (value, edges[1])))
            for items in to_remove:
                self._storage[items[0]].remove(items[1])
            del self._storage[value]
        else:
            raise ValueError("Node does not exist")

    def del_edge(self, value1, value2):
        "Delete the edge connecting 'value1' and 'value2' from the graph; raise an error if no such edge exsits."
        to_remove = []
        if (value1, value2) in self.edges():
            for edges in self._storage[value1]:
                if edges[0] == value2:
                    to_remove.append(edges)
            for edges in self._storage[value2]:
                if edges[0] == value1:
                    to_remove.append(edges)
            self._storage[value1].remove(to_remove[0])
            self._storage[value2].remove(to_remove[1])
        else:
            raise ValueError("Edge does not exist.")

    def has_node(self, value):
        """Return if node containing 'value' is contained in the graph."""
        return value in self._storage

    def neighbors(self, value):
        """Return a list of all nodes connected to the node containing 'value' by edges; raise an error if 'value' is nto in graph."""
        if value in self._storage:
            return [edge_value[0] for edge_value in self._storage[value]]
        else:
            raise ValueError("Value not in graph.")

    def adjacent(self, value1, value2):
        """Return if there is an edge connecting 'value1' and 'value2'; raise an error if either of the supplied values are not in graph."""
        adjacent = False
        if value1 not in self._storage or value2 not in self._storage:
            raise ValueError("One of the values are not in the graph")
        for edges in self._storage[value1]:
            if edges[0] == value2:
                adjacent = True
                break
        return adjacent

    def depth_first_traversal(self, start_val):
        """Return a list of depth_first_traversal starting at start_val"""
        path = [start_val]
        track = []

        for edge in self._storage[start_val]:
            track.append(edge[0])
        while track:
            current = track.pop(-1)
            path.append(current)
            for edge in self._storage[current]:
                if edge[0] not in path:
                    track.append(edge[0])
        return path

    def breadth_first_traversal(self, start_val):
        """Return a list of breadth_first_traversal starting at start_val"""
        path = [start_val]
        need_to_check = [start_val]

        while need_to_check:
            val = need_to_check.pop(0)
            for edge, weight in self._storage[val]:
                if edge not in path:
                    path.append(edge)
                    need_to_check.append(edge)

        return path

    def _find_all_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        paths = []
        for node, weight in self._storage[start]:
            if node not in path:
                new_paths = self._find_all_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths

    def _find_shortest_path(self, start, end):
        paths_with_weight = []

        for path in self._find_all_paths(start, end):
            total_weight = 0

            for i, node in enumerate(path):
                if i == len(path) - 1:
                    break
                for edges in self._storage[node]:
                    if edges[0] == path[i + 1]:
                        total_weight += edges[1]
            paths_with_weight.append((total_weight, path))

        return min(paths_with_weight)[1]

    def dijkstra_algorithm(self, start):
        unvisited_nodes = set()
        distance = {}
        for node in self._storage:
            unvisited_nodes.add(node)
            distance[node] = float("inf")

        distance[start] = 0
        previous_node = {node: None for node in self._storage}

        while unvisited_nodes:
            current_node = min(unvisited_nodes, key=lambda node: distance[node])
            unvisited_nodes.remove(current_node)

            for edge, weight in self._storage[current_node]:
                if edge in unvisited_nodes:
                    new_distance = distance[current_node] + weight
                    if new_distance < distance[edge]:
                        distance[edge] = new_distance
                        previous_node[edge] = current_node

        shortest_paths = {}
        for node in self._storage:
            path = []
            current = node
            while current is not None:
                path.insert(0, current)
                current = previous_node[current]
            shortest_paths[node] = [distance[node], path]
        del shortest_paths[start]
        return shortest_paths[min(shortest_paths, key=lambda node: distance[node])][1]

    def bellmanford_algorithm(self, start):
        distance = {}
        predecessor = {}
        for node_a, node_b in self.edges():
            if node_a not in distance:
                distance[node_a] = float("inf")
                predecessor[node_a] = None
            if node_b not in distance:
                distance[node_b] = float("inf")
                predecessor[node_b] = None
        distance[start] = 0
        for _ in range(len(self._storage) - 1):
            for node, edges in self._storage.items():
                for edge, weight in edges:
                    if distance[edge] > distance[node]:
                        distance[edge] = distance[node] + weight
                        predecessor[edge] = node
        for node, edges in self._storage.items():
            for edge, weight in edges:
                if distance[edge] > distance[node] + weight:
                    return "negative"
        return distance

    def _add_edge_single(self, value1, value2, weight):
        if value1 not in self._storage:
            self._storage[value1] = {(value2, weight)}
        self._storage[value1].add((value2, weight))
