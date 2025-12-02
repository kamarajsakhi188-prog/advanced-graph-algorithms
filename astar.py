# astar.py
import heapq
import math

def heuristic(a, b):
    # simple admissible heuristic
    return abs(a - b)  # works for abstract numbered nodes

def astar(graph, start, goal):
    pq = [(0, start)]
    g = {start: 0}
    parent = {start: None}

    while pq:
        _, node = heapq.heappop(pq)

        if node == goal:
            break

        for neighbor, weight in graph.neighbors(node):
            new_cost = g[node] + weight
            if neighbor not in g or new_cost < g[neighbor]:
                g[neighbor] = new_cost
                f = new_cost + heuristic(neighbor, goal)
                parent[neighbor] = node
                heapq.heappush(pq, (f, neighbor))

    # reconstruct path
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent.get(node)
    path.reverse()

    return path, g.get(goal, float("inf"))
