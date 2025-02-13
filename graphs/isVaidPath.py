def validPath(self, n, edges, source, destination):
        g = {}
        for i in range(n):
            g[i] = []
        for u ,v in edges:
            g[u].append(v)
            g[v].append(u)
        v = [False] *n
        s = [source]
        ans = []
        v[source] =True
        while s :
            node = s.pop()
            if node == destination :
                return True
            ans.append(node)
            for i in g[node]:
                if not v[i]:
                    s.append(i)
                    v[i] = True
        return False            

               

        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        