from collections import deque


def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = []
        dq = deque()
    
        for i in range(len(nums)):
        # Remove elements out of the window
            if dq and dq[0] < i - k + 1:
                dq.popleft()
        
        # Remove smaller elements from back as they won't be needed
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
        
        # Add current index
            dq.append(i)
        
        # Store max of the current window
            if i >= k - 1:
                ans.append(nums[dq[0]])
    
        return ans