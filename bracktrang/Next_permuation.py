def nextPermutation(nums):
    n = len(nums)
    i = n - 2

    # Step 1: Find first decreasing index
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:  # If we found such an index
        j = n - 1
        while nums[j] <= nums[i]:  # Step 2: Find next larger element
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]  # Swap

    # Step 3: Reverse the right part
    nums[i + 1:] = reversed(nums[i + 1:])

# Example Usage:
nums = [1, 2, 3]
nextPermutation(nums)
print(nums)  # Output: [1, 3, 2]
