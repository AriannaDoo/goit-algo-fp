from __future__ import annotations
import heapq
from typing import Dict, List, Tuple, Any


Graph = Dict[Any, List[Tuple[Any, float]]]  


def dijkstra(graph: Graph, start: Any) -> Dict[Any, float]:
   
    dist: Dict[Any, float] = {node: float("inf") for node in graph}
    dist[start] = 0.0

    pq: List[Tuple[float, Any]] = [(0.0, start)] 

    while pq:
        cur_dist, u = heapq.heappop(pq)
        if cur_dist > dist[u]:
            continue  # устаревшая запись

        for v, w in graph.get(u, []):
            new_dist = cur_dist + w
            if new_dist < dist.get(v, float("inf")):
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))

    return dist


if __name__ == "__main__":
    # Demo graph
    graph: Graph = {
        "A": [("B", 4), ("C", 2)],
        "B": [("A", 4), ("C", 1), ("D", 5)],
        "C": [("A", 2), ("B", 1), ("D", 8), ("E", 10)],
        "D": [("B", 5), ("C", 8), ("E", 2), ("F", 6)],
        "E": [("C", 10), ("D", 2), ("F", 2)],
        "F": [("D", 6), ("E", 2)],
    }

    start_node = "A"
    distances = dijkstra(graph, start_node)

    print(f"Shortest distances from {start_node}:")
    for node, d in sorted(distances.items()):
        print(f"{node}: {d}")
