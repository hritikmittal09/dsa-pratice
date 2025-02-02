class Solution:
    
    
    
    def isValid(self, arr, n, k, m):
        student = 1
        s = 0  # Start with zero sum
        
        for i in arr:
            s += i
            if s > m:
                student += 1
                s = i  # Reset sum to the current book's pages
            
            if student > k:
                return False
                
        return True      
    #Function to find minimum number of pages.
    def findPages(self, arr, k):
        if k > len(arr):  # If students are more than books, allocation isn't possible
            return -1

        l = max(arr)  # Minimum possible max pages
        h = sum(arr)  # Maximum possible max pages
        res = -1
        
        while l <= h:
            mid = (l + h) // 2
            if self.isValid(arr, len(arr), k, mid):  # Use `self.isValid`
                res = mid
                h = mid - 1  # Try to minimize max pages
            else:
                l = mid + 1  # Increase max pages if allocation fails
                
        return res