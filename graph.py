# graph.py
class Graph:
    def __init__(self):
        self.edges = {}  # adjacency list: node -> list of (neighbor, weight)

    def add_node(self, node):
        if node not in self.edges:
            self.edges[node] = []

    def add_edge(self, u, v, weight):
        self.add_node(u)
        self.add_node(v)
        self.edges[u].append((v, weight))

    def neighbors(self, node):
        return self.edges.get(node, [])
