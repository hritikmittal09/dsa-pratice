def maxArea( height):
        """
        :type height: List[int]
        :rtype: int
        """
        l =0
        r = len(height) -1
        ma =0
        while l < r :
            h = min(height[l],height[r])
            w = r -l
            a = h *w
            ma = max(ma, a)
            if height[l] >height[r]:
                r -=1
            else :
                l+=1
        return ma             
h = [1,8,6,2,5,4,8,3,7]
print(maxArea(h))
