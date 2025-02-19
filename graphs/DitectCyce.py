def solve(src, adj, v, cp):
    cp[src] = True
    v[src] = True

    for nei in adj[src]:
        if not v[nei]:  # If not visited, do DFS
            if solve(nei, adj, v, cp):
                return True
        elif cp[nei]:  # If already in recursion stack, cycle detected
            return True

    cp[src] = False  # Remove from recursion stack before returning
    return False

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        adj = {i: [] for i in range(numCourses)}
        v = [False] * numCourses  # Visited array
        cp = [False] * numCourses  # Recursion stack

        for u, v in prerequisites:
            adj[u].append(v)  # Create adjacency list

        for course in range(numCourses):  # Check for cycles in all nodes
            if not v[course]:  # Only check unvisited nodes
                if solve(course, adj, v, cp):
                    return False  # If cycle found, return False

        return True  # If no cycle, return True
