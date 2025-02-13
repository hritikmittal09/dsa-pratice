class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()  # Sort to handle duplicates
        res = []
        
        def backtrack(start, path, target):
            # If target is 0, we found a valid combination
            if target == 0:
                res.append(path[:])
                return
            # If target goes below zero, no need to continue
            if target < 0:
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicates on the same recursion level
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                # Include the candidate and reduce the target
                path.append(candidates[i])
                backtrack(i + 1, path, target - candidates[i])
                # Backtrack: remove the candidate
                path.pop()
        
        backtrack(0, [], target)
        return res

# Example usage:
sol = Solution()
print(sol.combinationSum2([10,1,2,7,6,1,5], 8))
# Expected Output: [[1,1,6], [1,2,5], [1,7], [2,6]]
