class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Step 1: Sort the array
        n = len(nums)
        ans = []

        for i in range(n - 2):  # Fix the first number
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate values for 'i'
                continue

            left, right = i + 1, n - 1  # Two pointers
            while left < right:
                total = nums[i] + nums[left] + nums[right]  # Sum of three numbers

                if total == 0:  # Found a triplet
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip duplicate values for 'left' and 'right'
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:  # Need a larger sum
                    left += 1
                else:  # Need a smaller sum
                    right -= 1

        return ans
        