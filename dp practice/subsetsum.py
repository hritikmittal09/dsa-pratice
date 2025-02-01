def subsetSum(nums: list[int], target: int) -> bool:
    n = len(nums)
    # Initialize the DP table with False
    t = [[False for _ in range(target + 1)] for _ in range(n + 1)]

    # Base Case: A target sum of 0 is always possible (empty subset)
    for i in range(n + 1):
        t[i][0] = True

    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if nums[i-1] <= j:
                # Include the current element or exclude it
                t[i][j] = t[i-1][j-nums[i-1]] or t[i-1][j]
            else:
                # Exclude the current element
                t[i][j] = t[i-1][j]

    return t[n][target]


# Test the function
nums = [5, 3, 4, 7]
t = 7
result = subsetSum(nums, t)
print(result)
