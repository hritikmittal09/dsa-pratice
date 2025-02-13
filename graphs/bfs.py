from collections import deque


def bfsOfGraph(self, adj) :
        g = {index: value for index, value in enumerate(adj)}  # Convert list to dict
        root = list(g.keys())[0]  # Get the first node as the root
        s = deque([root])
        
        ans = []
        v = [False] * len(g)  # Visited array
        v[root] = True  # Mark root as visited before enqueuing

        while s:
            node = s.popleft()
            ans.append(node)  # Add node to answer list

            for i in g[node]:  # Traverse all neighbors
                if not v[i]:  
                    s.append(i)
                    v[i] = True  # Mark as visited when adding to queue
        
        return ans
        