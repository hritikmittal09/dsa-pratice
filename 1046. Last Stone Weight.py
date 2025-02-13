import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        mhp = [-stone for stone in  stones]
        heapq.heapify(mhp)
        while len(mhp) > 1:
            f = -heapq.heappop(mhp)
            s = -heapq.heappop(mhp)
            if f != s:
                heapq.heappush(mhp, -(f - s))
        if len(mhp) ==1 :
            return -mhp[0]
        else :
            return 0            
