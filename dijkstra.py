# dijkstra.py
import heapq

def dijkstra(graph, start, goal):
    pq = [(0, start)]
    dist = {start: 0}
    parent = {start: None}

    while pq:
        current_dist, node = heapq.heappop(pq)

        if node == goal:
            break

        if current_dist > dist[node]:
            continue

        for neighbor, weight in graph.neighbors(node):
            new_dist = current_dist + weight
            if neighbor not in dist or new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                parent[neighbor] = node
                heapq.heappush(pq, (new_dist, neighbor))

    # reconstruct path
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent.get(node)
    path.reverse()

    return path, dist.get(goal, float("inf"))
