def canSum(nums: list[int], x: int, n: int, memo=None, pos=0):
    if memo is None:
        memo = {}
    if x in memo:
        return memo[x]
    if x == 0:
        return []
    elif x < 0:
        return None

    for i in nums:
        reminder = x - i
        res = canSum(nums, reminder, n, memo)
        if res is not None:
            memo[x] = res + [i]  # Append the current number to the result
            return memo[x]

    memo[x] = None  # Store None in memo if no solution exists
    return None


nums = [5, 3, 4, 7]
target = 7
n = len(nums)
result = canSum(nums, target, n)
print(result)
