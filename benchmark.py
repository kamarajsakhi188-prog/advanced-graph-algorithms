# benchmark.py
import random
import time
from graph import Graph
from dijkstra import dijkstra
from astar import astar

def generate_random_graph(n=150, edges_per_node=4):
    graph = Graph()
    for u in range(n):
        for _ in range(edges_per_node):
            v = random.randint(0, n - 1)
            weight = random.randint(1, 20)
            graph.add_edge(u, v, weight)
    return graph

def benchmark():
    graph = generate_random_graph()

    pairs = [(0, 50), (10, 70), (25, 120), (15, 90), (5, 140)]
    print("Benchmarking Dijkstra vs A*\n")

    for start, goal in pairs:
        print(f"Test: {start} → {goal}")

        # Dijkstra
        t1 = time.time()
        _, dist_d = dijkstra(graph, start, goal)
        t2 = time.time()

        # A*
        t3 = time.time()
        _, dist_a = astar(graph, start, goal)
        t4 = time.time()

        print(f"Dijkstra: {t2 - t1:.6f}s   Distance={dist_d}")
        print(f"A*:       {t4 - t3:.6f}s   Distance={dist_a}\n")

if __name__ == "__main__":
    benchmark()
