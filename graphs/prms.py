import heapq

def prims_algorithm(graph):
    """
    Implements Prim's Algorithm to find the Minimum Spanning Tree (MST) of a graph.

    :param graph: Dictionary where keys are node numbers and values are lists of (neighbor, weight) tuples.
    :return: The MST as a list of (node1, node2, weight) tuples.
    """
    start_node = next(iter(graph))  # Pick any starting node
    mst = []  # Store the MST edges
    visited = set()  # Keep track of visited nodes
    min_heap = [(0, start_node, None)]  # (weight, node, parent)
    
    while min_heap and len(visited) < len(graph):
        weight, node, parent = heapq.heappop(min_heap)

        if node in visited:
            continue
        
        visited.add(node)
        if parent is not None:
            mst.append((parent, node, weight))  # Add the edge to the MST

        for neighbor, edge_weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, node))

    return mst

# Example Graph (Adjacency List Representation)
graph = {
    0: [(1, 4), (7, 8)],
    1: [(0, 4), (2, 8), (7, 11)],
    2: [(1, 8), (3, 7), (8, 2), (5, 4)],
    3: [(2, 7), (4, 9), (5, 14)],
    4: [(3, 9), (5, 10)],
    5: [(2, 4), (3, 14), (4, 10), (6, 2)],
    6: [(5, 2), (7, 1), (8, 6)],
    7: [(0, 8), (1, 11), (6, 1), (8, 7)],
    8: [(2, 2), (6, 6), (7, 7)]
}

# Run Prim's Algorithm
mst = prims_algorithm(graph)
print("Minimum Spanning Tree (MST):", mst)
