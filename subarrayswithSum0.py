class Solution(object):
    def numOfSubarraysWithZeroSum(self, arr):
        count = 0  # Number of subarrays with sum zero
        prefix_sum = 0
        freq = {0: 1}  # Initialize with {0:1} to count subarrays starting from index 0

        for num in arr:
            prefix_sum += num  # Update prefix sum
            
            # If prefix_sum is already in the map, add its count to result
            if prefix_sum in freq:
                count += freq[prefix_sum]

            # Update the frequency of prefix_sum
            freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

        return count
