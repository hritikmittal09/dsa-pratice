def Iscycle(src,adj,v,cp,res):
    v[src] = True
    cp[src] = True

    for nei in adj[src]:
        
        if cp[nei] :
            return True
        if not v[nei]  and Iscycle(nei,adj,v,cp,res):
            return True
    cp[src] =False
    res.append(src)
    return False



            



    
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        adj = {i: [] for i in range(numCourses)}
        for u, v in prerequisites:
            adj[v].append(u)  # Reverse edge to maintain dependency order

        cp = [False] * numCourses  # Recursion stack
        vi = [False] * numCourses  # Visited nodes
        res = []

        for i in range(numCourses):
            if not vi[i]:
                if Iscycle(i, adj, vi, cp, res):
                    return []  # Cycle detected → No valid order

        return res[::-1]