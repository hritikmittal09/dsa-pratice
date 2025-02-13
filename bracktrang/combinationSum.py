class Solution:
    def combinationSum(self, candidates, target):
        res = []
        
        def backtrack(start, path,target):
            # If the current total equals target, add a copy of path to results.
            if target ==0 :
                res.append(path[:])
                return
            # If the total exceeds the target, no need to continue.
            if target <0:
                return
            
            # Try every candidate starting from the current index.
            for i in range(start, len(candidates)):
                # Include candidates[i] in the combination.
                path.append(candidates[i])
                # Because we can reuse the same candidate, we call backtrack with 'i' (not i+1)
                backtrack(i, path, target -  candidates[i])
                # Backtrack: remove the candidate added last.
                path.pop()
        
        backtrack(0, [], target)
        return res

# Example usage:
sol = Solution()
print(sol.combinationSum([2, 3, 6, 7], 7))
# Expected Output: [[2,2,3], [7]]
