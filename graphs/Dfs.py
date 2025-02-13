def dfsOfGraph(self, adj):
        g = {}
        for index,value in enumerate(adj):
            g[index] = value
        #print(g)
        root =list( g.keys())[0]
        s = [root]
        
        
        ans = []
        v =[False] * len(g)
        while s :
            node = s .pop()
            if v[node] !=True:
                ans.append(node)
            v[node ] =True
            for i in reversed(g[node]):
                if v[i] ==False:
                    s .append(i)
        return ans    