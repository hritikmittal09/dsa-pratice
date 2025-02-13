
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def dfs(node, m):
    if node is None :
        return node
    if node in m :
        return m[node]
    copy = Node(node.val)
    m[node] =copy
    for nei in node.neighbors:
        copy.neighbors.append(dfs(nei,m))
    return copy    

        

class Solution(object):
    def cloneGraph(self, node):
        m = {}
        return dfs(node,m)
        """
        :type node: Node
        :rtype: Node
        """
    