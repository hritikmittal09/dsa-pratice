from collections import Counter, defaultdict


def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""
    
    # Count frequency of characters in t
        t_count = Counter(t)
        required = len(t_count)  # Number of unique characters in t
    
    # Pointers for the sliding window
        left, right = 0, 0
    
    # Keep track of characters in the current window
        window_count = defaultdict(int)
        formed = 0  # Number of characters in the window that meet the required frequency
    
    # Result variables: (window length, left, right)
        res = float('inf'), None, None
    
        while right < len(s):
        # Add the character on the right to the window
            char = s[right]
            window_count[char] += 1
        
        # If the frequency of the current character matches that in t
            if char in t_count and window_count[char] == t_count[char]:
                formed += 1
        
        # Try to shrink the window until it's no longer valid
            while left <= right and formed == required:
                char = s[left]
            
            # Update the result if the current window is smaller
                if right - left + 1 < res[0]:
                    res = (right - left + 1, left, right)
            
            # Remove the leftmost character from the window
                window_count[char] -= 1
                if char in t_count and window_count[char] < t_count[char]:
                    formed -= 1
            
                left += 1
        
        # Expand the window by moving the right pointer
            right += 1
    
    # Return the minimum window substring
        return "" if res[0] == float('inf') else s[res[1]:res[2] + 1]

        