class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        m = int(1e9 + 7)
        c = 0  # Count of valid subarrays
        e = 1  # Count of even prefix sums (including the empty prefix)
        o = 0  # Count of odd prefix sums
        prefix_sum = 0  # Running prefix sum

        for num in arr:
            prefix_sum += num
            if prefix_sum % 2 == 0:
                c = (c + o) % m  # Add the count of odd prefix sums
                e += 1  # Increase count of even prefix sums
            else:
                c = (c + e) % m  # Add the count of even prefix sums
                o += 1  # Increase count of odd prefix sums
        
        return c
        