class Solution:
    def combinationSum2(self, candidates, target):
        result = []
        candidates.sort()  # Sort to handle duplicates
        self.helper(0, [], 0, target, candidates, result)
        return result

    def helper(self, index, path, total, target, candidates, result):
        if total == target:
            result.append(path[:])  # Append a copy of the valid combination
            return
        if total > target or index >= len(candidates):
            return

        # Include the current element
        self.helper(index + 1, path + [candidates[index]], total + candidates[index], target, candidates, result)

        # Move to the next different element to avoid duplicates
        while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
            index += 1  # Skip duplicate numbers

        # Exclude the current element and move forward
        self.helper(index + 1, path, total, target, candidates, result)


# Example Usage
sol = Solution()
print(sol.combinationSum2([10,1,2,7,6,1,5], 8))
# Output: [[1,1,6], [1,2,5], [1,7], [2,6]]
