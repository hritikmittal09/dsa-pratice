class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        """
        n = len(nums)
        ans = []
        pre = [1 for i in range(n)]
        suf = [1 for i in range(n) ]
        pre[0] =1
        suf [n-1] = 1
        for i in range(1,n):
            pre[i] = pre[i-1] * nums[i-1]
        for i in range(n-2,-1,-1):
            suf[i] = suf[i+1] * nums[i+1]
        for i in range(n):
            ans.append(suf[i]*pre[i])
        return ans        
                


        