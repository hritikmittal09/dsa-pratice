class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        g ={}
        n = len(strs)
        for i in range(n):
            s = "".join(sorted(strs[i]))
            g[s] =[]
        for i in strs:
            s = "".join(sorted(i))
            g[s].append(i)
        return g.values()        
            