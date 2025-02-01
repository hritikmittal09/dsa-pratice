from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = []
        c = Counter(nums)
        s = sorted(c.items(), key=lambda x: x[1], reverse=True)
        i =0
        for i in range(k):
            ans.append(s[i][0])
            i+=1
        print(s)    
        return ans
