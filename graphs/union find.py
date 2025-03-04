class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n  # Rank for union by rank

    def find(self, x):
        """Find with path compression"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        """Union by rank"""
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False  # Cycle detected
        
        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        
        return True  # Union successful

def has_cycle(edges, n):
    """
    Detects if an undirected graph has a cycle using Union-Find.

    :param edges: List of (u, v) edges
    :param n: Number of nodes
    :return: True if cycle exists, else False
    """
    uf = UnionFind(n)

    for u, v in edges:
        if not uf.union(u, v):  # If union fails, a cycle exists
            return True

    return False

# Example Graph (with cycle)
edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
n = 4  # Number of nodes
print("Cycle detected:", has_cycle(edges, n))  # Output: True

# Example Graph (without cycle)
edges = [(0, 1), (1, 2), (2, 3)]
print("Cycle detected:", has_cycle(edges, n))  # Output: False
